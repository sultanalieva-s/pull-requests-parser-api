# Pull Requests Parser API
Parses open pull requests for a given github repo link.
### How to run locally

From project root directory run `docker-compose build`. Then run `docker-compose up`. In case you do not have `docker` and `docker-compose`, install them on your machine and try again.

### Migrations
Go inside the container: `docker exec -it reviroio bash`. Now that you are inside the container run the commands: `./manage.py makemigrations` and `./manage.py migrate`

## Testing
Go inside the container: `docker exec -it reviroio bash`. Then, run the command: `./manage.py test`

## Description
For parsing libraries were used: BeautifulSoup - to tweak html, requests - to get html from a given link
