<h1 align="center">Chitter</h1>

<p align="center">
In this solo project, I integrated a SQL database in Python using the psycopg package to create a small web application called Chitter.</p>

<p>Chitter is a web application where you can log-in as a user, post messages and view other Chitter users messages.</p>

## Tech stack

**Frontend:**
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">

**Backend:**
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">

## Running the App

To run the application, clone the respository and run "pipenv install". Then, seed the SQL database with the following command:
psql -h 127.0.0.1 chitter_solo_project < seeds/chitter_solo_project.sql.

To access the web app, go to: http://127.0.0.1:5000/login which will take you to the login page.
