from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel


class Metadata(BaseModel):
    create: datetime = datetime.utcnow()
    query: str | None = None


class Content(BaseModel):
    urls: list[AnyHttpUrl]
    marketplace: str
    metadata: Metadata = Metadata()
