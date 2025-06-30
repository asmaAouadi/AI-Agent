# 🧠 AI Agent Project

This project is a modular and extensible AI agent powered by a local LLM (via [Ollama](https://ollama.com)) or OpenAI's API. You can choose which backend to use depending on your environment and preferences.

## ✨ Features

* ✅ Dual support for **Ollama** (local) and **OpenAI API** (cloud-based)
* 🧩 Modular design for easy extension
* 📄 Easy setup via `requirements.txt`
* ⚙️ Switch between models with minimal changes


## 🛠️ Requirements

Make sure you have Python 3.8+ installed. All dependencies are listed in `requirements.txt`.

Install with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

You can run the agent in two ways depending on the backend you'd like to use:

### 🔁 1. Run with Ollama (Local Model)

> Requires Ollama to be installed and running.

1. Install Ollama from [https://ollama.com](https://ollama.com)

2. Download a model (example: `llama3`):

   ```bash
   ollama run llama3
   ```

3. Run the project using the Ollama agent:

   ```bash
   python agent_ollama.py
   ```

---

### ☁️ 2. Run with OpenAI (API Key)

1. Set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

   Or create a `.env` file:

   ```
   OPENAI_API_KEY=your_key_here
   ```

2. Run the project using the OpenAI agent:

   ```bash
   python agent_openai.py
   ```

---

## 📁 Project Structure

```
.
├── agent_ollama.py        # Entry point for Ollama-based agent
├── agent_openai.py        # Entry point for OpenAI-based agent
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── ...
```

---

## 📌 Notes

* You can easily switch between agents by using different entry points (`agent_ollama.py` or `agent_openai.py`).
* For best performance with Ollama, make sure your hardware supports the model size you're using.

---

## 🤝 Contributions

Pull requests and issues are welcome! Feel free to fork this repo and enhance the agent further.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---
