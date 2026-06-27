from InquirerPy import inquirer

# Get user input with Inquirer and in a class
class Questions:
    def ask(self):
        self.title = inquirer.text(message="Project Title:").execute()
        self.description = inquirer.text(message="Project description:", multiline=True).execute()
        self.instructions = inquirer.text(message="Installation instructions:", multiline=True).execute()
        self.usage = inquirer.text(message="Usage information:").execute()
        self.license_type = inquirer.select(message="License", choices=["MIT", "Apache 2.0", "GPL 3.0"]).execute()
        self.author = inquirer.text(message="Author name:").execute()
        self.contact = inquirer.text(message="Contact information:").execute()

        return self

    # Changing class attributes to dictionary
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "instructions": self.instructions,
            "usage": self.usage,
            "license": self.license_type,
            "author": self.author,
            "contact": self.contact
    }
