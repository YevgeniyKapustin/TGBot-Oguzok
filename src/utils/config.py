from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN: str

    class Config:
        env_file = '../../.env'
        env_file_encoding = 'utf-8'
