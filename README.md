# jira-client

_work in progress - fetch and sort issue status infos from jira project_


## usage

### 1. clone and cd into repo

```bash
git clone git@github.com:winstonallo/jira-client.git && cd jira-client
```

### 2. create virtual environment and install requirements

```bash
# create virtual env.
python -m venv .venv

# actiavte virtual env.
source .venv/bin/activate

# install requirements
pip install -r requirements.txt
```


### 2. configurate json file

_if no config.json file is found, you will get prompted for the necessary data_

```bash
touch config.json
```

```json
{
    "email": "you@foo.com",
    "domain": "your-domain.atlassian.net",
    "api_token_path": "path/to/your/api-token",
    "project": "JIRA PROJECT KEY"
}

```


### 3. run
```bash
python main.py

options:
    --help      show this help message
    --status    issue status(es) to filter by
    --duedate   filter issues by du date (YYYY-MM-DD)
```
