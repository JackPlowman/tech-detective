from json import dump
from pathlib import Path

from .types import ProjectTechnologiesAndFrameworks


def generate_output_file(project_technologies_and_frameworks: list[ProjectTechnologiesAndFrameworks]) -> None:
    """Generate the output jsonfile.

    Args:
        project_technologies_and_frameworks (list[ProjectTechnologiesAndFrameworks]):
            The list of project technologies and frameworks.
    """
    file_content = {"repositories": project_technologies_and_frameworks}
    with Path.open("../project_technologies_and_frameworks.json", "w") as output_file:
        dump(file_content, output_file)
