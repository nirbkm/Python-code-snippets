# uv quickstart on Windows (cmd.exe)

This is a Windows-only guide that uses classic Command Prompt (cmd.exe) syntax. Commands are verified against the official uv docs.

## 1) Install uv (from cmd.exe)

```bat
:: Run the official installer script via PowerShell, from cmd.exe
powershell -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"

:: Alternative if you prefer Python’s package tools (ensure pip/pipx on PATH):
:: pipx install uv
:: pip install uv
```

The first line invokes PowerShell from cmd to execute uv’s Windows installer. The docs also list pip/pipx as alternatives. ([GitHub][1], [Astral Docs][2])

## 2) Initialize a new project

```bat
uv init myapp
cd myapp

:: uv creates pyproject.toml, main.py, README.md, and .python-version
```

Project creation is handled by `uv init`. ([Astral Docs][3])

## 3) Install and pin a Python version

```bat
uv python install 3.12
uv python pin 3.12
```

`uv python` manages multiple Python versions and pins the project with `.python-version`. ([Astral Docs][4], [PyPI][5])

## 4) Create or use the virtual environment

```bat
uv venv

:: You rarely need to activate manually when using uv.
:: If you do need it in cmd.exe:
:: .venv\Scripts\activate.bat
```

uv searches for `.venv` in the current/parent directories and will prompt to create one if missing. ([Astral Docs][6])

## 5) Add dependencies

```bat
:: Runtime dependencies
uv add fastapi pydantic

:: Dev-only dependencies
uv add --dev pytest ruff

:: With a constraint
uv add "requests>=2.32"
```

Dependencies are recorded in `pyproject.toml` and managed by uv. ([Astral Docs][3])

## 6) Run your app and tools

```bat
:: Run your app/tests inside the project environment
uv run python .\main.py
uv run pytest

:: Run a tool ad-hoc without installing it (ephemeral env)
uvx ruff --version

:: Install a tool so it’s available on PATH
uv tool install ruff
```

See uv’s tools guide for `uvx` and `uv tool`. ([Astral Docs][7])

## 7) Lock, sync, and upgrade

```bat
:: Upgrade all locked packages in uv.lock
uv lock --upgrade

:: Install to match the lockfile (or re-sync cleanly)
uv sync
```

Locking and syncing are automatic (e.g., `uv run` locks/syncs before executing), but the explicit commands give you control. ([Astral Docs][8])

## 8) Export requirements.txt (only when needed)

```bat
uv export --format requirements-txt -o requirements.txt
```

Export is for interoperability; the docs discourage keeping both `uv.lock` and `requirements.txt` in the same workflow. ([Astral Docs][8])

## 9) Extra: packaged projects (libraries)

```bat
:: Initialize a packaged (library) project
uv init mylib --package

:: Or pick a specific build backend
uv init mylib --build-backend hatchling
```

`--package` and `--build-backend` set up a build system so your project can be built/installed. ([Astral Docs][9])

## Handy Windows cmd tips

* Use backslashes for paths in cmd (e.g., `python .\main.py` as shown).
* Manual activation in cmd, if ever required: `.venv\Scripts\activate.bat`. In normal uv usage, `uv run`/`uv add` handle environments for you. ([Astral Docs][6])

## References

* uv installation on Windows and alternatives. ([GitHub][1], [Astral Docs][2])
* uv CLI reference (init, add, run, tool, etc.). ([Astral Docs][3])
* Managing Python versions with uv. ([Astral Docs][4], [PyPI][5])
* Using environments (.venv discovery/prompt). ([Astral Docs][6])
* Using tools and uvx. ([Astral Docs][7])
* Locking/syncing behavior and export guidance. ([Astral Docs][8])

[1]: https://github.com/astral-sh/uv?utm_source=chatgpt.com "GitHub - astral-sh/uv: An extremely fast Python package and project ..."
[2]: https://docs.astral.sh/uv/getting-started/installation/?utm_source=chatgpt.com "Installation | uv - Astral"
[3]: https://docs.astral.sh/uv/reference/cli/?utm_source=chatgpt.com "Commands | uv - Astral"
[4]: https://docs.astral.sh/uv/guides/install-python/?utm_source=chatgpt.com "Installing and managing Python | uv - Astral"
[5]: https://pypi.org/project/uv/?utm_source=chatgpt.com "uv · PyPI"
[6]: https://docs.astral.sh/uv/pip/environments/?utm_source=chatgpt.com "Using environments | uv - Astral"
[7]: https://docs.astral.sh/uv/guides/tools/?utm_source=chatgpt.com "Using tools | uv - Astral"
[8]: https://docs.astral.sh/uv/concepts/projects/sync/ "Locking and syncing | uv"
[9]: https://docs.astral.sh/uv/concepts/projects/config/?utm_source=chatgpt.com "Configuring projects | uv - docs.astral.sh"
