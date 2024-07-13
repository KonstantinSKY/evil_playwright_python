


# Configs
MIN_LENGTH = 10
MAX_LENGTH = 60


def check_page_title(page, expected_title, min_length=MIN_LENGTH, max_length=MIN_LENGTH):
    """
    Check various properties of the page title.

    Parameters:
    page (playwright.sync_api.Page): The Playwright page object.
    expected_title (str): The expected title of the page.
    min_length (int, optional): The minimum acceptable length of the title. Defaults to MIN_LENGTH.
    max_length (int, optional): The maximum acceptable length of the title. Defaults to MAX_LENGTH.

    Raises:
    AssertionError: If any of the checks fail, an assertion error will be raised.
    """
    # Check if the title contains the expected title
    expect(page).to_have_title(expected_title)

    title = page.title()
    assert title == expected_title, f"Expected title to be '{expected_title}', but got '{title}'."
    
    # Check title length (aligned with SEO best practices)
    title_length = len(title)
    assert min_length <= title_length <= max_length, f"Expected title length to be between {min_length} and {max_length} characters, but got {title_length} characters."

    # Check for no leading or trailing whitespace
    assert title == title.strip(), f"Expected title to have no leading or trailing whitespace, but got '{title}'."
    assert title == title.rstrip(), f"Expected title to have no trailing whitespace, but got '{title}'."
    assert title == title.lstrip(), f"Expected title to have no leading whitespace, but got '{title}'."
    
    print("Title is correct, has appropriate length, and has no leading or trailing whitespace.")