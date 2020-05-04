# github_api.py
import json
import requests
from collections import Counter
from dateutil.parser import parse

github_user = "thalesbruno"
endpoint = f"https://api.github.com/users/{github_user}/repos"

repos = json.loads(requests.get(endpoint).text)

# print(type(repos))
print(f"{github_user} has {len(repos)} public repos")

dates = [parse(repo['created_at']) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

print(month_counts)
print(weekday_counts)

last_5_repositories = sorted(repos,
                             key=lambda r: r['pushed_at'],
                             reverse=True)[:5]

last_5_repositories_names = [repo['name'] for repo in last_5_repositories]

print("last 5 repositories:")
print(*last_5_repositories_names, sep=', ')

last_5_languages = [repo['language'] for repo in last_5_repositories]
print("last five languages:")
print(*last_5_languages, sep=', ')
