from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    binance_api_base: str = "https://p2p.binance.com"
    scan_interval_seconds: int = 30
    telegram_bot_token: str = ""
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/binance_p2p"
    redis_url: str = "redis://localhost:6379/0"
    cors_origins: str = "http://localhost:8000"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
