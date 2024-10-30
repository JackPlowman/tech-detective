from unittest.mock import MagicMock, patch

from detector.application.app import generate_tech_report

FILE_PATH = "detector.application.app"


@patch(f"{FILE_PATH}.generate_output_file")
@patch(f"{FILE_PATH}.scrape_technologies")
@patch(f"{FILE_PATH}.retrieve_repositories")
def test_generate_tech_report(
    mock_retrieve_repositories: MagicMock, mock_scrape_technologies: MagicMock, mock_generate_output_file: MagicMock
) -> None:
    # Arrange
    tech_detective = MagicMock(full_name="JackPlowman/tech-detective")
    mock_retrieve_repositories.return_value = [tech_detective]
    # Act
    generate_tech_report()
    # Assert
    mock_retrieve_repositories.assert_called_once_with()
    mock_scrape_technologies.assert_called_once_with(tech_detective)
    mock_generate_output_file.assert_called_once_with(mock_scrape_technologies.return_value)
