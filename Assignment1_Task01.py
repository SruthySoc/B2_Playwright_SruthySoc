# Create a basic test that launches a browser, opens a website, and validates the page title.
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_valid():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        user_context = await browser.new_context()
        page = await user_context.new_page()
        await page.goto("https://www.facebook.com/")
        await expect(page).to_have_title("Facebook")
        print("The title is", await page.title())




