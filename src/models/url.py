from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class URL(BaseModel):
    original_url: str
    shortened_url: str
    created_at: datetime = datetime.now()
    expires_at: Optional[datetime] = None
    custom_shortcode: Optional[str] = None

class URLAnalytics(BaseModel):
    shortened_url: str
    clicks: int = 0
    last_accessed: Optional[datetime] = None