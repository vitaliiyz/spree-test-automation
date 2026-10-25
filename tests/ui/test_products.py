import math
import re

from playwright.sync_api import expect

from pages.products_page import ProductsPage

PRODUCTS_PER_BATCH = 12


def test_product_cards_display_required_details(opened_products_page: ProductsPage) -> None:
    """
    Test to verify that products cards are displayed and contain required details.
    """

    expect(opened_products_page.product_cards).to_be_visible()

    product_count = opened_products_page.load_all_products()

    # Verify every product has image, name and price
    for i in range(product_count):
        product = opened_products_page.products.nth(i)

        image = product.get_by_role("img")
        name = product.get_by_role("heading")
        price = product.locator("span:not(.line-through)").filter(has_text="$")

        image.scroll_into_view_if_needed()
        expect(image).to_be_visible()
        expect(image).to_have_js_property("complete", True)
        expect(image).not_to_have_js_property("naturalWidth", 0)

        expect(name).to_be_visible()
        expect(name).to_have_text(re.compile(r"\S"))

        expect(price).to_be_visible()
        expect(price).to_have_text(re.compile(r"^\$[0-9]{1,3}(?:,[0-9]{3})*\.[0-9]{2}$"))


def test_products_infinite_scroll(opened_products_page: ProductsPage):
    product_count_in_span = opened_products_page.get_product_count_in_span()

    # Count of loaded pages with products
    batches_count = math.ceil(product_count_in_span / PRODUCTS_PER_BATCH)

    # Verify every loading has necessary count of products
    for i in range(1, batches_count + 1):
        if i != batches_count:
            expect(opened_products_page.products).to_have_count(i * PRODUCTS_PER_BATCH)
            opened_products_page.products.last.scroll_into_view_if_needed()
        else:
            expect(opened_products_page.products).to_have_count(product_count_in_span)
            expect(opened_products_page.no_more_products_text).to_be_visible()
