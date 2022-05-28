from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel


class Metadata(BaseModel):
    """
    created - When the message was created
    query - The query which the SKU came from
    attempts - How many times the message have been requeued
    source - Who started this pipeline
    """

    created: datetime = datetime.utcnow()
    query: str | None = None
    attempts: int | None = None
    source: str | None = None


class Body(BaseModel):
    """
    urls - List of urls needed to be visited to obtain a SKU
    marketplace - Marketplace configuration to use
    metadata - Data about this message
    """

    urls: list[AnyHttpUrl]
    marketplace: str
    metadata: Metadata = Metadata()
