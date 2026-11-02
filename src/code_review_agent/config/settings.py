from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root (.../python-code-review-agent), so .env is found regardless of the cwd
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"

# BaseSettings: Automatically reads configuration from environment variables and .env
# For example: KEY in .env or environment variable becomes settings.key
"""
BaseSettings
1. Does auto read of environment variables
2. Pydantic validation, try to convert in expected type --> Raises validation error if value is not of valid type

Use of SecretStr instead of str?
--> It masks the value to secure logging purpose.
--> Get the value using settings.groq_api_key.get_secret_value()
"""
class Settings(BaseSettings):
    app_name: str = "Python Code Review Agent"
    app_env: str = "development"
    debug: bool = True

    groq_api_key: SecretStr

    llm_model: str = "llama-3.3-70b-versatile" # default value, it will be over-written by .env LLM_MODEL
    llm_temperature: float = 0.0

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
settings = Settings()