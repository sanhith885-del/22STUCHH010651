from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.shortener import ShortenerService
from src.middleware.logging import log

router = APIRouter()
shortener_service = ShortenerService()

class URLRequest(BaseModel):
    original_url: str
    custom_shortcode: str = None

class URLResponse(BaseModel):
    short_url: str
    original_url: str

class AnalyticsResponse(BaseModel):
    short_url: str
    clicks: int

@router.post("/shorten", response_model=URLResponse)
async def shorten_url(url_request: URLRequest):
    log({
        "stack": "API",
        "level": "info",
        "pkg": "url-shortener-microservice",
        "message": f"Shortening URL: {url_request.original_url}"
    })
    try:
        short_url = shortener_service.create_short_url(url_request.original_url, url_request.custom_shortcode)
        return {"short_url": short_url, "original_url": url_request.original_url}
    except Exception as e:
        log({
            "stack": "API",
            "level": "error",
            "pkg": "url-shortener-microservice",
            "message": str(e)
        })
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{shortcode}", response_model=URLResponse)
async def redirect_url(shortcode: str):
    log({
        "stack": "API",
        "level": "info",
        "pkg": "url-shortener-microservice",
        "message": f"Redirecting to shortcode: {shortcode}"
    })
    original_url = shortener_service.get_original_url(shortcode)
    if not original_url:
        log({
            "stack": "API",
            "level": "warning",
            "pkg": "url-shortener-microservice",
            "message": f"Shortcode not found: {shortcode}"
        })
        raise HTTPException(status_code=404, detail="Shortcode not found")
    return {"short_url": shortcode, "original_url": original_url}

@router.get("/analytics/{shortcode}", response_model=AnalyticsResponse)
async def get_analytics(shortcode: str):
    log({
        "stack": "API",
        "level": "info",
        "pkg": "url-shortener-microservice",
        "message": f"Retrieving analytics for shortcode: {shortcode}"
    })
    clicks = shortener_service.get_clicks(shortcode)
    return {"short_url": shortcode, "clicks": clicks}