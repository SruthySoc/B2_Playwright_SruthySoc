import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, expect
from Utils import config

@pytest.mark.asyncio
async def test_website_configuration(page):
    # Read the URL from config.py
    await page.goto(config.BASE_URL)

    # Print configuration and execution details
    print("Browser:", config.BROWSER_NAME)
    print("Headless mode:", config.HEADLESS)
    print("Default timeout:", config.DEFAULT_TIMEOUT)
    print("Navigation timeout:", config.NAVIGATION_TIMEOUT)
    print("Current URL:", page.url)
    print("Page title:", await page.title())

    # Verify that navigation completed with a title
    await expect(page).to_have_title("Online Shopping India Mobile, Cameras, Lifestyle & more Online @ Flipkart.com")

