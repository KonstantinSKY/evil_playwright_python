import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from .utils import navigate_and_wait  # Ensure this import statement is correct
from . import common


# Fixture to navigate to the page and wait for it to load
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    navigate_and_wait(
        page, "https://testpages.eviltester.com/styled/basic-web-page-test.html"
    )
    print("Navigated to the webpage.")
    yield page
    page.close()


# Test functions using the pre-loaded page fixture
def test_example_page_title(page):
    common.check_page_title(page, "Basic Web Page Title")


def test_navigation_links(page):
    print("Checking the presence of the navigation links.")
    common.check_link(page, 'div.page-navigation a[href="index.html"]', "index.html")


def test_app_navigation_links(page):
    print("Checking the presence of the app-specific navigation links.")
    # common.check_link(page, 'div.app-navigation a:has-text("Page")', "#")
    common.check_link(
        page,
        'div.app-navigation a[href="page?app=basicwebpageexample&t=About"]',
        "page?app=basicwebpageexample&t=About",
    )

def test_footer_links(page):
    common.check_link(page, 'div.page-footer a:nth-of-type(1)', 'https://eviltester.com')
    common.check_link(page, 'div.page-footer a:nth-of-type(2)', 'https://compendiumdev.co.uk')

    footer_links = page.query_selector_all('div.page-footer a')
    assert len(footer_links) == 2
    assert footer_links[0].get_attribute('href') == "https://eviltester.com"
    assert footer_links[1].get_attribute('href') == "https://compendiumdev.co.uk"


def test_example_page_heading(page):
    # Check if the heading is present
    heading = page.locator("h1")

    expect(heading).to_have_text("Basic Web Page Example")
    assert heading.text_content() == "Basic Web Page Example"

    expect(heading).to_be_visible()
    assert heading.is_visible() == True

    if heading.count() > 0:
        print("Element is present")
    else:
        print("Element is not present")

    # Locate the button
    # button = page.locator("button")

    # Method 1: Using expect
    # expect(button).to_have_text("Click Me")

    # # Check if the "More information..." link is present and visible
    # more_info_link = page.locator("a", has_text="More information...")
    # expect(more_info_link).to_be_visible()

    # # Click the "More information..." link
    # more_info_link.click()

    # Perform any additional actions or assertions as needed
