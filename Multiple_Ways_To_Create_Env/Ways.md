# 🐍 Ways to Create a Virtual Environment in Python

There are 3 different ways to create a virtual environment for Python projects:

---

## 1. ✅ Using `python` Command (Built-in `venv` Module)

```bash
# Create a virtual environment
python -m venv folder_name

# Activate the environment (Windows)
folder_name\Scripts\activate
```


## 2. ✅ Using `virtuslenv` command
```bash

# Create a virtual environment using virtualenv
virtualenv -p python3 virtual_env

# Activate the enviornment (Windows)
virtual_env\Scripts\activate
```


## 3. ✅  Using `Conda` Command in "Command prompt"

```bash

# Make sure that virtual environment is active

# Create a virtual environment using conda
conda create -p ./venv python==3.10 -y

# Activate the environment
conda activate ./venv

```