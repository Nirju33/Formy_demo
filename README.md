# $\textcolor{#1E90FF}{\text{Formy QA}}$

Selenium + Python scripts for testing UI elements on the [Formy Project](https://formy-project.herokuapp.com/) demo website.

## $\textcolor{#1E90FF}{\text{Overview}}$

This project automates common UI interactions — buttons, checkboxes, radio buttons, dropdowns, date pickers, drag and drop, file upload, modals, autocomplete, page scrolling, tab switching, and full form submission — using Selenium WebDriver in Python.

## $\textcolor{#1E90FF}{\text{Requirements}}$

- Python 3.14+
- Google Chrome
- [uv](https://docs.astral.sh/uv/)

## $\textcolor{#1E90FF}{\text{Setup}}$

1. Clone the repository

```
git clone https://github.com/Nirju33/Formy_demo.git
cd formy_qa
```

2. Create a virtual environment

```
uv venv
```

3. Activate the virtual environment

Windows

```
.venv\Scripts\activate
```

macOS/Linux

```
source .venv/bin/activate
```

4. Install dependencies

```
uv sync
```

## $\textcolor{#1E90FF}{\text{Running the Tests}}$

Run all tests:

```
pytest
```

Run tests with detailed output:

```
pytest -v
```

Run a specific test file:

```
pytest enabledisable.py
```

## $\textcolor{#1E90FF}{\text{Note}}$

`fileupload.py` uses a hardcoded file path (`C:\Users\NIRJALA\Downloads\four.png`). Change this to a file on your own computer before running it.

## $\textcolor{#1E90FF}{\text{Tech Stack}}$

- Python
- Selenium
- uv (for dependencies)

## $\textcolor{#1E90FF}{\text{Author}}$

**Nirju** – QA Automation Engineer