# Terminal Profile GIF

> Animated terminal-style developer profile generator for GitHub README files, portfolios, and personal websites.

## Author

<p align="center">
  <img
    src="terminal_profile.gif"
    alt="Animated terminal profile"
  />
</p>

## Overview

**Terminal Profile GIF** is a Python-based generator for creating an animated terminal-style developer profile.

It combines a static profile/background image with a simulated command-line session. Profile information is rendered progressively, character by character, with a blinking terminal cursor and configurable colors.

The animation can cycle through multiple languages, allowing the same profile to be presented in English, Portuguese, Spanish, or any other language added to the configuration.

The project is designed to be easy to customize while keeping the animation behavior deterministic and visually consistent.

The generator can also export the same animation to MP4 using FFmpeg, making it suitable for platforms that do not accept animated GIFs.

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
- Lossless GIF post-processing with Gifsicle
- MP4 export using FFmpeg
- Significant file-size reduction without intentional visual quality loss
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
- Gifsicle
- FFmpeg (required for MP4 export)

Install Pillow:

```bash
pip install Pillow
```

Gifsicle is used as a post-processing step to losslessly optimize the generated GIF and reduce its file size.

On Ubuntu / Debian:

```bash
sudo apt update
sudo apt install gifsicle
```

FFmpeg is used to convert the generated GIF into an MP4 video without changing the source animation logic.

On Ubuntu / Debian:

```bash
sudo apt update
sudo apt install ffmpeg
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

> Gifsicle is an optional post-processing dependency. If it is not installed, the generator still creates the GIF normally and keeps the unoptimized output.
>
> FFmpeg is optional if only the GIF is required. If FFmpeg is not available, the GIF is still generated normally and MP4 export is skipped with a warning.

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
├── terminal_profile.mp4
└── README.md
```

| File | Description |
|---|---|
| `perfil.png` | Background/profile image |
| `gerar_gif.py` | GIF and MP4 animation generator |
| `terminal_profile.gif` | Generated animated profile |
| `terminal_profile.mp4` | Generated MP4 version of the animation |
| `README.md` | Project documentation |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Magno-Rodrigues/terminal-profile-gif.git
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

Install Gifsicle on Ubuntu / Debian:

```bash
sudo apt update
sudo apt install gifsicle
```

Install FFmpeg on Ubuntu / Debian:

```bash
sudo apt update
sudo apt install ffmpeg
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

When MP4 export is enabled and FFmpeg is available, it also creates:

```text
terminal_profile.mp4
```

After the GIF is generated, Gifsicle performs a lossless optimization pass when enabled in `CONFIG`.

Typical output can be reduced substantially, for example:

```text
Before:  ~1.9 MB
After:   ~0.5 MB
Reduction: ~74%
```

The exact result depends on the number of frames, background image, text content, and animation configuration.

## MP4 export

The MP4 is generated from the completed GIF using FFmpeg. This keeps the existing Pillow rendering and animation state machine unchanged.

The conversion pipeline is:

```text
Pillow
  ↓
Animation frames
  ↓
Global palette
  ↓
Base GIF
  ↓
Gifsicle (lossless)
  ↓
Optimized GIF
  ↓
FFmpeg
  ↓
MP4
```

The default MP4 settings are controlled from `CONFIG`:

```python
"gerar_mp4": True,
"nome_arquivo_mp4": "terminal_profile.mp4",
"fps_mp4": 20,
"qualidade_mp4": 20,
```

The exporter uses H.264 with `yuv420p` for broad video compatibility and applies `+faststart` so the MP4 is suitable for web upload and playback.

The GIF remains the primary animation output. MP4 is an additional representation of the same animation for platforms that require video instead of GIF.

If FFmpeg is unavailable, the script prints a warning and continues without failing GIF generation.

For LinkedIn, use the MP4 version when the platform rejects the GIF because of its frame count or GIF-specific limits.

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

    # Lossless compression
    "otimizar_gif": True,
    "nivel_otimizacao": 3,

    # MP4
    "gerar_mp4": True,
    "nome_arquivo_mp4": "terminal_profile.mp4",
    "fps_mp4": 20,
    "qualidade_mp4": 20,
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

## MP4 export settings

```python
"gerar_mp4": True
```

Enables or disables MP4 generation.

```python
"nome_arquivo_mp4": "terminal_profile.mp4"
```

Controls the output filename.

```python
"fps_mp4": 20
```

Controls the target video frame rate used by the MP4 exporter.

```python
"qualidade_mp4": 20
```

Controls the H.264 CRF quality setting. Lower values produce higher quality and larger files; higher values produce smaller files with more compression.

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
            "GitHub: ...... Magno-Rodrigues",
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
        "GitHub: ...... Magno-Rodrigues",
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

The base GIF is generated with Pillow using the global palette and without Pillow's additional GIF optimization. A separate Gifsicle post-processing step then performs structural, lossless optimization.

This separation keeps the existing rendering and color behavior intact while significantly reducing the final file size.

## Lossless GIF optimization

Gifsicle is used after Pillow finishes generating the GIF:

```text
Pillow
  ↓
Animation frames
  ↓
Global palette
  ↓
Base GIF
  ↓
Gifsicle (lossless)
  ↓
Optimized GIF
```

The optimization does not intentionally resize, recolor, or reduce the visual quality of the animation. It focuses on removing redundant GIF data and optimizing frame structure.

The feature is enabled by default:

```python
"otimizar_gif": True,
"nivel_otimizacao": 3,
```

If Gifsicle is unavailable, the script preserves the generated GIF and displays a warning instead of failing the generation process.

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

For platforms that require video instead of GIF, use the generated MP4:

```text
terminal_profile.mp4
```

The MP4 uses the same animation rendered for the GIF and is intended as a video-compatible alternative rather than a separate animation implementation.

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
Review MP4 if required
       ↓
Adjust timing/layout
       ↓
Generate again
       ↓
Lossless GIF optimization
       ↓
MP4 export with FFmpeg
       ↓
Commit outputs
       ↓
Use GIF or MP4 on the target platform
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

Gifsicle is applied only after the GIF has been generated, keeping rendering and compression concerns separated.

FFmpeg is applied after GIF generation and does not alter the animation state machine or rendering logic.

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

## GIF is not compressed

Check whether Gifsicle is installed:

```bash
command -v gifsicle
```

On Ubuntu / Debian, install it with:

```bash
sudo apt update
sudo apt install gifsicle
```

Then run the generator again:

```bash
python gerar_gif.py
```

## MP4 is not generated

Check whether FFmpeg is installed:

```bash
command -v ffmpeg
```

You can also verify the executable directly:

```bash
ffmpeg -version
```

On Ubuntu / Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Then run the generator again:

```bash
python gerar_gif.py
```

If FFmpeg is unavailable, GIF generation continues normally and only the MP4 export is skipped.

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

- GitHub: https://github.com/Magno-Rodrigues
- LinkedIn: https://linkedin.com/in/cmrda
- Email: cmrda@outlook.com

> Built with Python and Pillow.
>
> AI as an engineering multiplier.
