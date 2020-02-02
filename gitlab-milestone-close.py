import gitlab
import json
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse

# https://python-gitlab.readthedocs.io/en/stable/api-usage.html
# private token or personal token authentication
gl = gitlab.Gitlab('https://gitlab.com', private_token='GITLAB_TOKEN')

# ------------------------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------------------------

# Get a instance of Project for the project
def get_project():
    project = gl.projects.get('GITLAB_PROJECT')
    return project

# Close validated issues
def close_validated_issues(milestone):
    issues = []
    issues += project.issues.list(labels=['Validated'], state='opened', all=True)

    for issue in issues:
        if issue.milestone and issue.milestone['title'] != milestone:
            issue.notes.create({'body': 'Task completed in ' + issue.milestone['title']})
            issue.state_event = 'close'
            issue.save()

# Get a instance of Milestone for the open milestone
def get_open_milestone(project):
    milestones = project.milestones.list(state='active')
    milestones.sort(key=lambda x: x.id, reverse=False)
    
    current_milestone = milestones[0]
        
    return current_milestone

# Get a instance of Milestone for the current milestone
def get_current_milestone(project):
    milestones = project.milestones.list(state='active')
    milestones.sort(key=lambda x: x.id, reverse=False)
    
    current_milestone = milestones[0]
    for milestone in milestones:
        if datetime.now() < parse(milestone.due_date): 
            current_milestone = milestone
            break
        
    return current_milestone

def set_issues_milestone(issues, milestone_id):
    for issue in issues:
        issue.milestone_id = milestone_id
        issue.save()


# ------------------------------------------------------------------------------------------------
# Executing script
# ------------------------------------------------------------------------------------------------

# Step 0: Clean up terminal
print("")

# Step 1: Load the project
project = get_project()
print("- Project: " + project.name)
print("")

open_milestone = get_open_milestone(project)
print("- Open Milestone: " + open_milestone.title)
print("")

# Step 2: Load the issues in baseline
issues = project.issues.list(labels=['Validated'], state='opened', all=True)
print("- Issues with label 'Validated': " + str(len(issues)))

user_input = input("-- Close the issues validated ? \n-- Type 'yes' to create:")
print("-- You entered: " + user_input)

if user_input.strip().lower() == 'yes':
    user_input = input("-- Type the name of current milestone, issue in the current milestone will no be closed.. \n-- Name: ")
    print("-- You entered: " + user_input)
    close_validated_issues(user_input)
print("")

issues = []
issues = project.issues.list(milestone=open_milestone.title, state='opened', all=True)
print("- Issues unstart/ongoing in the Open Milestone: " + str(len(issues)))
print("")

current_milestone = get_current_milestone(project)
print("- Current Milestone: " + current_milestone.title)
print("")

user_input = input("-- Move the issues to the Current Milestone ? \n-- Type 'yes' to move:")
print("-- You entered: " + user_input)

if user_input.strip().lower() == 'yes':
    set_issues_milestone(issues, current_milestone.id)
    print("")

print("")

print("..ciao!")
