from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    SMTP_HOST: str = "sandbox.smtp.mailtrap.io"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    FROM_EMAIL: str = "no-reply@yourapp.com"
    FRONTEND_URL: str = "http://localhost:3000"

    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    TEST_MODE: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()