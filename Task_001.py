import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_valid(async_page):
    await async_page.goto("https://www.amazon.in/")
    expect(async_page).to_have_title("Amazon")
    print(await async_page.title())
    logo = async_page.locator('//*[@id="nav-logo-sprites"]')
    await expect(logo).to_be_visible()
