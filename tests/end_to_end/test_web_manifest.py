from requests import get

from .utils.variables import PROJECT_URL


def test_web_manifest() -> None:
    """Test that the web manifest file is valid."""
    # Act
    response = get(f"{PROJECT_URL}/manifest.webmanifest", timeout=2)
    # Assert
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/manifest+json; charset=utf-8"
    web_manifest = response.json()
    assert web_manifest["name"] == "Tech Detective"
    assert web_manifest["description"] == "What Technologies are used in my projects?"
    assert web_manifest["start_url"] == "/tech-detective"
