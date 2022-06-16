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
    url - URL to visited in order to obtain SKUs
    marketplace - Marketplace configuration to use
    metadata - Data about this message
    """

    url: AnyHttpUrl
    marketplace: str
    metadata: Metadata = Metadata()
