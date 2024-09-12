import re
import pytest
from playwright.async_api import async_playwright

SITE_URL = 'http://127.0.0.1:8000'


@pytest.mark.asyncio
async def test_add_single_item_to_cart():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless=True for background execution
        page = await browser.new_page()


        await page.goto(f"{SITE_URL}/product/")

        await page.wait_for_selector('form')


        product_id = 1
        quantity_to_add = 2
        form_selector = f'form input[name="productId"][value="{product_id}"]'
        form = await page.query_selector(form_selector)
        if form:
            parent_form = await form.evaluate_handle('element => element.closest("form")')
            print('here is the parent element')
            print(parent_form)
            quantity_input = await parent_form.query_selector('input[name="quantity"]')
            await quantity_input.fill(str(quantity_to_add))
            submit_button = await parent_form.query_selector('button[type="submit"]')
            await submit_button.click()


        await page.wait_for_selector('#cart-items')

        cart_items = await page.query_selector_all('#cart-items ul li')
        assert len(cart_items) == 1

        cart_item_text = await cart_items[0].inner_text()


        product_name = re.search(r'(.+?) - Quantity', cart_item_text).group(1).strip()
        assert product_name == 'laptop', f"Expected 'laptop', but got '{product_name}'"

        quantity = re.search(r'Quantity: (\d+)', cart_item_text).group(1)
        assert quantity == str(quantity_to_add), f"Expected quantity '{quantity_to_add}', but got '{quantity}'"


        await browser.close()

