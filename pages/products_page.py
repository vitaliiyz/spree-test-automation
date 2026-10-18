from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Products page object for handling products catalog."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._path = "/products"

        self.product_cards: Locator = self.page.locator("div.grid").filter(
            has=self.page.locator("h3 a")
        )
        self.product: Locator = self.product_cards.locator("xpath=/div")
        self.products_count_span: Locator = self.page.locator("span").filter(has_text="products")
        self.no_more_products_text: Locator = self.page.get_by_text(
            "No more products to load", exact=True
        )

    def get_product_count_in_span(self):
        products_count_in_span = self.products_count_span.inner_text().split(" ")
        return int(products_count_in_span[0])
