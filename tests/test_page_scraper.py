import unittest
from unittest import TestCase

from rabbit_models.page_scraper import Body, Metadata


class TestPageScraper(TestCase):
    def setUp(self) -> None:
        self._urls = ["https://www.americanas.com.br/produto/1706966384"]
        self._marketplace = "americanas"
        self._source = "test"

    def test_model(self) -> None:
        # Create model
        body = Body(
            urls=self._urls,
            marketplace=self._marketplace,
            metadata=Metadata(source=self._source),
        )

        assert body.urls == self._urls
        assert body.marketplace == self._marketplace
        assert body.metadata.created

        # Transform to JSON string
        json = body.json(exclude_none=True)
        body = Body.parse_raw(json)

        assert body.urls == self._urls
        assert body.marketplace == self._marketplace
        assert body.metadata.created

        # Transform to JSON bytes
        json = body.json(exclude_none=True).encode()
        body = Body.parse_raw(json)

        assert body.urls == self._urls
        assert body.marketplace == self._marketplace
        assert body.metadata.created


if __name__ == "__main__":
    unittest.main()
