class VersionControlNaive:
    def __init__(self):
        self.revisions = []

    def add_revision(self, content):
        self.revisions.append(content)
        return len(self.revisions) - 1

    def get_revision(self, rev_id):
        if 0 <= rev_id < len(self.revisions):
            return f"Revision {rev_id}:\n{self.revisions[rev_id]}"
        return "Revision not found."

    def get_latest_revision(self):
        if not self.revisions:
            return "No revisions available."
        return self.get_revision(len(self.revisions) - 1)

    def get_all_revisions(self):
        if not self.revisions:
            return ["No revisions available."]
        return [self.get_revision(rev_id) for rev_id in range(len(self.revisions))]
