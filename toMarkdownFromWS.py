import markdown

class ToMarkdown:
    def __init__(self, ws):
        self.ws = ws

    def to_markdown(self):
        markdown = "|Repository|Branch|Commit Id|Commit Message|Commit Message Body|Commited on (Date)|\n"
        markdown += "|---|---|---|---|---|---|\n"
        for commit in self.ws:
            markdown += f"|{commit.repository}|{commit.branch}|{commit.commit_id}|{commit.message}|{commit.message}|---|\n"
        return markdown    