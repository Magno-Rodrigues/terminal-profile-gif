# Terminal Profile GIF

> Animated terminal-style developer profile generator for GitHub README files, portfolios, and personal websites.

## Author

**Carlos Magno R. de Assis**  
AI Engineer | LLMs & RAG | AI Security

- GitHub: https://github.com/Magno-Rodigues
- LinkedIn: https://linkedin.com/in/cmrda
- Email: cmrda@outlook.com

---

## Overview

**Terminal Profile GIF** is a Python-based generator for creating an animated terminal-style developer profile.

It combines a static profile/background image with a simulated command-line session. Profile information is rendered progressively, character by character, with a blinking terminal cursor and configurable colors.

The animation can cycle through multiple languages, allowing the same profile to be presented in English, Portuguese, Spanish, or any other language added to the configuration.

The project is designed to be easy to customize while keeping the animation behavior deterministic and visually consistent.

---

## Features

- Character-by-character terminal typing animation
- Blinking cursor before every line
- Configurable number of cursor blinks
- Configurable typing speed
- Configurable cursor timing
- Multilingual profile content
- Configurable language order
- Configurable interval between language cycles
- Configurable final pause
- Configurable terminal position
- Configurable font size and line spacing
- Configurable prompt and cursor characters
- Independent colors for prompt, labels, values, and language indicator
- Global GIF palette for consistent colors across frames
- Infinite GIF looping
- Custom background/profile image
- Easy addition of new languages
- No external API or runtime service required

---

## How the animation works

Each line follows the same sequence:

```text
Cursor visible
      ↓
Cursor invisible
      ↓
Cursor visible
      ↓
Cursor invisible
      ↓
Cursor visible
      ↓
Cursor invisible
      ↓
Character-by-character typing
      ↓
Completed line remains visible
      ↓
Next line
```

After an entire language cycle is completed, the final state remains visible for the configured interval before the next language begins.

Example:

```text
English
   ↓
[interval]
   ↓
Português
   ↓
[interval]
   ↓
Español
   ↓
[final pause]
   ↓
Loop
```

The language indicator becomes part of the terminal state after it is typed, so it remains visible throughout that language's profile cycle.

---

# Requirements

- Python 3.9+
- Pillow

Install Pillow:

```bash
pip install Pillow
```

Using a virtual environment is recommended:

```bash
python -m venv .venv
source .venv/bin/activate
pip install Pillow
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install Pillow
```

---

# Project structure

```text
.
├── perfil.png
├── gerar_gif.py
└── README.md
```

After generation:

```text
.
├── perfil.png
├── gerar_gif.py
├── terminal_profile.gif
└── README.md
```

| File | Description |
|---|---|
| `perfil.png` | Background/profile image |
| `gerar_gif.py` | GIF animation generator |
| `terminal_profile.gif` | Generated animated profile |
| `README.md` | Project documentation |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Magno-Rodigues/terminal-profile-gif.git
cd terminal-profile-gif
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install Pillow:

```bash
pip install Pillow
```

---

# Usage

Place the background image in the project directory:

```text
perfil.png
```

Then run:

```bash
python gerar_gif.py
```

The generator creates:

```text
terminal_profile.gif
```

---

# Configuration

Animation behavior is centralized in the `CONFIG` dictionary.

```python
CONFIG = {

    # Files
    "nome_arquivo": "terminal_profile.gif",
    "imagem_fundo": "perfil.png",

    # Language order
    "ordem_idiomas": ["EN", "PT", "ES"],

    # Cursor
    "quantidade_piscadas": 3,
    "duracao_cursor_visivel": 250,
    "duracao_cursor_invisivel": 250,

    # Typing
    "duracao_por_caractere": 60,

    # Intervals
    "intervalo_entre_ciclos": 2000,
    "duracao_final": 4000,

    # Layout
    "tamanho_fonte": 24,
    "espacamento_linha": 15,
    "x_inicial": 540,
    "y_inicial": 255,

    # Terminal
    "prompt": "$ ",
    "cursor": "_",

    # Language indicator
    "mostrar_indicador_idioma": True,
    "formato_indicador_idioma": "[{codigo}] {nome}",

    # Colors
    "cor_prompt": (201, 209, 217),
    "cor_rotulo": (242, 141, 53),
    "cor_valor": (141, 231, 241),
    "cor_idioma": (201, 209, 217),

    # GIF
    "loop": 0,
    "optimize": False,
    "dither": False,
}
```

## Language order

```python
"ordem_idiomas": ["EN", "PT", "ES"]
```

Controls the sequence of the animation.

Examples:

```python
"ordem_idiomas": ["PT", "EN", "ES"]
```

or:

```python
"ordem_idiomas": ["ES", "PT", "EN"]
```

or only English:

```python
"ordem_idiomas": ["EN"]
```

No animation logic needs to be changed.

## Cursor blinking

```python
"quantidade_piscadas": 3
```

Controls how many blink cycles occur before each line is typed.

## Cursor timing

```python
"duracao_cursor_visivel": 250,
"duracao_cursor_invisivel": 250,
```

Values are in milliseconds.

## Typing speed

```python
"duracao_por_caractere": 60
```

Lower values produce faster typing.

Example:

```python
"duracao_por_caractere": 35
```

## Interval between languages

```python
"intervalo_entre_ciclos": 2000
```

Controls how long the completed language remains visible before the next language begins.

The previous language remains on screen during the interval.

## Final pause

```python
"duracao_final": 4000
```

Controls how long the final language remains visible before the GIF loops.

## Layout

```python
"tamanho_fonte": 24,
"espacamento_linha": 15,
"x_inicial": 540,
"y_inicial": 255,
```

These parameters control font size, line spacing, and terminal position.

## Prompt and cursor

```python
"prompt": "$ ",
"cursor": "_",
```

Both can be customized.

For example:

```python
"prompt": "> ",
"cursor": "█",
```

## Language indicator

Enable or disable it:

```python
"mostrar_indicador_idioma": True
```

Default:

```text
$ [EN] English
```

The format is configurable:

```python
"formato_indicador_idioma": "[{codigo}] {nome}"
```

Available placeholders:

- `{codigo}` — language code
- `{nome}` — language name

Example:

```python
"formato_indicador_idioma": "LANG={codigo} | {nome}"
```

produces:

```text
$ LANG=EN | English
```

---

# Profile content

Profile content is separated from animation configuration.

Example:

```python
IDIOMAS = {

    "EN": {
        "nome": "English",

        "linhas": [
            " ",
            "Name: ........ Carlos Magno R. de Assis",
            "Role: ........ AI Engineer | LLMs & RAG | AI Security",
            "Location: .... Brazil (Remote)",
            "Focus: ....... AI Engineering, Intelligent Systems & Data",
            "Stack: ....... Python, PostgreSQL, Docker, Ollama, MinIO, Power BI",
            "Specialties: . LLMs, RAG, AI Security, Prompt Engineering",
            "Experience: .. Software Development, AI & Data Analytics",
            " ",
            "CONTACT",
            "Email: ....... cmrda@outlook.com",
            "GitHub: ...... Magno-Rodigues",
            "LinkedIn: .... linkedin.com/in/cmrda",
        ],
    },
}
```

Each item in `linhas` becomes a terminal line.

---

# Adding a language

Add a new entry to `IDIOMAS`:

```python
"FR": {
    "nome": "Français",

    "linhas": [
        " ",
        "Nom: ........ Carlos Magno R. de Assis",
        "Rôle: ....... AI Engineer | LLMs & RAG | AI Security",
        "Localisation: Brésil (Remote)",
        "Focus: ...... AI Engineering, Intelligent Systems & Data",
        "Stack: ...... Python, PostgreSQL, Docker, Ollama, MinIO, Power BI",
        "Spécialités: LLMs, RAG, AI Security, Prompt Engineering",
        "Expérience: . Software Development, AI & Data Analytics",
        " ",
        "CONTACT",
        "Email: ....... cmrda@outlook.com",
        "GitHub: ...... Magno-Rodigues",
        "LinkedIn: .... linkedin.com/in/cmrda",
    ],
},
```

Then add it to the desired position:

```python
"ordem_idiomas": ["EN", "FR", "PT", "ES"]
```

The animation engine does not need to be modified.

---

# Line formatting

Lines containing `:` are automatically divided into two visual sections.

Example:

```text
Name: ........ Carlos Magno R. de Assis
```

The label uses `cor_rotulo`.

The value uses `cor_valor`.

Lines without `:` are rendered as a single text block.

This makes headings such as:

```text
CONTACT
```

possible without additional formatting.

---

# Colors

The terminal uses independent RGB colors:

```python
"cor_prompt": (201, 209, 217),
"cor_rotulo": (242, 141, 53),
"cor_valor": (141, 231, 241),
"cor_idioma": (201, 209, 217),
```

### Prompt

Controls `$` and the typing cursor.

### Labels

Controls labels such as:

```text
Name:
Role:
Location:
Focus:
Stack:
Email:
```

### Values

Controls the actual profile data.

### Language indicator

Controls:

```text
[EN] English
[PT] Português
[ES] Español
```

---

# GIF color consistency

GIF uses indexed color palettes.

Because the animation contains many frames, independent palette generation can cause subtle color changes between frames.

The generator therefore creates a shared global palette and reserves the main terminal colors.

Dithering is disabled by default:

```python
"dither": False
```

GIF optimization is also disabled:

```python
"optimize": False
```

This prioritizes visual consistency over maximum file-size reduction.

---

# Font selection

The generator attempts to load a monospace font from several common locations, including:

- Consolas
- Courier
- Courier New
- DejaVu Sans Mono

A monospace font is recommended because terminal output depends on predictable character widths.

If no configured font is found, the script falls back to a system/default font.

---

# GitHub README integration

Place the generated GIF in your repository, for example:

```text
assets/
└── terminal_profile.gif
```

Then include it in your README:

```html
<p align="center">
  <img
    src="assets/terminal_profile.gif"
    alt="Animated terminal profile"
  />
</p>
```

Or:

```markdown
![Animated Terminal Profile](assets/terminal_profile.gif)
```

---

# Recommended workflow

```text
Edit profile content
       ↓
Adjust CONFIG
       ↓
Run generator
       ↓
Review GIF
       ↓
Adjust timing/layout
       ↓
Generate again
       ↓
Commit GIF
       ↓
Use in README
```

---

# Technical design

The generator separates three concerns:

```text
Configuration
     ↓
Profile content
     ↓
Animation / rendering engine
```

### Configuration

Controls how the animation behaves.

### Profile content

Controls what is displayed.

### Rendering engine

Controls how content becomes animation frames.

Each frame is generated from a clean copy of the background image. The current terminal state is then rendered over it.

Previously completed lines are redrawn for every frame, preventing artifacts caused by modifying frames in place.

The language indicator becomes part of the terminal state after it is typed, so it remains visible during the corresponding profile cycle.

A global palette preserves the configured terminal colors across frames.

---

# Troubleshooting

## Background image not found

Check that:

```text
perfil.png
gerar_gif.py
```

are in the expected location, or change:

```python
"imagem_fundo": "perfil.png"
```

## Text is outside the image

Adjust:

```python
"x_inicial": 540,
"y_inicial": 255,
```

## Text is too large

Reduce:

```python
"tamanho_fonte": 24
```

For example:

```python
"tamanho_fonte": 20
```

## Animation is too slow

Reduce:

```python
"duracao_por_caractere": 60
```

For example:

```python
"duracao_por_caractere": 40
```

## Cursor blinks too much

Reduce:

```python
"quantidade_piscadas": 3
```

## Languages change too quickly

Increase:

```python
"intervalo_entre_ciclos": 2000
```

For example:

```python
"intervalo_entre_ciclos": 3000
```

---

# License

This project is provided for personal and portfolio use.

If you distribute or adapt the project, update this section according to the license you choose for the repository.

---

## Author

**Carlos Magno R. de Assis**

AI Engineer focused on:

- AI Engineering
- LLM Applications
- Retrieval-Augmented Generation (RAG)
- AI Security
- Prompt Engineering
- Software Engineering
- Data Analytics
- Power BI

- GitHub: https://github.com/Magno-Rodigues
- LinkedIn: https://linkedin.com/in/cmrda
- Email: cmrda@outlook.com

> Built with Python and Pillow.
>
> AI as an engineering multiplier.
