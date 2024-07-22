class Commit:
    def __init__(self, repository, branch, commit_id, message):
        self.commit_id = commit_id
        self.repository = repository
        self.message = message
        self.branch = branch

    def __str__(self):
        return f"|{self.repository}|{self.branch}|{self.commit_id}|{self.message}|{self.message}|---|\n"