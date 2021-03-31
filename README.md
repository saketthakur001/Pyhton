# Pyhton

A personal archive of Python scripts and small projects from learning/experimenting with the language — automation, machine learning basics, games, and a handful of utility tools. This is a collection of individual scripts rather than a single application, and quality/completeness varies from script to script.

## What's in here

- **`linear_regression/`** — small scripts fitting/plotting linear regression by hand (matplotlib), e.g. `liniear regression.py`, `population prediction.py`, `hotel prediction.py`, `celsius to fahienheit.py`.
- **`machine learning/gym/`** — early experiments with OpenAI Gym.
- **`Noah_Assistent/`** — `Noah Assistant.py`, a Windows voice assistant built on `pyttsx3`, `speech_recognition`, and `wikipedia` (wake-word style commands, opens apps/websites, tells time, etc.). Hardcoded to a Windows username-based music folder path.
- **`Pyautogui/`** — GUI-automation scripts using `pyautogui`, including a downloader helper and a typing-race "hack" (auto-typer).
- **`record_mouse_and_keyboard/`** — records and replays mouse/keyboard events using the `mouse`/`keyboard` libraries.
- **`rename/`, `rename_naruto/`** — scripts that scrape/parse episode names (from a saved HTML page) and use them to batch-rename video files.
- **`sub_acceleration/`** — scripts for changing subtitle timing/speed.
- **`text to audio/`** — PDF-to-text extraction (`PyPDF2`) and text-to-speech/MP3 conversion.
- **`video_editing/`** — a script for cutting a clip out of a video.
- **`projects/`** and **`old python projects/`** — a larger, less organized set of practice scripts: Project Euler solutions, a console tic-tac-toe game (some variants with `pygame`), password-related scripts (Wi-Fi password lookup, RAR password guessing, a "password guesser"), a movie/show downloader, currency converter, pandas practice, and more. `old python projects/` appears to be an earlier/duplicate version of `projects/` kept for reference.
- **`For me/`** — personal notes/journal files (`diary.dat`, `thoughts.dat`) and a scratch test script; not part of any project.

## Running the scripts

There's no single entry point or shared `requirements.txt` — each script is standalone. In general:

1. Open the script you want to run and check its imports.
2. Install what it needs, e.g.:
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia pyautogui mouse keyboard PyPDF2 matplotlib pandas gym
   ```
3. Run it directly: `python "path/to/script.py"`

## Known limitations

- Several scripts hardcode absolute Windows paths (e.g. `C:/Users/saket/...`), so they won't run as-is on another machine or OS without editing the path.
- Some scripts (e.g. under `old python projects/`) are unfinished, duplicated, or left as scratch/test files (`Untitled-1.py`, `tests.py`, `test.py`).
- A few filenames/folders contain typos (`liniear regression.py`, `Noah_Assistent`) — left as-is to avoid breaking any references.
- The "password guesser" and Wi-Fi password scripts are basic/educational brute-force or lookup utilities, not security tools.
- No automated tests; this is a learning archive, not a maintained library.
