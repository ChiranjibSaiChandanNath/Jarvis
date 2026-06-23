# JARVIS

<div align="center">

<!-- Animated multi-line typing title -->
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=30&duration=2800&pause=900&color=4FC3F7&center=true&vCenter=true&multiline=false&width=720&lines=J.A.R.V.I.S.+%E2%80%94+Voice+Assistant;Local+Kokoro+TTS+%7C+Groq+Llama+3.3" alt="J.A.R.V.I.S." />

<br/>

<!-- Enhanced animated SVG — glowing cap with pulse rings + orbiting dots -->
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <defs>
    <radialGradient id="pulseGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4FC3F7" stop-opacity="0.22"/>
      <stop offset="70%" stop-color="#7C4DFF" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4FC3F7" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#4FC3F7" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Soft background glow -->
  <circle cx="100" cy="100" r="90" fill="url(#pulseGlow)">
    <animate attributeName="r" values="80;92;80" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;1;0.6" dur="4s" repeatCount="indefinite"/>
  </circle>

  <!-- Static reference rings -->
  <circle cx="100" cy="100" r="88" fill="none" stroke="#4FC3F7" stroke-width="0.5" stroke-opacity="0.12"/>
  <circle cx="100" cy="100" r="70" fill="none" stroke="#4FC3F7" stroke-width="0.5" stroke-opacity="0.12"/>
  <circle cx="100" cy="100" r="50" fill="none" stroke="#7C4DFF" stroke-width="0.5" stroke-opacity="0.12"/>

  <!-- Crosshair guides -->
  <line x1="100" y1="12" x2="100" y2="188" stroke="#4FC3F7" stroke-width="0.4" stroke-opacity="0.15"/>
  <line x1="12" y1="100" x2="188" y2="100" stroke="#4FC3F7" stroke-width="0.4" stroke-opacity="0.15"/>

  <!-- Outer spinning dashed ring -->
  <circle cx="100" cy="100" r="88" fill="none" stroke="#4FC3F7" stroke-width="1.4"
    stroke-dasharray="18 9" stroke-linecap="round" stroke-opacity="0.65">
    <animateTransform attributeName="transform" type="rotate"
      from="0 100 100" to="360 100 100" dur="10s" repeatCount="indefinite"/>
  </circle>

  <!-- Middle counter-rotating dashed ring -->
  <circle cx="100" cy="100" r="72" fill="none" stroke="#7C4DFF" stroke-width="0.9"
    stroke-dasharray="7 6" stroke-opacity="0.5">
    <animateTransform attributeName="transform" type="rotate"
      from="360 100 100" to="0 100 100" dur="7s" repeatCount="indefinite"/>
  </circle>

  <!-- Inner pulse ring -->
  <circle cx="100" cy="100" r="50" fill="none" stroke="#00e676" stroke-width="0.7"
    stroke-dasharray="4 8" stroke-opacity="0.4">
    <animateTransform attributeName="transform" type="rotate"
      from="0 100 100" to="360 100 100" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="stroke-opacity" values="0.2;0.6;0.2" dur="3s" repeatCount="indefinite"/>
  </circle>

  <!-- Orbiting dot 1 (cyan, outer ring) -->
  <circle r="4" fill="#4FC3F7" opacity="0.9">
    <animateMotion dur="10s" repeatCount="indefinite">
      <mpath href="#orbit1"/>
    </animateMotion>
    <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite"/>
  </circle>
  <path id="orbit1" d="M 100,12 A 88,88 0 1 1 99.9,12" fill="none"/>

  <!-- Orbiting dot 2 (purple, middle ring, opposite phase) -->
  <circle r="3" fill="#7C4DFF" opacity="0.8">
    <animateMotion dur="7s" repeatCount="indefinite" keyPoints="0.5;1;0.5" keyTimes="0;0.5;1" calcMode="linear">
      <mpath href="#orbit2"/>
    </animateMotion>
  </circle>
  <path id="orbit2" d="M 100,28 A 72,72 0 1 1 99.9,28" fill="none"/>

  <!-- Orbiting dot 3 (green, inner ring) -->
  <circle r="2.5" fill="#00e676" opacity="0.7">
    <animateMotion dur="4s" repeatCount="indefinite" keyPoints="0.25;1;0.25" keyTimes="0;0.5;1" calcMode="linear">
      <mpath href="#orbit3"/>
    </animateMotion>
  </circle>
  <path id="orbit3" d="M 100,50 A 50,50 0 1 1 99.9,50" fill="none"/>

  <!-- Arc Reactor Outer Ring -->
  <circle cx="100" cy="100" r="28" fill="none" stroke="#4FC3F7" stroke-width="1.8" stroke-opacity="0.8">
    <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
  </circle>
  <!-- Arc Reactor Inner Core -->
  <circle cx="100" cy="100" r="14" fill="rgba(79,195,247,0.18)" stroke="#4FC3F7" stroke-width="2.5">
    <animate attributeName="r" values="12;15;12" dur="2s" repeatCount="indefinite"/>
  </circle>
  <!-- Arc Reactor Segments (Triangular / Lines radiating) -->
  <g stroke="#4FC3F7" stroke-width="1.5" stroke-opacity="0.7">
    <line x1="100" y1="68" x2="100" y2="76" />
    <line x1="100" y1="124" x2="100" y2="132" />
    <line x1="68" y1="100" x2="76" y2="100" />
    <line x1="124" y1="100" x2="132" y2="100" />
    <line x1="77" y1="77" x2="83" y2="83" />
    <line x1="123" y1="123" x2="117" y2="117" />
    <line x1="77" y1="123" x2="83" y2="117" />
    <line x1="123" y1="77" x2="117" y2="83" />
  </g>

  <!-- Core centre glow -->
  <circle cx="100" cy="100" r="16" fill="url(#coreGlow)">
    <animate attributeName="r" values="14;18;14" dur="2.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2.5s" repeatCount="indefinite"/>
  </circle>

  <!-- Corner blinking status dots -->
  <circle cx="28" cy="38" r="2.5" fill="#4FC3F7">
    <animate attributeName="opacity" values="0;1;0" dur="2.2s" begin="0.1s" repeatCount="indefinite"/>
  </circle>
  <circle cx="172" cy="140" r="2.5" fill="#7C4DFF">
    <animate attributeName="opacity" values="0;1;0" dur="2.7s" begin="0.7s" repeatCount="indefinite"/>
  </circle>
  <circle cx="164" cy="34" r="2" fill="#00e676">
    <animate attributeName="opacity" values="0;1;0" dur="2s" begin="1.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="34" cy="152" r="2" fill="#ff6d00">
    <animate attributeName="opacity" values="0;1;0" dur="2.4s" begin="0.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="100" cy="16" r="1.8" fill="#4FC3F7" opacity="0.5">
    <animate attributeName="opacity" values="0.2;0.9;0.2" dur="1.8s" begin="0.9s" repeatCount="indefinite"/>
  </circle>
</svg>

<br/>

<!-- Badge row 1: Core stack -->
![Python](https://img.shields.io/badge/Python-3.11+-4FC3F7?style=for-the-badge&logo=python&logoColor=black&labelColor=0a0f1e)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-7C4DFF?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=0a0f1e)
![TypeScript](https://img.shields.io/badge/TypeScript-Vite-ff6d00?style=for-the-badge&logo=typescript&logoColor=white&labelColor=0a0f1e)
![Three.js](https://img.shields.io/badge/Three.js-Orb-00e676?style=for-the-badge&logo=three.js&logoColor=white&labelColor=0a0f1e)

<br/>

<!-- Badge row 2: Tools & status -->
![Groq](https://img.shields.io/badge/Groq-API-4FC3F7?style=for-the-badge&labelColor=0a0f1e)
![Llama 3.3](https://img.shields.io/badge/Llama_3.3-LLM-7C4DFF?style=for-the-badge&labelColor=0a0f1e)
![Kokoro TTS](https://img.shields.io/badge/Kokoro_TTS-ONNX-00e676?style=for-the-badge&labelColor=0a0f1e)
![SQLite](https://img.shields.io/badge/SQLite-Memory-ff6d00?style=for-the-badge&logo=sqlite&logoColor=white&labelColor=0a0f1e)
![Status](https://img.shields.io/badge/Status-Active-00e676?style=for-the-badge&labelColor=0a0f1e)


<br/>

> **A Voice-First AI Assistant with Local Speech Synthesis, and Groq Llama 3.3 Reasoning**

<br/>

<!-- GitHub repo stats -->
[![Stars](https://img.shields.io/github/stars/ChiranjibSaiChandanNath/Jarvis?style=social)](https://github.com/ChiranjibSaiChandanNath/Jarvis/stargazers)
[![Forks](https://img.shields.io/github/forks/ChiranjibSaiChandanNath/Jarvis?style=social)](https://github.com/ChiranjibSaiChandanNath/Jarvis/network/members)
[![Issues](https://img.shields.io/github/issues/ChiranjibSaiChandanNath/Jarvis?color=ff6d00&style=flat-square)](https://github.com/ChiranjibSaiChandanNath/Jarvis/issues)
[![Last Commit](https://img.shields.io/github/last-commit/ChiranjibSaiChandanNath/Jarvis?color=00e676&style=flat-square)](https://github.com/ChiranjibSaiChandanNath/Jarvis/commits)

<br/>

> If you find this project useful, please consider giving it a **⭐ Star** — it really helps! 👆

</div>

<!-- Animated wave divider -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="60" viewBox="0 0 900 60" preserveAspectRatio="none">
  <defs>
    <linearGradient id="waveGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#4FC3F7" stop-opacity="0"/>
      <stop offset="20%"  stop-color="#4FC3F7" stop-opacity="0.6"/>
      <stop offset="50%"  stop-color="#7C4DFF" stop-opacity="0.6"/>
      <stop offset="80%"  stop-color="#00e676" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00e676" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <path d="M0,30 C150,55 300,5 450,30 C600,55 750,5 900,30" fill="none" stroke="url(#waveGrad)" stroke-width="2">
    <animate attributeName="d"
      values="M0,30 C150,55 300,5 450,30 C600,55 750,5 900,30;
              M0,30 C150,5 300,55 450,30 C600,5 750,55 900,30;
              M0,30 C150,55 300,5 450,30 C600,55 750,5 900,30"
      dur="5s" repeatCount="indefinite"/>
  </path>
  <path d="M0,38 C150,62 300,14 450,38 C600,62 750,14 900,38" fill="none" stroke="url(#waveGrad)" stroke-width="1" opacity="0.4">
    <animate attributeName="d"
      values="M0,38 C150,62 300,14 450,38 C600,62 750,14 900,38;
              M0,38 C150,14 300,62 450,38 C600,14 750,62 900,38;
              M0,38 C150,62 300,14 450,38 C600,62 750,14 900,38"
      dur="5s" begin="0.8s" repeatCount="indefinite"/>
  </path>
</svg>
</div>

> [!IMPORTANT]
> **Always use Google Chrome for the best result.** The voice transcription engine (Web Speech API) is most stable and natively supported in Google Chrome. Other browsers (like Edge, Firefox, or Brave) may fail to capture voice input or raise network connection errors.

---

## Features

- **Voice conversation** -- speak naturally, JARVIS listens and replies with a local British voice
- **Groq LLM** -- powered by `llama-3.3-70b-versatile` for reasoning and `llama-4-scout` for vision
- **Local Kokoro TTS** -- British male voice (`bm_george`) runs fully on CPU via ONNX, no cost
- **Real-time Weather** -- *"What's the weather?"* or *"Weather in Tokyo?"* via OpenWeatherMap
- **Smart Web Browsing** -- *"Search for black holes"*, *"Open github.com"*, *"Search YouTube for lofi"*
- **Task & Notes** -- *"Remind me to call the client"*, *"Save that as a note"*
- **Memory** -- remembers your facts, project context, and preferences across sessions
- **Screen Vision** -- *"What's on my screen?"* triggers a screenshot and AI description
- **Open Apps** -- *"Open Notepad"*, *"Open Spotify"*, *"Launch VS Code"*
- **Write to Notepad** -- *"Write a shopping list in Notepad"* creates and opens it instantly
- **Audio-reactive Orb** -- Three.js particle orb that pulses with your voice

---

## Step-by-Step Windows Setup Guide

Follow this guide to get JARVIS running from scratch on Windows.

### 1. Prerequisites
Ensure you have the following installed on Windows:
- **Python 3.10+** (Ensure "Add Python to PATH" is checked during installation)
- **Node.js 18+** (Ensure "Add to PATH" is checked during installation; includes `npm`. If you don't have it, run `winget install OpenJS.NodeJS.LTS` in a new Command Prompt and restart your terminal)
- **Google Chrome** (required for Web Speech API transcription)
- **Groq API key** -- Powers the LLM brain for free ([Get one here](https://console.groq.com/))
- **OpenWeatherMap API key** (Optional) -- Powers real-time weather details ([Get one here](https://openweathermap.org/api))


### 2. Setup Files & Dependencies

1. Clone the repository and navigate to the project folder:
   ```cmd
   git clone https://github.com/ChiranjibSaiChandanNath/Jarvis.git
   cd Jarvis
   ```

2. Install Python dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

3. Install additional packages needed for local voice synthesis:
   ```cmd
   pip install kokoro-onnx soundfile
   ```

4. Install frontend Node dependencies:
   ```cmd
   cd frontend
   npm install
   cd ..
   ```

### 3. Download Local Kokoro TTS Models
We use local Kokoro voice generation. Run the download script once to fetch the ONNX model files:
```cmd
python download_kokoro.py
```
This downloads `kokoro-v1.0.onnx` and the `voices-v1.0.bin` files to your project folder (~340MB total).

---

## Running JARVIS

There are two ways to start JARVIS — pick whichever suits you.

---

### ⚡ Option A — Automatic (Recommended)

Double-click **`start.bat`** from the `Jarvis` folder, or run it from CMD:
```cmd
start.bat
```

> **First time only:** If no `.env` file exists, `start.bat` automatically copies `.env.example` to `.env` and opens Notepad so you can fill in your API keys. Save the file and press any key to continue.
>
> **Every time after that:** JARVIS starts directly — no prompts, no delays.

`start.bat` does everything automatically:

| Step | What happens |
|------|-------------|
| 1 | Opens **JARVIS Backend** window → runs `py server.py` |
| 2 | Opens **JARVIS Frontend** window → runs `cd frontend && npm run dev` |
| 3 | Waits 3 seconds for Vite to spin up |
| 4 | Opens **Google Chrome** at `http://localhost:5173` automatically |

---

### 🖥️ Option B — Manual (Two Terminals)

If you prefer to run each part yourself:

**Terminal 1 — Backend:**
```cmd
py server.py
```
*Expected output:*
```
[jarvis] Initializing Kokoro TTS model...
[jarvis] Kokoro TTS initialized successfully.
Uvicorn running on http://0.0.0.0:8340
```

**Terminal 2 — Frontend:**
```cmd
cd frontend
npm run dev
```
*Expected output:*
```
  VITE v5.x.x  ready in xxx ms
  ➜  Local:   http://localhost:5173/
```

**Then open Chrome manually:**
```
http://localhost:5173
```

> **Note:** If running Option B for the first time, manually copy `.env.example` to `.env` and fill in your keys:
> ```cmd
> copy .env.example .env
> notepad .env
> ```

---

### Open the Application
- **Local Access**: Open Google Chrome and navigate to **`http://localhost:5173`**
- **Mobile / Local Network**: Connect your phone to the same Wi-Fi, then open Chrome and go to the **Network** IP shown in your frontend terminal (e.g. **`http://192.168.1.15:5173`**)

Click anywhere on the orb page once to activate the audio system. JARVIS will greet you: *"Good afternoon, sir."*


---

## Troubleshooting Voice / Microphone Issues on Windows

If JARVIS greets you but does not respond when you speak:

### 1. "recognition error: network"
If you see this error in Edge/Brave, it means the browser's speech-to-text service is blocked.
- **Fix:** Use **Google Chrome** instead.
- **Brave Fix:** Go to `brave://settings/privacy`, turn ON **"Use Google services for push messaging and speech recognition"**, and restart.

### 2. Silence (No logs appearing when speaking)
If it says `listening...` but doesn't capture your voice:
1. **Chrome Settings:** Paste `chrome://settings/content/microphone` in a new Chrome tab and hit Enter. Make sure your active microphone hardware (e.g. *Microphone (Realtek Audio)*) is selected in the dropdown rather than a virtual driver.
2. **Windows Settings:** Open **Settings** > **Privacy & security** > **Microphone**. Verify:
   - *Microphone access* is **ON**.
   - *Let desktop apps access your microphone* is **ON** (and Google Chrome is allowed).
3. **Sound Control:** In Windows Sound settings, verify that your input volume slider is at `100` and the test meter bounces when you talk.
