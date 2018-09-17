import requests
import os
import shutil

USER = 'mmarszal7'
OUTPUT = 'github_repos'

response = requests.get('https://api.github.com/users/' + USER + '/repos').json()
repos = list(map(lambda r: r['name'], response))

for repo in repos:
	os.system('git clone https://github.com/{0}/{1} {2}/{1}'.format(USER, repo, OUTPUT))

shutil.make_archive(OUTPUT, 'zip', OUTPUT)
