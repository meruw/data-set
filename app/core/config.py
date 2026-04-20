from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # =========================
    # SAP config
    # =========================
    SAP_BASE_URL: str
    SAP_COMPANY_DB: str
    SAP_USERNAME: str
    SAP_PASSWORD: str

    # =========================
    # app config
    # =========================
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # =========================
    # local config
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


# singleton instance
settings = Settings()