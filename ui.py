import re
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def display_article(source, title, full_text, highlight_words):
    header = Text(f"\nSource: {source}", style="italic cyan")
    title_text = Text(title, style="bold magenta")
    body = Text(f"\n{full_text}", style="white")

    if highlight_words:
        for row in highlight_words:
            word = row["word"]
            word = word.strip().strip(".,!?:;")
            if not word:
                continue
            pattern = rf"\b{re.escape(word)}\b"
            body.highlight_regex(pattern, style="bold yellow underline")

    panel = Panel(
        Text.assemble(title_text, body),
        title="[bold yellow]English Passage[/bold yellow]",
        subtitle=header,
        padding=(1, 2),
        width=80,
    )

    console.print(panel)
