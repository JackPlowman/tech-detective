from unittest.mock import MagicMock, patch

from detector.application.app import generate_tech_report

FILE_PATH = "detector.application.app"


@patch(f"{FILE_PATH}.scrape_technologies")
@patch(f"{FILE_PATH}.retrieve_repositories")
def test_generate_tech_report(mock_retrieve_repositories: MagicMock, mock_scrape_technologies: MagicMock) -> None:
    # Arrange
    mock_retrieve_repositories.return_value = ["test"]
    # Act
    generate_tech_report()
    # Assert
    mock_retrieve_repositories.assert_called_once_with()
    mock_scrape_technologies.assert_called_once_with("test")
