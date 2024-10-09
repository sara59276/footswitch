# Foot Switch GUI

## Table of contents
- Author
- Description
- How-to clone the repo
- How to update the requirements.txt
- How to generate the executable

## Author
Sara Wysk

## Description


## How to clone the repo
Firstly, run the following commands:
```
git clone https://github.com/sara59276/FootSwitch.git
cd FootSwitch
pip install virtualenv
virtualenv .venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
Lastly, mark the `src` directory as sources root.

## How to update the requirements.txt
```
.\venv\Scripts\activate
pip freeze > requirements.txt
```
## How to generate the executable
```
pyinstaller.exe --noconsole --onefile --name AIFGenerator .\src\main.py
```
