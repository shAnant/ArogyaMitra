from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GROQ_API_KEY: str
    SPOONACULAR_API_KEY: str
    YOUTUBE_API_KEY: str 
    GOOGLE_API_KEY: str
    
    GOOGLE_CALENDAR_CLIENT_ID: str
    GOOGLE_CALENDAR_CLIENT_SECRET: str
    GOOGLE_CALENDAR_REDIRECT_URI: str

    class Config:
        env_file = ".env"


settings = Settings()