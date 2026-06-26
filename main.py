from InquirerPy import inquirer

# Get user input with Inquirer

title = inquirer.text(message="Project Title:").execute()
description = inquirer.text(message="Project description:").execute()
instructions = inquirer.text(message="Installation instructions:").execute()
usage = inquirer.text(message="Usage information:").execute()
license_type = inquirer.select(message="License", choices=["MIT", "Apache 2.0", "GPL 3.0"]).execute()
author = inquirer.text(message="Author name:").execute()
contact = inquirer.text(message="Contact information:").execute()

print(title, description, instructions, usage, license_type, author, contact)