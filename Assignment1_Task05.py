
# tests/test_browser_suite.py

import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_login(page):
    await page.goto("https://www.saucedemo.com/")

    await page.locator("#user-name").fill("standard_user")
    await page.locator("#password").fill("secret_sauce")
    await page.locator("#login-button").click()

    await expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    print("Login test passed")


@pytest.mark.asyncio
async def test_search(chromium_page):
    await chromium_page.goto("https://duckduckgo.com/")

    search_box = chromium_page.locator('input[name="q"]')
    await search_box.fill("Playwright Python")
    await search_box.press("Enter")

    await expect(chromium_page).to_have_title(
        __import__("re").compile("Playwright Python", __import__("re").I)
    )

    print("Search test passed")


@pytest.mark.asyncio
async def test_navigation(firefox_page):
    await firefox_page.goto("https://www.selenium.dev/")

    await expect(firefox_page).to_have_title(
        __import__("re").compile("Selenium", __import__("re").I)
    )

    print("Navigation test passed")


@pytest.mark.asyncio
async def test_form_validation(webkit_page):
    await webkit_page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    text_input = webkit_page.locator('input[name="my-text"]')
    await expect(text_input).to_be_visible()

    await text_input.fill("Pytest browser test")
    await expect(text_input).to_have_value("Pytest browser test")

    print("Form validation test passed")
