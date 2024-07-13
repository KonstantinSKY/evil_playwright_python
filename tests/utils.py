# tests/utils.py
import pytest

def navigate_and_wait(page, url, timeout=10000):
    try:
        page.goto(url, timeout=timeout)
        page.wait_for_load_state("networkidle", timeout=timeout)
        print(f"Page {url} loaded successfully.")
    except TimeoutError as e:
        print(f"Page loading timed out: {e}")
        pytest.fail(f"Test failed due to timeout: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        pytest.fail(f"Test failed due to an unexpected error: {e}")