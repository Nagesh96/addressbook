import os
tickets_details = os.environ.get('JIRA_TICKETS')
jira_tickets = tickets_details.split(',')
for issue in jira_tickets:
  print(issue)
