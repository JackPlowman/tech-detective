from structlog import get_logger, stdlib

from .utils.github_interactions import retrieve_repositories, scrape_technologies
from .utils.output_file import generate_output_file

logger: stdlib.BoundLogger = get_logger()


def generate_tech_report() -> None:
    """Generate a report on the technologies used in the repository."""
    repositories = retrieve_repositories()
    technologies_and_frameworks = [scrape_technologies(repository) for repository in repositories]
    generate_output_file(technologies_and_frameworks)
