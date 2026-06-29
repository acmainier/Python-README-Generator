import os

# Format input in Markdown

def generate_readme(answers):
        content = f"""# {answers["title"]}

## Description:

{answers["description"]}

---

## Installation instructions:

```
{answers["instructions"]}
```

---

## Usage information:

{answers["usage"]}

---

## License:

{answers["license"]}

---

## Author name:

{answers["author"]}

---

## Contact information:

{answers["contact"]}"""

# Creation of README.md + addition of input

        with open("GENERATED_README.md", "w") as file:
            file.write(content)

# Creation of README.md file path

        path = os.path.abspath("GENERATED_README.md")
        return path
