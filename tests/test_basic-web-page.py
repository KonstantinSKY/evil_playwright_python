import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from .utils import navigate_and_wait  # Ensure this import statement is correct

# Fixture to navigate to the page and wait for it to load
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    navigate_and_wait(page, "https://testpages.eviltester.com/styled/basic-web-page-test.html")
    print("Navigated to the webpage.")
    yield page
    page.close()


# Test functions using the pre-loaded page fixture
def test_example_page_title(page):
    # Check if the title contains "Example Domain"
    expect(page).to_have_title("Basic Web Page Title")

    title = page.title()
    assert title == "Basic Web Page Title", "Expected title to be 'Basic Web Page Title'."
 
   # Check title length (aligned with SEO best practices)
    min_length = 10
    max_length = 60
    title_length = len(title())
    assert min_length <= title_length <= max_length, f"Expected title length to be between {min_length} and {max_length} characters, but got {title_length} characters."

    # Check for no leading or trailing whitespace
    # assert title == title.strip(), f"Expected title to have no leading or trailing whitespace, but got '{title}'."
    assert title == title.rstrip(), f"Expected title to have no trailing whitespace, but got '{title}'."
    assert title == title.lstrip(), f"Expected title to have no leading whitespace, but got '{title}'."
    


def test_navigation_links(page):
    print("Checking the presence of the navigation links.")
    try:
        # Locate the link
        index_link_query = page.query_selector('div.page-navigation a[href="index.html"]')
        index_link_locator = page.locator('div.page-navigation a[href="index.html"]')
        # Assert that the link is found
        assert index_link_query is not None, "Expected to find the index navigation link."
        assert index_link_query, "Expected to find the index navigation link."
        print("Index_link:", index_link_query)

        assert index_link_locator.count() > 0, "Expected to find the index navigation link."
        # # Check if the link has the correct href attribute
        link_href = index_link_locator.get_attribute('href')
        assert link_href == "index.html", f"Expected link href to be 'index.html', but got '{link_href}'."

        assert index_link_locator.is_visible(), "Expected the index navigation link to be visible."
        assert index_link_query.is_enabled(), "Expected the index navigation link to be enabled."


        print("Navigation link is correct.")
    except AssertionError as e:
        raise AssertionError(f"Navigation link error: {str(e)}")

def test_app_navigation_links(page):
    print("Checking the presence of the app-specific navigation links.")
    try:
        page_link = page.query_selector('div.app-navigation a:has-text("Page")')
        about_link = page.query_selector('div.app-navigation a[href="page?app=basicwebpageexample&t=About"]')
        assert page_link is not None, "Expected to find the page link."
        assert about_link is not None, "Expected to find the about link."
    
    
        page_link_href = page_link.get_attribute('href')
        about_link_href = about_link.get_attribute('href')
        
        # assert page_link_href is not None, "Expected to find the href attribute for the page link."
        assert about_link_href is not None, "Expected to find the href attribute for the about link."

    except AssertionError as e:
        raise AssertionError(f"App navigation link error: {str(e)}")  

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

