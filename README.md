# Jarvis - Voice Assistant

A Python-based voice-activated desktop assistant that listens for a wake word and executes commands like opening websites, playing music, and reading live news headlines.

---

## Features

- 🎙️ Wake word detection — activates on **"Jarvis"**
- 🌐 Opens websites via voice (Google, YouTube)
- 🎵 Plays music from YouTube by song name
- 📰 Reads top news headlines using NewsAPI

---

## Demo

```
You: "Jarvis"
Jarvis: "Ya"
You: "Open Google"
→ Opens google.com in browser

You: "Jarvis"
Jarvis: "Ya"
You: "Play eye"
→ Opens the song on YouTube

You: "Jarvis"
Jarvis: "Ya"
You: "News"
→ Reads top headlines aloud
```

---

## Tech Stack

- **Python 3.x**
- `SpeechRecognition` — microphone input and speech-to-text
- `pyttsx3` — text-to-speech engine
- `PyAudio` — audio stream handling
- `requests` — NewsAPI HTTP calls
- `webbrowser` — browser control

---

## Project Structure

```
jarvis/
├── main.py            # Core assistant logic and wake word loop
├── musicLibrary.py    # Song name → YouTube URL mapping
├── requirements.txt   # Project dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- A working microphone
- [NewsAPI key](https://newsapi.org/) (free)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/jarvis.git
cd jarvis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
# Open main.py and replace the newsapi value:
params = {
    "country": "in",
    "newsapi": "YOUR_API_KEY_HERE"
}

# 4. Run
python main.py
```

> **Note for Windows users:** PyAudio may require a pre-built wheel. Install via:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## Adding Songs

Open `musicLibrary.py` and add entries:

```python
music = {
    "song_name": "https://youtube.com/your-link",
}
```

Then say: *"Jarvis... play song_name"*

---

## Known Limitations

- Requires a stable internet connection for speech recognition (uses Google's API)
- Music library is manually maintained — no Spotify/YouTube search integration yet
- News API key is hardcoded — should be moved to environment variables

---

## Roadmap

- [ ] Move API keys to `.env` file
- [ ] Add more voice commands (weather, calculator, reminders)
- [ ] Migrate to FastAPI backend for web-based control
- [ ] Integrate with OpenAI/Gemini for conversational AI responses

---

## Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## License

[MIT](LICENSE)
