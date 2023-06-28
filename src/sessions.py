import os
import re
from ruamel.yaml import YAML
import questionary
from src.helpers import sanitize

# Session Class
class Session:
    def __init__(self, name, company_target=None, search_query=None):
        self.name = name
        self.company_target = company_target
        self.search_query = search_query
        self.yaml = YAML()

    def save(self):
        filename = f"sessions/{sanitize(self.name)}.yaml"
        with open(filename, 'w') as file:
            self.yaml.dump({
                'session_name': self.name, 
                'company_target': self.company_target,
                'search_query': self.search_query
            }, file)

    @staticmethod
    def load(name):
        filename = f"sessions/{sanitize(name)}.yaml"
        yaml = YAML()
        with open(filename, 'r') as file:
            data = yaml.load(file)
            return Session(data['session_name'], data.get('company_target'), data.get('search_query'))
        
    @staticmethod
    def create_or_resume():
        # Create sessions directory if not exist
        if not os.path.exists('sessions'):
            os.makedirs('sessions')

        # Ask user to create or resume a session
        action = questionary.select(
            "Do you want to:",
            choices=[
                'Create a new session',
                'Resume an existing one'
            ]).ask()

        if action == 'Create a new session':
            session_name = questionary.text("Enter a name for the new session:").ask()
            company_target = questionary.text("Enter the target company:").ask()
            search_query = questionary.text("Enter the search query for the title of the person:").ask()

            session = Session(session_name, company_target, search_query)
            session.save()
            return session

        elif action == 'Resume an existing one':
            # List existing sessions
            session_files = [f[:-5] for f in os.listdir('sessions') if f.endswith('.yaml')]
            session_name = questionary.select(
                "Choose a session to resume:",
                choices=session_files).ask()

            session = Session.load(session_name)
            print(f"Resumed session: {session.name}")
            return session

        else:
            print("Invalid action.")
            return None