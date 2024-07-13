import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_simple():
    assert 1 + 1 == 2


# def test_simple_2():
    # expect(1).to_be(1)