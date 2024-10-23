from structlog import get_logger, stdlib

from .utils.github_interactions import retrieve_repositories

logger: stdlib.BoundLogger = get_logger()


def generate_tech_report() -> str:
    """Generate a report on the technologies used in the repository."""
    return retrieve_repositories()
