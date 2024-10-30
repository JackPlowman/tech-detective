from json import dump
from pathlib import Path


def generate_output_file(project_technologies_and_frameworks: list[str]) -> None:
    """Generate the output jsonfile."""
    file_format = {
        "repositories": [
            {
                "full_name": "JackPlowman/tech-detective",
                "project_technologies_and_frameworks": project_technologies_and_frameworks,
            }
        ]
    }
    with Path.open("../project_technologies_and_frameworks.json", "w") as output_file:
        dump(file_format, output_file)
