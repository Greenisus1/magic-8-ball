# magic 8 ball

Ask a question. Get one random classic-style 8-ball answer, with no translation, AI, explanation, animation or extra answer text. Runs offline with Python3 standard library. No question history, files, API keys or network. For fun, not real predictions. Independent app, not affiliated with Mattel.

    python3 eightball.py

Type /quit or /exit to leave. Blank questions produce no answer. For one answer only:

    python3 eightball.py --question "Will I win?"

Store category: Games. Install checks syntax, no packages installed. Tested on Linux with unit tests and actual PTY question/answer/quit. Raspberry Pi hardware untested.

Response wording reference: https://en.wikipedia.org/wiki/Magic_8-Ball
Toy examples: https://shopping.mattel.com/en-gb/products/magic-8-ball-toys-and-games-original-fortune-teller-ball-30188-en-gb

## Fullscreen Store launch

Version 1.0.1 adds a full-terminal interface when launched through the Store. Python 3 with curses and an interactive terminal are required. The original source remains available directly. Interactive output wraps and scrolls with PgUp/PgDn. Enter returns after completion. Arguments on `bash app-store.sh run` retain the original command-line path. No administrative/package/transfer action ran during validation. Linux terminal checks passed; physical Raspberry Pi and non-Linux systems are untested.
