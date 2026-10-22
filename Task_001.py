import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_valid(async_page):
    await async_page.goto("https://www.amazon.in/")
    await expect(async_page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    title = await async_page.title()
    print("Page title is ",title)
    # logo = async_page.locator('//*[@id="nav-logo-sprites"]')
    # await expect(logo).to_be_visible()
    print("Test completed")
