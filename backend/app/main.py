"""
API Sentinel — Phase 1
Minimal FastAPI application with health-check endpoint.
"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from .env (if it exists)
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "api-sentinel")
APP_ENV = os.getenv("APP_ENV", "development")

app = FastAPI(
    title=APP_NAME,
    description="API Sentinel — an API monitoring platform",
    version="0.1.0",
)


@app.get("/")
def root():
    """Welcome endpoint."""
    return {
        "message": f"Welcome to {APP_NAME}",
        "environment": APP_ENV,
    }


@app.get("/health")
def health_check():
    """Health-check endpoint used by uptime monitors."""
    return {
        "status": "healthy",
        "service": "api-sentinel",
    }
