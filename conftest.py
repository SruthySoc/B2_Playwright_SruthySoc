import pytest
import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture
async def browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        yield browser
        await browser.close()


@pytest_asyncio.fixture
async def context(browser):
    context = await browser.new_context()
    yield context
    await context.close()


@pytest_asyncio.fixture
async def page(context):
    page = await context.new_page()
    yield page
    await page.close()





@pytest_asyncio.fixture()
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()

@pytest_asyncio.fixture()
async def chromium_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

@pytest_asyncio.fixture()
async def firefox_page():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

@pytest_asyncio.fixture()
async def webkit_page():
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()