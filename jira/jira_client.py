import os
from dotenv import load_dotenv
from jira import JIRA

class JiraClient:
    """Jira client for the Noah project, based on https://jira.readthedocs.io/api.html#jira.client.JIRA.issue"""

    def __init__(self):
        load_dotenv()
        server = os.getenv('JIRA_SERVER')
        user = os.getenv('USER')
        apiToken = os.getenv('TOKEN')

        jiraOptions = {'server': server}
  
        # Get a JIRA client instance, Pass Authentication parameters and  Server name.
        # token can be obtained in https://id.atlassian.com/manage-profile/security/api-tokens
        self.jira = JIRA(options = jiraOptions, basic_auth=(user, apiToken))

    def get_projects(self):
        projects = self.jira.projects()
        return projects

    #  Get ticket by Key.
    def get_ticket(self, key):
        singleIssue = self.jira.issue(key)
        print('{}: {}:{}'.format(singleIssue.key,
                            singleIssue.fields.summary,
                            singleIssue.fields.reporter.displayName))
        return singleIssue

    def get_tickets_by_project(self, prj):
        return self.jira.search_issues('project=' + prj)

    def create_ticket(self, prj, summary, description, type):
        new_issue = self.jira.create_issue(project=prj, summary=summary, description=description, issuetype={'name': type})
        return new_issue

    def add_comment(self, key, text):
        self.jira.add_comment(key, text)   
      