# Pull Requests Parser API

## Features

- [x] Stores user request in database with field 'github_link'
- [x] Validates the github_link
- [x] Requests html for a given github link and stores the html in the database in userrequestresult table
- [x] Parses pullrequests data from the html and stores each open pullrequest in the database
- [x] From the database pullrequests are return to a user
- [x] Tests for pullrequest view and github link validation
- [x] Swagger docs


### How to run locally

From project root directory run `docker-compose build`. Then run `docker-compose up`. In case you do not have `docker` and `docker-compose`, install them on your machine and try again.

### Migrations
Go inside the container: `docker exec -it reviroio bash`. Now that you are inside the container run the commands: `./manage.py makemigrations` and `./manage.py migrate`

## Testing
Go inside the container: `docker exec -it reviroio bash`. Then, run the command: `./manage.py test`

## Description
For parsing libraries were used: BeautifulSoup - to tweak html, requests - to get html from a given link
