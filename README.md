# Automation Framework with Playwright and pytest

## Manual steps:
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
