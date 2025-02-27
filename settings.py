from environs import Env

env = Env()
env.read_env(".env")


class Settings:

    def get_postgres_uri(self, sync: bool = False) -> str:
        driver = "postgresql+psycopg2" if sync else "postgresql+asyncpg"
        uri = "{driver}://{user}:{password}@{host}:{port}/{name}".format(
            driver=driver,
            user=env("POSTGRES_USER"),
            password=env("POSTGRES_PASSWORD"),
            host=env("POSTGRES_HOST"),
            port=env("DB_EXTERNAL_PORT"),
            name=env("POSTGRES_DB"),
        )
        return uri
