<H1>FastJOB</H1>
Description

## Project requirements

* python >= 3.10
* PostgreSQL >= 15

<hr>

## Development Environment Set Up

### Start project directly on your host

#### Virtual Environment Set up

```bash
  python -m venv <path_to_env>
  source <path_to_env>/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

### to run server run command below

```
uvicorn main:app --reload --port 8080
``` 

```Note: You can Run Server On Any Port 8080 Is An Example```

<hr>

* ORM : SQLAlchemy


* DB : SQLite
* Or
* DB : PostgreSQL

```Note: You Can Change DB in sessions.py```

