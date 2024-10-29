from structlog import get_logger, stdlib

from .utils.github_interactions import retrieve_repositories, scrape_technologies

logger: stdlib.BoundLogger = get_logger()


def generate_tech_report() -> str:
    """Generate a report on the technologies used in the repository."""
    repositories = retrieve_repositories()

    # Temporary code to test the scraper
    tech_detective = next(
        repository for repository in repositories if repository.full_name == "JackPlowman/tech-detective"
    )
    scrape_technologies(tech_detective)

    # Reimplement this
    # for repository in repositories:
    #     scrape_technologies(repository) # noqa: ERA001
