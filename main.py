from github import Github
import re
import sys

# parse sp label
def get_sp(labels):
    for l in labels:
        if(re.match('\d+', l.name)):
            return l.name

g = Github()

for i in g.search_issues(f"repo:rsks/circlecitest is:open label:{sys.argv[1]}"):
    title=i.title
    assignee=i.assignees[0].login
    sp=get_sp(i.labels)
    out = f"{title}, {assignee}, {sp}"
    print(out)


