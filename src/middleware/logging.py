from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from .log import log
import httpx


async def log(params):
    testapiserver = "http://20.244.56.144/evaluation-service/auth"
    async with httpx.AsyncClient() as client:
        response = await client.post(testapiserver, json=params)
        response.raise_for_status()
        return response.json()
    
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        log_params = {
            "stack": "Incoming Request",
            "level": "INFO",
            "pkg": "url-shortener-microservice",
            "message": f"Request: {request.method} {request.url}"
        }
        await log(log_params)

        response: Response = await call_next(request)

        log_params = {
            "stack": "Outgoing Response",
            "level": "INFO",
            "pkg": "url-shortener-microservice",
            "message": f"Response: {response.status_code} for {request.method} {request.url}"
        }
        await log(log_params)

        return response

