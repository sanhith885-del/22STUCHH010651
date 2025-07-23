from datetime import datetime
from typing import Dict, Any

url_clicks: Dict[str, int] = {}
url_creation_times: Dict[str, datetime] = {}

def track_click(short_url: str) -> None:
    """Track a click on a shortened URL."""
    if short_url in url_clicks:
        url_clicks[short_url] += 1
    else:
        url_clicks[short_url] = 1
        url_creation_times[short_url] = datetime.now()

def get_stats(short_url: str) -> Dict[str, Any]:
    """Retrieve analytics for a shortened URL."""
    clicks = url_clicks.get(short_url, 0)
    creation_time = url_creation_times.get(short_url)
    return {
        "short_url": short_url,
        "clicks": clicks,
        "creation_time": creation_time.isoformat() if creation_time else None,
    }