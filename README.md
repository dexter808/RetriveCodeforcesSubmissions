# RetriveCodeforcesSubmissions
This repo helps in retrieving codeforces submissions of a specific user.

## What it does?
It takes a username as an input and saves the codeforcces submissions in the subfolders.
Folders with problem names will be created in the 'current directory', with each folder containing submissions in the format :
`solution_<submission_id>.<extension>`

## Requirements:
1. BeautifulSoup

## How to use?
1. CD into the folder where you want to save the submissions.

` cd my-submmissions`

2. Now run the script using python3

`python3 <Path to SubmissionRetrival.py> <username>`

### Note:
It only retrives the submissions to problems which have been used in some contests and it uses web scrapping to retrive the content and thus is prone to errors when any dependency or layout of the website itself changes.
