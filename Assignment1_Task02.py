
# Create a test that navigates to a website using the page fixture.

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_navigate_to_website(async_page):
    # Navigate to the website
    await async_page.goto("https://www.flipkart.com/")

    # Verify the page title
    await expect(async_page).to_have_title("Online Shopping India Mobile, Cameras, Lifestyle & more Online @ Flipkart.com")

    # Print the current URL
    print("Current URL:", async_page.url)

