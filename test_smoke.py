import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_valid(async_page):
    await async_page.goto("https://www.amazon.in/")
    await expect(async_page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    title = await async_page.title()
    print("Page title is ",title)
    logo = async_page.locator('//*[@id="nav-logo-sprites"]')
    await expect(logo).to_be_visible()
    print("Test completed")

#
# @pytest.mark.smoke
# @pytest.mark.asyncio
# async def test_homepage_url(page):
#     await page.goto("https://www.amazon.in/")
#
#     print("Current URL:", page.url)
#
#     await expect(page).to_have_url(
#         re.compile(r"https://www\.amazon\.in/.*")
#     )





# import re
# import pytest
# from playwright.async_api import expect
#
#
# @pytest.mark.smoke
# @pytest.mark.asyncio
# async def test_homepage_title(page):
#     await page.goto("https://www.amazon.in/")
#
#     title = await page.title()
#     print("Homepage title:", title)
#
#     await expect(page).to_have_title(re.compile("Amazon"))
#
#

