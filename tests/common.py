from playwright.sync_api import Playwright, sync_playwright, expect


# Configs
MIN_LENGTH = 10
MAX_LENGTH = 60


def check_page_title(page, expected, min_length=MIN_LENGTH, max_length=MAX_LENGTH):
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
    expect(page).to_have_title(expected)

    title = page.title()
    assert title == expected, f"Expected title to be '{expected}', but got '{title}'."

    # Check title length (aligned with SEO best practices)
    title_length = len(title)
    assert (
        min_length <= title_length <= max_length
    ), f"Expected title length to be between {min_length} and {max_length} characters, but got {title_length} characters."

    # Check for no leading or trailing whitespace
    assert (
        title == title.strip()
    ), f"Expected title to have no leading or trailing whitespace, but got '{title}'."
    assert (
        title == title.rstrip()
    ), f"Expected title to have no trailing whitespace, but got '{title}'."
    assert (
        title == title.lstrip()
    ), f"Expected title to have no leading whitespace, but got '{title}'."

    print(
        "Title is correct, has appropriate length, and has no leading or trailing whitespace."
    )


def check_link(page, link_selector: str, expected_href: str):
    """
    Check the presence, visibility, and href attribute of a navigation link.

    Parameters:
    page (Page): The Playwright page object.
    link_selector (str): The CSS selector for the link.
    expected_href (str): The expected href attribute of the link.

    Raises:
    AssertionError: If any of the checks fail.
    """
    print("Checking the presence of the navigation link.")

    link_query = page.query_selector(link_selector)
    link_locator = page.locator(link_selector)

    # Assert that the link is found
    assert (
        link_query is not None
    ), f"Expected to find the navigation link using query_selector."
    assert (
        link_locator.count() > 0
    ), f"Expected to find the navigation link using locator."

    # Check if the link has the correct href attribute
    expect(link_locator).to_have_attribute("href", expected_href)
    link_href = link_locator.get_attribute("href")
    assert (
        link_href == expected_href
    ), f"Expected link href to be '{expected_href}', but got '{link_href}'."

    # Check if the link is visible
    expect(link_locator).to_be_visible()

    # Check if the link is enabled (interactable)
    assert link_query.is_enabled(), "Expected the navigation link to be enabled."

    print("Navigation link is correct, visible, and has the correct href attribute.")
