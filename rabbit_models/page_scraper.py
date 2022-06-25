from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, constr, validator


class Metadata(BaseModel):
    """
    created - When the message was created
    query - The query which the SKU came from
    attempts - How many times the message have been requeued
    source - Who started this pipeline
    """

    created: datetime = datetime.utcnow()
    query: constr(strip_whitespace=True, min_length=1) | None = None
    attempts: int = 0
    source: constr(strip_whitespace=True, to_lower=True, min_length=1)


class Body(BaseModel):
    """
    urls - List of urls needed to be visited to obtain a SKU
    marketplace - Marketplace configuration to use
    metadata - Data about this message
    """

    urls: list[AnyHttpUrl]
    marketplace: constr(strip_whitespace=True, to_lower=True, min_length=1)
    metadata: Metadata

    _urls = validator("urls", each_item=True, allow_reuse=True)(lambda u: str(u))
