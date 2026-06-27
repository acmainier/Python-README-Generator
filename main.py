from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
import os

# Initialize Rich Console
console = Console()

# 1. Display Styled Text
console.print(Panel.fit("[bold orchid]Welcome to my Python README file Generator![/bold orchid]"))


# Get user input with Inquirer

title = inquirer.text(message="Project Title:").execute()
description = inquirer.text(message="Project description:").execute()
instructions = inquirer.text(message="Installation instructions:").execute()
usage = inquirer.text(message="Usage information:").execute()
license_type = inquirer.select(message="License", choices=["MIT", "Apache 2.0", "GPL 3.0"]).execute()
author = inquirer.text(message="Author name:").execute()
contact = inquirer.text(message="Contact information:").execute()

# Format input in Markdown

content = f"""# {title}

## Description:
{description}

## Installation instructions:
{instructions}

## Usage information:
{usage}

## License:
{license_type}

## Author name:
{author}

## Contact information:
{contact}"""

# Creation of README.md + addition of input

with open("README.md", "w") as file:
        file.write(content)

path = os.path.abspath("README.md")

console.print(Panel.fit(f"[chartreuse3]Success! Your file has been created! Click [link=file://{path}]here[/link] to open it![/chartreuse3]"))