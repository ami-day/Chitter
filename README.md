<h1 align="center">Chitter</h1>

<p align="center>
In this solo project, I integrated a SQL database in Python using the psycopg package to create a small web application called Chitter. Chitter is a web application where you can log-in as a user, post messages and view other Chitter users messages. I implemented this project using Flask, Pytest, HTML, CSS and Jinja templates.</p>

# Running the app
To run the application, clone the respository and run "pipenv install". Then, seed the SQL database with the following command:
psql -h 127.0.0.1 chitter_solo_project < seeds/chitter_solo_project.sql.

To access the web app, go to: http://127.0.0.1:5000/login which will take you to the login page.
