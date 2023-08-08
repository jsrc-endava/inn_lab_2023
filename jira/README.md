This is a wraper to interact in a simple way with the Jira board.

How to import the jira client
```
from jira_client import JiraClient
```

To initialize the jira client, please do this
```
jiraClient = JiraClient()
```

To get ticket information.
```
singleIssue = jiraClient.get_ticket('VEL-1')
print('{}: {}:{}'.format(singleIssue.key,
                         singleIssue.fields.summary,
                         singleIssue.fields.reporter.displayName))
```

To create a ticket
```
new_issue = jiraClient.get_ticket('VEL', 'My ticket', 'my ticket description', 'Bug')
```

To add a comment in a ticket
```
jiraClient.add_comment('VEL-1', 'This is a comment')
```