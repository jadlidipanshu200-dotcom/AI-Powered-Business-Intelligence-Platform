"""
Application configuration settings.
"""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    APP_NAME: str = "AI-Powered Business Intelligence Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("ENVIRONMENT", "development") == "development"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://biuser:bipassword@localhost:5432/business_intelligence"
    )
    DATABASE_ECHO: bool = DEBUG
    
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    CACHE_EXPIRE_TIME: int = int(os.getenv("CACHE_EXPIRE_TIME", "3600"))
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]
    
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    MAX_UPLOAD_SIZE: int = int(os.getenv("MAX_UPLOAD_SIZE", "10485760"))
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")
    
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "logs/app.log")
    
    MODEL_PATH: str = os.getenv("MODEL_PATH", "ml/models")
    PREDICTION_CONFIDENCE_THRESHOLD: float = float(
        os.getenv("PREDICTION_CONFIDENCE_THRESHOLD", "0.7")
    )
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
