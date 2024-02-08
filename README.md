# jira-client

_work in progress - fetch and sort issue status infos from jira project_

## usage


### 1. clone and cd into repo


```bash
git clone git@github.com:winstonallo/jira-client.git && cd jira-client
```

### 2. configurate json file

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
python3 main.py

options:
    --help      show this help message
    --status    issue status(es) to filter by
    --duedate   filter issues by du date (YYYY-MM-DD)
```
