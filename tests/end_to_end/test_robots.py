from playwright.sync_api import Page, expect
from requests import get

from .utils.variables import PROJECT_URL


def test_robots_txt(page: Page) -> None:
    """Test that the robots.txt file is valid."""
    # Act
    page.goto(f"{PROJECT_URL}/robots.txt")
    # Assert
    body = page.locator("body")
    expect(body).to_contain_text("User-agent: *")
    expect(body).to_contain_text("Allow: /")
    expect(body).to_contain_text(f"Sitemap: {PROJECT_URL}/sitemap-index.xml")


def test_robots_txt_api_request() -> None:
    """Test that the robots.txt file is valid by making an API request."""
    # Act
    response = get(f"{PROJECT_URL}/robots.txt", timeout=2)
    # Assert
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/plain; charset=utf-8"
