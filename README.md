# Stands


### gitlab-baseline-generate.py

Script to manager a baseline in the gitlab:
- Find and update issues without milestone
- Build a release note for the baseline
- Move issues from baseline to validating
- Close issue-tasks done in the baseline

### gitlab-milestone-close.py 

Script to manager a release in the gitlab:
- Close issues validated
- Move issues from previous to next milestone

### sqlserver-database-reset.py

Script to reset a target database:
- Execute the script of drop
- Execute the script of structure
- Execute the script of bootstrap
- Execute optional scripts in the database

### x0-lang.py 

Load a lang json (used in ngx-translate) and convert in a testable lang in pattern x0:
- Load the target lang json
- Convert the content
- Dump the x0 lang in a json file
