from __future__ import annotations

from os import getenv

from github import Github, PaginatedList, Repository
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
