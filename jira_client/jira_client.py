import requests
import argparse
from requests.auth import HTTPBasicAuth
from datetime import datetime

SUCCESS = 200
API_ENDPOINT = '/rest/api/3/search'

class JiraClient:

    def __init__(self, email, api_token, domain):
        self.auth = HTTPBasicAuth(email, api_token)
        self.headers = { "Accept": "application/json", "Content-Type": "application/json" }
        self.base_url = f'https://{domain}'
        
    def search_issues(self, jql_query, max_results = 50, fields='key,summary,status,duedate', status=None, duedate=None):
        conditions = [jql_query]
        if status is not None:
            status_condition = ' OR '.join([f'status="{s}"' for s in status])
            conditions.append(f'({status_condition})')
        if duedate is not None:
            conditions.append(f'duedate <= {duedate}')
        jql_query_final = ' AND '.join(conditions)
        query = { 'jql': jql_query_final, 'maxResults': max_results, 'fields': fields }
        response = requests.get(f'{self.base_url}{API_ENDPOINT}', headers=self.headers, params=query, auth=self.auth)
        if response.status_code == SUCCESS:
            return response.json()['issues']
        else:
            raise Exception(f'failed to search issues: {response.status_code}, {response.text}')

    def sort_by_status(self, issues):
        issues_by_status = {}
        for issue in issues:
            status = issue['fields']['status']['name']
            if status not in issues_by_status:
                issues_by_status[status] = []
            issues_by_status[status].append(issue)
        for status, issues in issues_by_status.items():
            issues.sort(key=lambda x: (x['fields'].get('duedate') or '9999-12-31', x['key']))
        return issues_by_status   

    def print_issues(self, issues_by_status):
        for status, issues in issues_by_status.items():
            print(f'Status: {status} ({len(issues)} issues)\n')
            for issue in issues:
                key = issue['key']
                summary = issue['fields']['summary']
                duedate = issue['fields'].get('duedate') or 'No due date'
                if duedate != 'No due date':
                    duedate_datetime = datetime.strptime(duedate, '%Y-%m-%d')
                    if duedate_datetime.date() < datetime.now().date():
                        duedate = '\033[31m' + duedate + '\033[m'
                print(f'Issue Key: {key}:\n{summary}\nDue: {duedate}\n')

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='JiraClient')
        parser.add_argument('-s', '--status', nargs='+', help='Issue status(es) to filter by', required=False)
        parser.add_argument('-d', '--duedate', help='Filter issues by due date. Use YYYY-MM-DD format.', required=False)
        return parser.parse_args()
    

