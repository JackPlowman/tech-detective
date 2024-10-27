from playwright.sync_api import Page, expect

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
