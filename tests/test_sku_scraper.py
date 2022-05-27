import unittest
from unittest import TestCase

from rabbit_models.sku_scraper import Content


class TestSkuScraper(TestCase):
    def setUp(self) -> None:
        self._urls = ["https://www.americanas.com.br/produto/1706966384"]
        self._marketplace = "americanas"

    def test_model(self) -> None:
        # Create model
        content = Content(
            urls=self._urls,
            marketplace=self._marketplace,
        )

        assert content.urls == self._urls
        assert content.marketplace == self._marketplace
        assert content.metadata.created

        # Transform to JSON string
        json = content.json(exclude_none=True)
        content = Content.parse_raw(json)

        assert content.urls == self._urls
        assert content.marketplace == self._marketplace
        assert content.metadata.created

        # Transform to JSON bytes
        json = content.json(exclude_none=True).encode()
        content = Content.parse_raw(json)

        assert content.urls == self._urls
        assert content.marketplace == self._marketplace
        assert content.metadata.created


if __name__ == "__main__":
    unittest.main()
