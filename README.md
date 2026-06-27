# 🤖 J.A.R.V.I.S. — AI Voice Assistant

> **Just A Rather Very Intelligent System**

A production-grade AI voice assistant built with Python, inspired by Iron Man's JARVIS. Features multi-provider AI with automatic fallback, long-term memory, intelligent intent routing, a plugin skill architecture, and a premium futuristic GUI.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-00d4ff?style=for-the-badge)](https://github.com/TomSchimansky/CustomTkinter)
[![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## ✨ Features

### 🧠 Multi-Provider AI Engine
- **7+ AI providers**: Google Gemini, OpenAI GPT, Anthropic Claude, Groq, NVIDIA NIM, DeepSeek, OpenRouter
- **Automatic fallback chain** — if one provider fails, seamlessly switches to the next
- **Streaming responses** for real-time conversation
- **Optional local AI** via Ollama (Llama, Qwen) — no internet required

### 🗣️ Voice Interface
- **Speech-to-text** via Google Web Speech API
- **Text-to-speech** with ElevenLabs (premium) or pyttsx3 (offline fallback)
- **Smart response length** — summarizes long answers before reading aloud
- **Push-to-talk** via `Ctrl+Space` hotkey

### 🧩 Plugin Skill Architecture
| Skill | Description |
|-------|-------------|
| 🖥️ App Launcher | Auto-discovers and launches installed applications |
| 🔍 Web Search | Google, YouTube, Wikipedia |
| 📸 Screenshot | Captures and saves to Desktop |
| 📊 System Info | Battery, CPU, RAM, disk usage |
| 🔊 Volume Control | Up, down, mute/unmute via pycaw |
| 🧮 Calculator | Safe math expression evaluation |
| 🌤️ Weather | Current weather via OpenWeatherMap |
| 💬 WhatsApp | Send messages via pywhatkit |
| ⏰ Reminders | Natural language time parsing + notifications |
| 📝 Notes | Persistent note-taking system |
| 📂 File Search | Search Desktop, Documents, Downloads |

> **Easy to extend** — add new skills by creating a single Python file.

### 💾 Long-Term Memory
- **SQLite-backed** persistent memory across restarts
- Remembers **user preferences** and personal facts
- **Conversation history** preserved
- Notes and reminders stored in database
- Contextual recall: *"What sport do I play?"* → *"You told me your favorite sport is badminton."*

### 🎨 Premium GUI
- **Futuristic dark theme** with animated arc reactor
- **Tabbed interface**: Chat, Memory, Settings, Logs
- Real-time status indicators (listening, thinking, speaking)
- Smooth animations and responsive design

### 🏗️ Professional Architecture
- Clean **modular design** with separation of concerns
- **Intent classification → Skill routing → AI fallback** pipeline
- Professional **logging** with file rotation
- **Type hints** and docstrings throughout
- Comprehensive **test suite**
- No hardcoded secrets — environment variables only

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **Windows 10/11**
- **Microphone** (for voice input)
- **Google Gemini API Key** ([Get one free](https://aistudio.google.com/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
copy .env.example .env
# Edit .env and add your Gemini API key (required)
```

### Running

```bash
python main.py
```

Or double-click `launch_jarvis.bat`.

---

## 🏛️ Architecture

```
jarvis/
├── main.py                 # Entry point
├── config/
│   ├── settings.py         # Environment & constants
│   └── prompts.py          # AI personality & prompts
├── core/
│   ├── assistant.py        # Main orchestrator
│   ├── brain.py            # Multi-provider AI engine
│   ├── speech.py           # STT & TTS unified module
│   ├── memory.py           # SQLite long-term memory
│   ├── intent.py           # Intent classifier
│   ├── tool_router.py      # Plugin skill router
│   └── logger.py           # Professional logging
├── skills/
│   ├── browser.py          # Web, YouTube, Wikipedia
│   ├── system.py           # Apps, volume, battery, power
│   ├── calculator.py       # Math evaluation
│   ├── weather.py          # OpenWeatherMap
│   ├── reminders.py        # Reminder system
│   ├── screenshots.py      # Screen capture
│   ├── whatsapp.py         # WhatsApp messaging
│   └── files.py            # File search
├── gui/
│   ├── app.py              # Main window (tabbed)
│   ├── widgets.py          # Custom widgets
│   └── animations.py       # Arc reactor animation
├── database/               # SQLite (auto-created)
├── logs/                   # Log files (auto-created)
├── assets/                 # Icons & static files
└── tests/                  # Test suite
```

### How It Works

```
User Input (Voice / Text)
         │
         ▼
  ┌─────────────┐
  │   Intent     │  Rule-based classifier
  │  Classifier  │  (no AI calls needed)
  └──────┬──────┘
         │
    ┌────┴────┐
    ▼         ▼
 Skill     AI Brain
 Router    (Multi-provider
  │        + fallback)
  │         │
  └────┬────┘
       ▼
  ┌─────────┐
  │ Memory  │  SQLite persistence
  │ System  │
  └────┬────┘
       ▼
  Speech Output
  (ElevenLabs / pyttsx3)
```

---

## 🔧 Configuration

### Required
| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Google Gemini API key ([Get one](https://aistudio.google.com/apikey)) |

### Optional AI Providers
| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI GPT models |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `GROQ_API_KEY` | Groq (ultra-fast inference) |
| `NVIDIA_NIM_API_KEY` | NVIDIA NIM |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `OPENROUTER_API_KEY` | OpenRouter (100+ models) |

### Optional Features
| Variable | Description |
|----------|-------------|
| `ELEVENLABS_API_KEY` | Premium human-like voice |
| `OPENWEATHER_API_KEY` | Weather data |
| `AI_MODE` | `cloud` (default) or `local` (Ollama) |
| `OLLAMA_MODEL` | Model name for local AI (default: `llama3`) |

---

## 🧪 Testing

```bash
python -m pytest tests/ -v
```

---

## 🛣️ Roadmap

- [ ] Screen sharing & visual analysis
- [ ] Google Calendar integration
- [ ] Email management
- [ ] Smart home control (Home Assistant)
- [ ] Multi-language support
- [ ] Mobile companion app
- [ ] Custom wake word training (Picovoice)
- [ ] Voice cloning

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.10+ |
| GUI | CustomTkinter |
| AI | Google Gemini, OpenAI, Anthropic, Groq, NVIDIA NIM |
| Speech | SpeechRecognition, pyttsx3, ElevenLabs |
| Database | SQLite3 |
| System | psutil, pycaw, pywin32 |
| Testing | pytest, unittest |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Inspired by **J.A.R.V.I.S.** from the Marvel Cinematic Universe
- Powered by **Google Gemini AI**

---

*Built with ❤️ as a portfolio project demonstrating AI engineering, system integration, and software architecture.*
