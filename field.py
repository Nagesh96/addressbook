import os
tickets_details = os.environ.get('JIRA_TICKETS')
field_value = os.environ.get('FIELD_VALUE')
print(f'Artifact URL:', field_value)
jira_tickets = tickets_details.split(',')
for issue in jira_tickets:
  print(f'Jira_Tickets:', issue)
