from __future__ import annotations

from os import getenv

from github import Github, GithubException, PaginatedList, Repository
from structlog import get_logger, stdlib

logger: stdlib.BoundLogger = get_logger()


def retrieve_repositories() -> PaginatedList[Repository]:
    """Retrieve the list of repositories to analyse.

    Returns:
        PaginatedList[Repository]: The list of repositories.
    """
    github = Github()
    repository_owner = getenv("GITHUB_REPOSITORY_OWNER")
    repositories = github.search_repositories(query=f"user:{repository_owner} archived:false")
    logger.info(
        "Retrieved repositories to analyse",
        repositories_count=repositories.totalCount,
        repositories=[repository.full_name for repository in repositories],
    )
    return repositories


def scrape_technologies(repository: Repository) -> list[str]:
    """Scrape the technologies used in a repository.

    Args:
        repository (Repository): The repository to scrape.

    Returns:
        list[str]: The list of technologies used in the repository.
    """
    expected_files = [
        "README.md",
        "Readme.md",
        "readme.md",
    ]  # Ordered in most common to least common
    found_file = False
    for expected_file in expected_files:
        try:
            file = repository.get_contents(expected_file)
            logger.debug("Found file", file=file.name, repository=repository.full_name)
            found_file = True
            break
        except GithubException:
            logger.debug("No file found", repository=repository.full_name)
    if not found_file:
        logger.debug("No Readme files found", repository=repository.full_name)
        return []
    return []
