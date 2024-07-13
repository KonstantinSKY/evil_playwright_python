# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


    # Helper function for navigation and waiting
def navigate_and_wait(page, url, timeout=10000):
    try:
        page.goto(url, timeout=timeout)  # Set a timeout for page navigation
        page.wait_for_load_state("networkidle", timeout=timeout)  # Set a timeout for load state
        print(f"Page {url} loaded successfully.")
    except TimeoutError as e:
        print(f"Page loading timed out: {e}")
        pytest.fail(f"Test failed due to timeout: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        pytest.fail(f"Test failed due to an unexpected error: {e}")