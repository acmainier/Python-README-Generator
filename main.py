from rich.console import Console
from rich.panel import Panel
from questions import ask_questions
from generator import generate_readme

# Initialize Rich Console
console = Console()

# Display Styled Welcome Text
console.print(Panel.fit("[bold orchid]Welcome to my Python README file Generator![/bold orchid]"))

answers = ask_questions()

path = generate_readme(answers)

# Display Styled Sucess Text + link
console.print(Panel.fit(f"[chartreuse3]Success! Your file has been created! Click [link=file://{path}]here[/link] to open it![/chartreuse3]"))