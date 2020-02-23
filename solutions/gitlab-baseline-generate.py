import gitlab

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

# Get a instance of Milestone for the current milestone
def get_current_milestone(project):
    milestones = project.milestones.list(state='active')
    milestones.sort(key=lambda x: x.id, reverse=False)
    return milestones[0]

# Get a instance of Tag for the current project
def get_current_baseline(project):
    tags = project.tags.list()
    return tags[0]

# Get a list of issue without milestone
def get_issues_missing_milestone(project):
    issues = project.issues.list(milestone="none", state='opened')
    return issues

# Update all issue without mislestone
def set_milestone_in_issues(issues):
    for issue in issues:
        editable_issue = project.issues.get(issue.iid, lazy=True)
        editable_issue.milestone_id = milestone.id
        editable_issue.save()

# Update the description of issue
def update_issues(issue, baseline):
    description = issue.description

    if not description:
        description = ''

    contains_information = "Additional information" in description
    if (contains_information == False):
        description = description + "\n\n**Additional information**"

    contains_version = "* Baselines:" in description
    if (contains_version == False):
        description = description + "\n* Baselines:"

    issue.description = description + "\n  * " + baseline

# Print the release note for the baseline
def build_release_note():
    issues = project.issues.list(labels=['Baselined'], state='opened', all=True)
    bugs = []
    tasks = []
    others = []
    for issue in issues:
        if 'Bug' in issue.labels:
            bugs.append(issue)
        elif 'Task' in issue.labels:
            tasks.append(issue)
        else:
            others.append(issue)
    print("")
    text1 = build_issue_list("Bugs:", bugs)
    text2 = build_issue_list("Tasks:", tasks)
    text3 = build_issue_list("Others:", others)
    return "\n" + text1 + "\n" + text2 + "\n" + text3

# Print issues link
def build_issue_list(title, issues):
    text = ''
    text += title
    for issue in issues:
        link = "\n* [" + issue.title + "](" + issue.web_url + ")"
        text += link
    text += '\n'
    return text

# Move to validating
def move_to_validating(milestone):
    issues = []
    issues += project.issues.list(labels=['Baselined'], state='opened', all=True)

    for issue in issues:
        labels = []
        if 'Bug' in issue.labels or 'Improvement' in issue.labels:
            for label in issue.labels:
                if label != 'Baselined':
                   labels.append(label)
            labels.append('Validating')
            issue.labels = labels
            issue.save()
        else:
            issue.notes.create({'body': 'Task completed in: ' + baseline.name})
            issue.state_event = 'close'
            issue.save()

# ------------------------------------------------------------------------------------------------
# Executing script
# ------------------------------------------------------------------------------------------------

# Step 0: Clean up terminal
print("")

# Step 1: Load the project
project = get_project()
print("- Project:", project.name, "\n")

# Step 2: Load the milestone
milestone = get_current_milestone(project)
print("- Current milestone:", milestone.title, "\n")

# Step 3: Load issues without milestone
issues = get_issues_missing_milestone(project)
print("- Issues without milestone:", len(issues))

user_input = input("-- Update issue without milestone? \n-- Type 'yes' to update:\n")
print("-- You entered:", user_input, "\n")

# Step 4: Update issues without milestone
if user_input.strip().lower() == 'yes':
    issues = project.issues.list(milestone="none", state='opened')
    set_milestone_in_issues(issues)
    print("-- Issues updated!")
print("")

# Step 5: Load the baseline
baseline = get_current_baseline(project)
print("- Current baseline:", baseline.name)
print("")

tag = project.tags.get(baseline.name)

# Step 6: Load the issues in baseline
issues = project.issues.list(labels=['Baselined'], state='opened', all=True)
print("- Issue with label 'Baselined':", len(issues))

user_input = input("-- Create and set a release note for the tag(Baseline)? \n-- Type 'yes' to create:")
print("-- You entered:", user_input)

if user_input.strip().lower() == 'yes':
    release_note = build_release_note()
    tag.set_release_description(release_note)
print("")

# Step 7: Update the description of issues in baseline
user_input = input("-- Update the description for the issues in the baseline? \n-- Type 'yes' to update:")
print("-- You entered:", user_input)

if user_input.strip().lower() == 'yes':
    print("     Updating the description of issues...")
    for issue in issues:
        update_issues(issue, baseline.name)
        issue.save()
    print("     ...issues updated!")
print("")

# Step 8: Load the issues in baseline
issues = project.issues.list(labels=['Baselined'], state='opened', all=True)
print("- Issue with label 'Baselined':", len(issues))
print("-- Move the Bugs and Improvements from 'Baselined' to 'Validating' ? ")
print("   -- Task/Dev Team will be closed")

user_input = input("-- Type 'yes' to move:")
print("-- You entered:", user_input)

if user_input.strip().lower() == 'yes':
    move_to_validating(user_input)

print("")
print("..ciao!")
