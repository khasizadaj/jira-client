from jira_client.jira_client import JiraClient
from config.json_config import JsonConfig

def main():
    config = JsonConfig().config
    jira_client = JiraClient(config['email'], config['api_token'], config['domain'])
    args = jira_client.parse_arguments()
    raw_issues = jira_client.searchIssues(config['base_query'], status=args.status, duedate=args.duedate)
    if raw_issues != None:
        issues_by_status = jira_client.sort_by_status(raw_issues)
        jira_client.printIssues(issues_by_status)
    else:
        print("No issues found.")
    
if __name__ == '__main__':
    main()