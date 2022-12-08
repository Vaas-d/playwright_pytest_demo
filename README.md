# Automation Framework with Playwright and pytest

## Manual steps:

Basic playwright + pytest testing framework. Framework displays how to test different UI elements
and scenarios utilising https://demoqa.com/ as a testing sandbox.

Framework utilises functionality of the Allure reporter. Reports are stored and displayed via GitHub Pages.
Also, there is an integrated Slack notification when GitHub Actions runs. 
### 1. Install environment:
```
  python -m pip install --upgrade pip
  pip install pipenv
  pipenv install --system
  playwright install chromium
```

### 2. Run playwright tests:
```
pytest
```

### 3. Generate allure report:
```
allure serve reports
```
