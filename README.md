# Asista AI — Chatbot with Streamlit

Asista AI is a multi-turn chatbot that keeps conversation history and uses a single backend for both a **CLI** (command-line) and a **Streamlit** web interface. The backend uses LangChain’s unified chat model API with Mistral’s `mistral-small-2506` model to generate responses.

---

## Features

- **Multi-turn conversation** — Full chat history is sent to the model for context-aware replies.
- **Dual interfaces** — Use the same logic via terminal (CLI) or Streamlit web app.
- **Separated frontend and backend** — Chat logic lives in `chatbot_app.py`; Streamlit only handles UI and calls `get_response()`.
- **Session-based UI** — Streamlit keeps messages in session state so the conversation persists while the app is open.
- **Simple configuration** — Model and API key are configured via environment variables (e.g. `.env`).

---

## Project Structure

This repository contains only the files needed to run the chatbot:

```
genai/
├── README.md
├── requirements.txt
├── .env                    # Not in repo — you create this with your API key
├── chatbot_app.py      # Backend: model init + get_response(); runnable as CLI
├── streamlit_app.py    # Streamlit frontend (imports chatbot_app)
└── screenrecording     # sample run
```

- **`chatbot_app.py`** — Backend: initializes the Mistral model and exposes `get_response(messages)`. Can be run as a CLI with `python chatmodel/chatbot_app.py` (type `0` to exit).
- **`streamlit_app.py`** — Streamlit UI only; imports `get_response` from `chatbot_app` and manages chat display and input.

---

## Prerequisites

- **Python** 3.10 or 3.11 (recommended).
- **Mistral API key** — Get one at [Mistral AI](https://www.mistral.ai/) (sign up / API section).
- A terminal and (for the web app) a browser.

---

## Installation

1. **Clone the repository** (or download the project):

   ```bash
   git clone <your-repo-url>
   cd genai
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   The app uses (among others) `langchain`, `langchain-mistralai`, `streamlit`, and `python-dotenv`. The full list is in `requirements.txt`.

---

## Configuration

1. **Create a `.env` file** in the project root (same folder as `requirements.txt`):

   ```bash
   touch .env
   ```

2. **Add your Mistral API key**:

   ```env
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

   The exact variable name may depend on what `langchain-mistralai` expects (often `MISTRAL_API_KEY`). Check [LangChain Mistral docs](https://python.langchain.com/docs/integrations/chat/mistral) if needed.

3. **Do not commit `.env`** — Add `.env` to `.gitignore` so your key is never pushed to GitHub.

---

## Usage

### Option 1: Streamlit (web UI)

From the **project root** (`genai/`):

```bash
streamlit run chatmodel/streamlit_app.py
```

Your browser will open the Asista AI chat interface. Type in the input box and press Enter to get replies. Conversation is kept in session state until you refresh or close the tab.

### Option 2: CLI (terminal)

From the project root:

```bash
python chatmodel/chatbot_app.py
```

Type your messages and press Enter. Type `0` and Enter to exit.

---

## Architecture

- **Backend (`chatbot_app.py`):**
  - Loads environment variables and initializes the Mistral chat model once at import time.
  - Exposes `get_response(messages: list) -> str`, which calls `model.invoke(messages)` and returns the assistant’s text. The `messages` list is the same format used in the original design (alternating user/assistant strings).

- **Frontend (`streamlit_app.py`):**
  - Imports `get_response` from `chatbot_app`.
  - Uses `st.session_state.messages` to store the conversation list.
  - Renders each message with `st.chat_message` and `st.write`, and uses `st.chat_input` for new user input. On submit, it appends the user message, calls `get_response(st.session_state.messages)`, then appends the assistant reply and re-renders.

- **Single process:** Running the Streamlit app is enough; the chatbot runs inside the same process via the import. No need to start `chatbot_app.py` separately.

---

## Tech Stack

| Layer        | Technology |
|-------------|------------|
| **LLM**     | Mistral (`mistral-small-2506`) via Mistral AI API |
| **Orchestration** | LangChain (`init_chat_model`, `model_provider="mistralai"`) |
| **Frontend**| Streamlit (chat UI, session state, chat input) |
| **Config**  | `python-dotenv` + `.env` for API key |
| **Language**| Python 3.x |

---

## Credits & Acknowledgments

- **Mistral AI** — This project uses **Mistral**’s language model (`mistral-small-2506`) for chat completions. Mistral provides the core LLM capability that powers Asista AI’s responses.  
  - [Mistral AI](https://www.mistral.ai/)  
  - [Mistral API Documentation](https://docs.mistral.ai/)

- **LangChain** — Used for the unified chat model interface (`init_chat_model`) and integration with Mistral (`langchain-mistralai`).

- **Streamlit** — Used for the web UI and chat experience.

---

## Learning Outcomes

By working through or studying this project, you can:

1. **Use LangChain’s unified chat API** — Initialize a provider-agnostic chat model with `init_chat_model` and invoke it with a list of messages for multi-turn conversation.

2. **Integrate an LLM with Mistral** — Configure and call Mistral’s API (e.g. `mistral-small-2506`) via LangChain, including environment-based API key management.

3. **Separate backend and frontend** — Design a small backend module that exposes a single function (`get_response`) and a frontend that only handles UI and session state, making the same logic reusable across CLI and web.

4. **Build a Streamlit chat app** — Use `st.chat_message`, `st.chat_input`, and `st.session_state` to implement a persistent chat interface that calls an external backend function.

5. **Manage conversation state** — Maintain a list of messages (user/assistant) in memory and pass the full history to the model so it can produce context-aware responses.

6. **Run the same logic in two ways** — Use `if __name__ == "__main__"` to keep a CLI entry point in the same file that is also imported by Streamlit, so one codebase serves both interfaces.

7. **Handle configuration and secrets** — Use `.env` and `python-dotenv` for API keys and avoid committing secrets to version control.

8. **Read and use a dependency list** — Rely on `requirements.txt` for reproducible setup and understand the roles of LangChain, Streamlit, and provider-specific packages.

---

**Author:** Sahil Bhatti

---

*Asista AI by Sahil Bhatti. Powered by Mistral.*
