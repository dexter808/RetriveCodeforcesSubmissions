import requests
from bs4 import BeautifulSoup as bs
import json
import os
import sys
import re

def get_sub_and_save(url,file_path):
	x=requests.get(url)
	sp=bs(x.text,"html.parser")
	os.makedirs(os.path.dirname(file_path),exist_ok=True)
	with open(file_path,"w+") as f:
		f.write(sp.find_all("pre")[0].text)
		f.write("\n")
	print("Done")

def check_if_present(subs,stri):
	check_regex=re.compile(subs,flags=re.IGNORECASE)
	if check_regex.search(stri)==None:
		return False
	else:
		return True
		
def return_extension(prog_lang):
	prog_extensions={"c\+\+":".cpp","c":".c","java":".java","python":".py","perl":".pl","javascript":".js"}
	for pg in prog_extensions:
		if check_if_present(pg,prog_lang):
			return prog_extensions[pg]
	return "."+prog_lang


username=str(sys.argv[1])
submissions=requests.get('https://codeforces.com/api/user.status?handle='+username+'&from=1&count=10')
submissions_json=json.loads(submissions.text)
for sub in submissions_json['result']:
	if sub['verdict'] == 'OK' and 'contestId' in sub.keys():
		problem_name=sub['problem']['name']
		extension=return_extension(sub['programmingLanguage'])
		get_sub_and_save('https://codeforces.com/contest/'+str(sub['contestId'])+'/submission/'+str(sub['id']),problem_name+'/solution_'+str(sub['id'])+extension)
