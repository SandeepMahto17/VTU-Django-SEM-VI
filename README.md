
# DJANGO LAB PROGRAMS VTU

The repo contains all the programs of Django(Fullstack Development) for VTU 6th semester (21CS62).

#Building and Running Locally

Below are the steps for running the programs Locally




## Requirements
Python

## Installation

Install django

```bash
  pip install django
```
```bash
  cd ..
```

Create and Activate a Virtual Environment
```bash
  python -m venv venv
 .\venv\Scripts\activate
```
```bash
  cd django-project
```

Install Dependencies

```bash
  python install -r requirements.text
```
Set Up the Database
```bash
  python manage.py migrate
```
Create super user(optional)

```bash
  python manage.py createsuperuser
```
Run server
```bash
  python manage.run server
```