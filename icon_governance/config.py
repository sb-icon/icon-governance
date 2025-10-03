from __future__ import annotations

import os
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NAME: str = "governance"
    VERSION: str = "v0.10.7"  # x-release-please-version

    NETWORK_NAME: str = "mainnet"

    # Ports
    PORT: int = 8000
    HEALTH_PORT: int = 8180
    METRICS_PORT: int = 9400

    METRICS_ADDRESS: str = "localhost"

    # Prefix
    REST_PREFIX: str = "/api/v1"
    HEALTH_PREFIX: str = "/heath"
    METRICS_PREFIX: str = "/metrics"
    DOCS_PREFIX: str = "/api/v1/governance/docs"

    CORS_ALLOW_ORIGINS: str = "*"
    CORS_ALLOW_CREDENTIALS: bool = False
    CORS_ALLOW_METHODS: str = "GET,POST,HEAD,OPTIONS"
    CORS_ALLOW_HEADERS: str = ""
    CORS_EXPOSE_HEADERS: str = "x-total-count"

    # Monitoring
    HEALTH_POLLING_INTERVAL: int = 60

    # ICON Nodes
    ICON_NODE_URL: str = "https://api.icon.community/api/v3"
    BACKUP_ICON_NODE_URL: str = "https://ctz.solidwallet.io/api/v3"

    # API endpoints
    COMMUNITY_API_ENDPOINT: str = "https://tracker.icon.community"

    # Logs service - For getting value for iscore
    # TODO: Replace this when stateful processing comes in maybe
    LOGS_SERVICE_URL: str = "https://tracker.icon.community"

    # Kafka
    KAFKA_BROKER_URL: str = "localhost:29092"
    SCHEMA_REGISTRY_URL: str = "http://localhost:8081"
    CONSUMER_IS_TAIL: bool = False

    # Topics
    CONSUMER_GROUP: str = "governance"
    CONSUMER_TOPIC_BLOCKS: str = "blocks"
    # Backfilling
    CONSUMER_AUTO_OFFSET_RESET: str = "earliest"
    JOB_ID: Optional[str] = None

    # DB
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "changeme"
    POSTGRES_SERVER: str = "127.0.0.1"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DATABASE: str = "postgres"

    # Endpoints
    MAX_PAGE_SIZE: int = 100

    governance_address: str = "cx0000000000000000000000000000000000000000"
    CRON_SLEEP_SEC: int = 600

    apy_start_block: int = 44000000

    model_config = SettingsConfigDict(
        extra="ignore",
    )


TEST_ENV = os.path.join(os.path.dirname(__file__), "..", ".env.test")

if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
elif os.path.exists(TEST_ENV):
    settings = Settings(_env_file=TEST_ENV)
else:
    settings = Settings()
