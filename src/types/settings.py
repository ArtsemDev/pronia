import ujson
from pydantic import BaseConfig, BaseSettings, PostgresDsn
from pydantic import BaseModel


class Config(BaseConfig):
    json_dumps = ujson.dumps
    json_loads = ujson.loads
    orm_mode = True


class Schema(BaseModel):
    Config = Config


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn

    class Config:
        env_file = '.env'
