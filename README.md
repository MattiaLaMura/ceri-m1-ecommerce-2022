# S-E06-0632: Projet e-commerce

To run the project, you need to create a **.env** file in the *root* folder and copy the following lines:
```text
USER=<DB User>
PASSWORD=<DB Password>
HOST=<DB Host>
PORT=<DB Port>
DBNAME=<DB Name>
SECRET_KEY=<random key for auth service>
```
This file will be used to stock the environment variables and pass them to the ```docker run```.

To build and run it, you just need to execute the following commands:
```shell
# OPTIONAL : this is just to run a test database 

docker run -d -p 3306:3306 --name db -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=db mysql



docker build -t backend -f backend.Dockerfile . && docker run -d --name backend --env-file .env -p 8000:22 backend



# CHANGE THE BACKEND URL IN THE SOURCE CODE : 'http://localhost:8000' or the deployed final url

docker build -t frontend -f frontend.Dockerfile . && docker run -d --name frontend -p 8001:80 frontend
```
The **Backend** is now accessible on the following *url*:
> localhost:8000

The **FrontEnd** is now accessible on the following **url**:
> localhost:8001

## Dream team

|             |            |
| ----------- | ---------- |
| Nom         | Baloma™    |
| Identifiant | purplepig  | 🐷

<br>

### Staff


| Role                      | Membre          |
| ------------------------- | --------------- |
| Backend engineer          | Lorenzo LA MURA |
| Frontend engineer         | Bastien MEFFRE  |
| Site reliability engineer | Mattia LA MURA  |
