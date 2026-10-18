# Create a basic test that launches a browser, opens a website, and validates the page title.
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_valid(async_page):
    await async_page.goto("https://www.facebook.com/")
    await expect(async_page).to_have_title("Facebook")
    print("The title is", await async_page.title())


