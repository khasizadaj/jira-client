import json
import os

class JsonConfig:
    
    def __init__(self, file_path = 'config.json'):
        self.file_path = file_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            try:
                with open(self.file_path, 'r') as config_file:
                    config = json.load(config_file)
            except json.JSONDecodeError:
                print("config file is not valid json")
                return {}
        else:
            print("no config file found - prompting for data")
            config = self.prompt_for_config()
        self.update_config(config)
        return config
    
    def prompt_for_config(self):
        config = {
            'email': input("jira email: "),
            'domain': input("jira domain (example.atlassian.net): "),
            'api_token_path': input("path to your jira API token: "),
            'project': input("jira project key")
        }
        with open(self.file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)
        return config
    
    def update_config(self, config):
        config['base_query'] = f"project = {config.get('project')}"
        try:
            with open(config['api_token_path'], 'r') as file:
                config['api_token'] = file.read().strip()
        except FileNotFoundError:
            print(f"API token file {config['api_token_path']} not found")