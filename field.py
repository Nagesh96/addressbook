import os
tickets_details = os.environ.get('JIRA_TICKETS')
value = os.environ.get('artifacturl')
print(f'Artifact URL:', value)
jira_tickets = tickets_details.split(',')
for issue in jira_tickets:
  print(f'Jira_Tickets:', issue)
