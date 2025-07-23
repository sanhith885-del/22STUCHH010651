from fastapi import HTTPException
from pydantic import BaseModel, HttpUrl
import random
import string
import time
from datetime import datetime, timedelta
from src.middleware.logging import log

class URL(BaseModel):
    original_url: HttpUrl
    short_code: str = None
    created_at: datetime = None
    expires_at: datetime = None

url_storage = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_short_url(original_url: str, custom_code: str = None):
    if custom_code and custom_code in url_storage:
        raise HTTPException(status_code=400, detail="Custom code already exists.")
    
    short_code = custom_code if custom_code else generate_short_code()
    expires_at = datetime.now() + timedelta(days=30)  
    
    url_entry = URL(original_url=original_url, short_code=short_code, created_at=datetime.now(), expires_at=expires_at)
    url_storage[short_code] = url_entry
    
    log({
        "stack": "shortener.create_short_url",
        "level": "info",
        "pkg": "url-shortener-microservice",
        "message": f"Created short URL: {short_code} for {original_url}"
    })
    
    return url_entry

def get_original_url(short_code: str):
    url_entry = url_storage.get(short_code)
    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found.")
    
    if url_entry.expires_at < datetime.now():
        raise HTTPException(status_code=410, detail="Short URL has expired.")
    
    log({
        "stack": "shortener.get_original_url",
        "level": "info",
        "pkg": "url-shortener-microservice",
        "message": f"Retrieved original URL for short code: {short_code}"
    })
    
    return url_entry.original_url

def get_all_urls():
    return list(url_storage.values())