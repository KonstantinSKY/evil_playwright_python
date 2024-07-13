import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from .utils import navigate_and_wait  # Ensure this import statement is correct

# Fixture to navigate to the page and wait for it to load
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    navigate_and_wait(page, "https://testpages.eviltester.com/styled/basic-html-form-test.html")
    yield page
    page.close()


# Test functions using the pre-loaded page fixture
def test_example_page_title(page):
    # Check if the title contains "Example Domain"
    expect(page).to_have_title(" HTML Form Elements")
    
    # title = page.locator("title")
    # assert title.text_content() == " HTML Form Elements"

def test_example_page_heading(page):
    # Check if the heading is present
    heading = page.locator("h1")
    
    expect(heading).to_have_text("Basic HTML Form Example")
    assert heading.text_content() == "Basic HTML Form Example"
    
    expect(heading).to_be_visible()
    assert heading.is_visible() == True

    if heading.count() > 0:
        print("Element is present")
    else:
        print("Element is not present")


def test_fill_username(page):
    # Fill the username field
    username_input = page.locator("input[name='username']")
    username_input.click()
    # Optional delay after clicking the field
    page.wait_for_timeout(5000)
    username_input.fill("testuser")
    page.wait_for_timeout(5000)
    # Optionally, you can add assertions here
    expect(username_input).to_have_value("testuser")

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

