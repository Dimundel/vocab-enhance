# ⛏️ WordMiner

**WordMiner** is an AI-powered CLI application that helps advanced English (also German in future) learners discover, learn, and retain C1-C2 vocabulary from authentic articles.

Instead of relying on predefined word lists, WordMiner automatically mines sophisticated vocabulary from high-quality publications using LLM, stores each word together with its context, and helps users remember it through a Spaced Repetition System.

---

## ✨ Features

- 📚 **Automated Mining**
  - Fetches random long-form articles from high-quality sources such as BBC News, The Guardian, Aeon, and Nautilus.

- 🤖 **AI-Powered Extraction**
  - Uses LLM to identify advanced vocabulary.

- 💬 **Contextual Learning**
  - Stores every word together with:
    - its original sentence,
    - a concise definition,
    - an easy synonym used as a learning hint.

- 🧠 **Spaced Repetition**
  - Reviews vocabulary using a Spaced Repetition System.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/wordminer.git
cd wordminer
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Create a `.env` file

```text
GOOGLE_API_KEY=your_api_key
```

---

## 🚀 Usage

Mine new vocabulary:

```bash
uv run main.py
```

Practice learned words:

```bash
uv run main.py --practice
```

---

## 🏗️ Future Improvements

- German language support
- Word graph
- Support multiple LLM providers
- Learning statistics dashboard
- Additional article sources

---

## 📄 License

This project is licensed under the MIT License.
