import feedparser
import random
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client()

SOURCES = {
    "Aeon": "https://aeon.co/feed.rss",
    "The Guardian": "https://www.theguardian.com/news/series/the-long-read/rss",
    "Wired": "https://www.wired.com/feed/rss",
}

console = Console()


def get_random_article():
    source_name = random.choice(list(SOURCES.keys()))
    url = SOURCES[source_name]

    with console.status(f"[bold green]Fetching from {source_name}..."):
        feed = feedparser.parse(url)

    if not feed.entries:
        return None, None, None

    article = random.choice(feed.entries[:10])
    return source_name, article.title, article.summary


def display_article(source, title, summary):
    import re

    clean_text = re.sub("<[^<]+?>", "", summary)
    header = Text(f"\nSource: {source}", style="italic cyan")
    title_text = Text(title, style="bold magenta")
    body = Text(f"\n{clean_text}", style="white")

    panel = Panel(
        Text.assemble(title_text, body),
        title="[bold yellow]English Passage[/bold yellow]",
        subtitle=header,
        padding=(1, 2),
        width=80,
    )

    console.print(panel)


def main():
    console.clear()
    console.print("[bold blue]Test[/bold blue]\n")
    source, title, summary = get_random_article()

    if source:
        display_article(source, title, summary)
        console.print(
            "\n[dim]Press Enter to get another one or Ctrl+C to exit...[/dim]"
        )
        input()
    else:
        console.print("\n[red]Failed to fetch articles. Check your internet.[/red]")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        console.print("\nGoodbye!")
    response = client.models.generate_content(
        model="gemini-flash-lite-latest", contents="Hello! Are you here?"
    )
    print(response.text)
