# jira-client

_work in progress - fetch and sort issue status infos from jira project_

## Usage:

### Example
```python
from jira_client import JiraClient, readConfig

def main():
    email = 'you@domain.com'
    domain = 'jira-domain.atlassian.net'
    with open('path/to/your/api-token', 'r')as file:
        api_token = file.read().strip()
    jira_client = JiraClient(email, api_token, domain)
    args = jira_client.parseArguments()
    base_jql_query = 'project = <your-project-name>'
    raw_issues = jira_client.searchIssues(base_jql_query, status = args.status, duedate = args.duedate)
    if raw_issues != None:
        issues_by_status = jira_client.sortByStatus(raw_issues)
        jira_client.printIssues(issues_by_status)
    else:
        print("No issues found.")
    
if __name__ == '__main__':
    main()
```