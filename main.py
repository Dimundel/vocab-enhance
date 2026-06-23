import re
import argparse
from database import get_connection, init_db, save_words, get_words_for_practice
from fetcher import get_random_article
from llm import extract_words_from_text
from ui import (
    console,
    display_article,
    display_words,
    display_word_bank,
    display_practice_sentences,
)


def mode_fetch(conn):
    with console.status("[bold green]Searching for new article...[/bold green]"):
        source, title, text = get_random_article()
    if source:
        with console.status("[bold green]Analazying text...[/bold green]"):
            words = extract_words_from_text(text)
        display_article(source, title, text, words)
        print()
        display_words(words)

        save_words(conn, words, source)
        console.print(
            "\n[dim]Press Enter to get another one or Ctrl+C to exit...[/dim]"
        )
        input()


def mode_practice(conn):
    words_data = get_words_for_practice(conn, limit=5)

    if len(words_data) < 5:
        return

    word_bank = [row["word"] for row in words_data]
    questions = []

    for idx, row in enumerate(words_data, 1):
        target_word = row["word"]
        context = row["context"]
        synonym = row["simple_synonym"]

        pattern = rf"(?i)\b{re.escape(target_word)}\b"
        hidden_context = re.sub(pattern, f"[___] (hint: {synonym})", context)

        questions.append(
            {
                "id": idx,
                "target_word": target_word,
                "hidden_context": hidden_context,
                "definition": row["definition"],
            }
        )

    display_word_bank(word_bank)
    display_practice_sentences(questions)

    score = 0
    console.print("[dim]Type correct word for this sentence:[/dim]")

    for q in questions:
        answer = input(f"Sentence {q['id']}: ").strip()

        if answer.lower() == q["target_word"].lower():
            console.print("[bold green]Correct![/bold green]\n")
            score += 1
        else:
            console.print("[bold red]Incorrect.[/bold red]")
            console.print(
                f"Correct answer: [bold green]{q['target_word']}[/bold green]"
            )
            console.print(f"[dim]Definition: {q['definition']}[/dim]\n")

    console.print(f"[bold cyan]Your result: {score}/{len(questions)}[/bold cyan]")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--practice", action="store_true")
    args = parser.parse_args()

    conn = get_connection()
    init_db(conn)

    if args.practice:
        mode_practice(conn)
    else:
        try:
            while True:
                mode_fetch(conn)
        except KeyboardInterrupt:
            console.print("\n[yellow]Goodbye![/yellow]")
    conn.close()


if __name__ == "__main__":
    main()
