
import re
import pytest
from playwright.async_api import expect


@pytest.mark.regression
@pytest.mark.asyncio
async def test_search_box_visible(page):
    await page.goto("https://www.amazon.in/")

    search_box = page.locator("#twotabsearchtextbox")

    await expect(search_box).to_be_visible()

    print("Search box is visible")


@pytest.mark.regression
@pytest.mark.asyncio
async def test_search_functionality(page):
    await page.goto("https://www.amazon.in/")

    search_box = page.locator("#twotabsearchtextbox")
    await search_box.fill("laptop")
    await search_box.press("Enter")

    await expect(page).to_have_url(
        re.compile(r".*/s\?k=laptop.*")
    )

    print("Tested Search functionality successfully")
