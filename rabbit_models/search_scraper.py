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
    url - URL to visited in order to obtain SKUs
    marketplace - Marketplace configuration to use
    metadata - Data about this message
    """

    url: AnyHttpUrl
    marketplace: constr(strip_whitespace=True, to_lower=True, min_length=1)
    metadata: Metadata

    _urls = validator("url")(lambda u: str(u))
