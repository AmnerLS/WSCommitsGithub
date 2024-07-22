import bs4
import requests
from Commit import Commit
from itertools import zip_longest

class WSCommits:
    def __init__(self, base_url):
        self.base_url = base_url
        self.commits_message = []
        self.commits_id = []
        self.commits_date = []
        self.branch_name= base_url.split('/')[-2]
    
    def fetch_commits(self):
        res = requests.get(self.base_url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        commits_array= []
        commits2 = soup.select('div.ml-5, div.flex-column')

        for commit in commits2:
            for item in commit.select('li span.Text-sc-17v1xeu-0 > a.color-fg-default'):
                self.commits_message.append(item['title'].split('\n')[0].strip())
            for item in commit.select('span.Button-label.color-fg-muted'):
                self.commits_id.append(item.text.strip())
            for item in commit.select('div.Timeline__TimelineBody-sc-1nkzbnu-2 > h3.cgQnMS'):
                self.commits_date.append(item.text.strip())
        
        for n, (message, commit_id) in enumerate(zip(self.commits_message, self.commits_id), start=1):
            print(f"|{self.base_url}|{self.branch_name}|{commit_id}|{message}|{message}|---|\n")
            commits_array.append(Commit(self.base_url, self.branch_name, commit_id, message))
        
        

        return commits_array

    def display_commits(self, commits_array):
        for n, commit in enumerate(commits_array, start=1):
            print(f"Commit {n}: {commit}")






    
    


