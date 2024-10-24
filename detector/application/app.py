from structlog import get_logger, stdlib

from .utils.github_interactions import retrieve_repositories, scrape_technologies

logger: stdlib.BoundLogger = get_logger()


def generate_tech_report() -> str:
    """Generate a report on the technologies used in the repository."""
    repositories = retrieve_repositories()
    for repository in repositories:
        scrape_technologies(repository)
