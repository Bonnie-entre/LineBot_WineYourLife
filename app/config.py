from pydantic import BaseSettings

class Settings(BaseSettings):
    LINE_CHANNEL_ACCESS_TOKEN: str
    LINE_CHANNEL_SECRET: str
    GOOGLE_MAP_API_KEY: str
    class Config:
        env_file = "../.env"


settings = Settings()
