from pydantic_settings import BaseSettings, SettingsConfigDict

# após instalar o pydantic-settings, eu uso como modelo o BaseSettings na classe Settings()


class Settings(BaseSettings):
    # no SettingsConfigDict eu informo qual o arquivo env do meu projeto e o encoding
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # defino qual é o campo do meu .env e o tipo dele, que nesse caso é string
    DATABASE_URL: str

    # exemplo do arquivo .env
    # DATABASE_URL="sqlite://database.db"
