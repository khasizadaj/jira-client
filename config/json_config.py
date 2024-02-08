import json
import os

class JsonConfig:
    
    def __init__(self, file_path = 'config.json'):
        self.config = self.getConfig(file_path)

    def getConfig(self, file_path):
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as config_file:
                config = json.load(config_file)
        else:
            print("no config file found - prompting for setup")
            email = input("jira email: ")
            domain = input("jira domain (example.atlassian.net): ")
            api_token_path = input("path to your api token: ")
            project = input("jira project key: ")
            
            config = {
                'email': email,
                'domain': domain,
                'api_token_path': api_token_path,
                'project': project
            }
            with open(file_path, 'w') as config_file:
                json.dump(config, config_file, indent = 4)
        config['email'] = config.get('email')
        config['domain'] = config.get('domain')
        config['base_query'] = 'project = ' + config.get('project')
        with open(config.get('api_token_path'), 'r') as file:
            config['api_token'] = file.read().strip()
        return config