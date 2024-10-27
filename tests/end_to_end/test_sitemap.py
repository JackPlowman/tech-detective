from defusedxml.ElementTree import fromstring
from requests import get

from .utils.variables import PROJECT_URL


def test_sitemap_index_xml() -> None:
    """Test that the sitemap index file is valid."""
    # Act
    response = get(f"{PROJECT_URL}/sitemap-index.xml", timeout=2)
    # Assert
    sitemap_index_element = fromstring(response.content)
    assert sitemap_index_element.tag == "{http://www.sitemaps.org/schemas/sitemap/0.9}sitemapindex"
    sitemap_element = sitemap_index_element.find("{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap")
    loc_element = sitemap_element.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
    assert loc_element == f"{PROJECT_URL}/sitemap-0.xml"


def test_sitemap_0_xml() -> None:
    """Test that the sitemap file is valid."""
    # Act
    response = get(f"{PROJECT_URL}/sitemap-0.xml", timeout=2)
    # Assert
    sitemap_element = fromstring(response.content)
    assert sitemap_element.tag == "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset"
    # Check that the sitemap contains the expected number of URLs
