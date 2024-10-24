from unittest.mock import MagicMock, call, patch

from detector.application.utils.github_interactions import retrieve_repositories

FILE_PATH = "detector.application.utils.github_interactions"


@patch(f"{FILE_PATH}.Github")
@patch(f"{FILE_PATH}.getenv")
def test_retrieve_repositories(mock_getenv: MagicMock, mock_github: MagicMock) -> None:
    # Arrange
    token = "TestToken"  # noqa: S105
    mock_getenv.side_effect = [token, "Test"]
    full_name = "Test3/Test4"
    mock_github.return_value.search_repositories.return_value = search_return = MagicMock(
        totalCount=1, list=[MagicMock(full_name=full_name)]
    )
    # Act
    repositories = retrieve_repositories()
    # Assert
    mock_github.assert_called_once_with()
    mock_getenv.assert_has_calls([call("GITHUB_REPOSITORY_OWNER")])
    assert repositories == search_return
    # Cleanup
