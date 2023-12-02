import os


def get_database_uri():
    db_host = os.getenv("POSTGRES_HOST")

    if os.getenv("TEST_MODE"):
        db_host = "test_db"

    db_port = os.getenv("POSTGRES_PORT")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")
    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


class Settings:
    DEBUG = os.getenv("DEBUG", default=True)
    API_ROOT = "app.api"
    API_VERSIONS = [
        "v1",
    ]
    SQLALCHEMY_DATABASE_URI = get_database_uri()


settings = Settings()
