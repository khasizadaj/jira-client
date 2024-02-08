import requests
from requests.auth import HTTPBasicAuth

SUCCESS = 200

class JiraClient:
    
    
    def __init__(self, email, api_token, domain):
        self.auth = HTTPBasicAuth(email, api_token)
        self.headers = { "Accept": "application/json", "Content-Type": "application/json" }
        self.base_url = f'https://{domain}'
        
    def searchIssues(self, jql_query, max_results = 50, fields = 'key,summary,status'):
        api_endpoint = '/rest/api/3/search'
        query = { 'jql': jql_query, 'maxResults': max_results, 'fields': fields }
        response = requests.get(self.base_url + api_endpoint, headers = self.headers, params = query, auth = self.auth)
        if response.status_code == SUCCESS:
            return response.json()['issues']
        else:
            print('Failed to search issues:', response.status_code, response.text)         
            
    def sortByStatus(self, issues):
        issues_by_status = {}
        for issue in issues:
            status = issue['fields']['status']['name']
            if status not in issues_by_status:
                issues_by_status[status] = []
            issues_by_status[status].append(issue)
        return issues_by_status   

def printIssues(issues_by_status):
    for status, issues in issues_by_status.items():
        print(f'\nStatus: {status} ({len(issues)} issues)')
        for issue in issues:
            key = issue['key']
            summary = issue['fields']['summary']
            print(f' {key}: {summary}')

