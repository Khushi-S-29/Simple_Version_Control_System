class VersionControlOptimized:
    def __init__(self):
        self.revisions = {}
        self.latest_id = -1

    def add_revision(self, content):
        self.latest_id += 1
        self.revisions[self.latest_id] = content
        return self.latest_id

    def get_revision(self, rev_id):
        return f"Revision {rev_id}:\n{self.revisions.get(rev_id, 'Revision not found.')}"

    def get_latest_revision(self):
        if self.latest_id == -1:
            return "No revisions available."
        return self.get_revision(self.latest_id)

    def get_all_revisions(self):
        if not self.revisions:
            return ["No revisions available."]
        return [self.get_revision(rev_id) for rev_id in sorted(self.revisions.keys())]
