# jira-progress-tracker


## Usage:
```python

from jira_client import JiraClient, printIssues

if __name__ == '__main__':
    email = 'your-email@domain.com'
    domain = 'https://your-jira-domain.atlassian.net'
    token_path = 'path/to/your/token'
    try:
        with open(token_path, 'r') as file:
            api_token = file.read().strip()
    except FileNotFoundError:
        print(f"Could not find file {token_path}.")
        exit(1)

    # Create an instance of the JiraClient
    jira_client = JiraClient(email, api_token, domain)

    # Define the JQL Query and fetch corresponding issues
    jql_query = 'project = <your-project-name> AND status in ("To Do", "In Progress", "Done")'
    raw_issues = jira_client.searchIssues(jql_query)

    # Sort issues by status
    issues_by_status = jira_client.sortByStatus(raw_issues)
    jira_client.printIssues(issues_by_status)
```