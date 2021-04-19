# Installation

Use git to clone this repository

```bash
git clone https://github.com/ghazimuharam/self-learning-blank-space.git
```

## Prerequisite

Make sure you have python 3.7 installed on your machine

```bash
> python --version
Python 3.7.10
```

To run the script in this repository, you need to install the prerequisite library from requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

Before running the main program, you need to configure `JSON_DIR` and `JSON_OUTPUT` variable on `main.py`

```python
# Movies data directory
JSON_DIR = 'path/to/dir'

# Location to output json file
JSON_OUTPUT = 'path/filename.json'
```

Run the extraction process by using the command below

```bash
python main.py
```
