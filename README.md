# My mad2 project demo


Steps to run the project

## Virtual environment

to create virtual environment run this
```bash
python -m venv venv
```

how to activate
```bash
.\venv\Scripts\activate # windows
source .\venv\bin\activate # linux and mac
```

how to install requirements for python backend
```bash
pip install -r requirements
```

## Run Python Backend

```bash
python app.py
```

## Run Vue Frontend

```bash
cd frontend
npm install # installs node modules (requried packages for frontend app)
npm run dev # run the FE server
```

## Run Celery App

### Worker

```bash
celery -A celery_app worker --loglevel=info # ONLY WINDOWS USERS ADD "--pool=solo"
```

### Beat

```bash
celery -A celery_app beat --loglevel=info
```