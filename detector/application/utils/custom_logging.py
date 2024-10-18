from logging import DEBUG, INFO
from os import getenv

from structlog import configure, make_filtering_bound_logger


def set_up_custom_logging() -> None:
    """Setup custom logging for the application."""
    level = INFO
    if getenv("DEBUG", "false").lower() == "true":
        level = DEBUG
    configure(wrapper_class=make_filtering_bound_logger(level))
