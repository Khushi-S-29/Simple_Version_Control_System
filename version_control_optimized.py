class VersionControlOptimized:
    def __init__(self):
        self.revisions = {}
        self.latest_id = -1
    
    def add_revision(self, content):
        if self.latest_id >= 0:
            last_revision = self.revisions[self.latest_id]['content']
            delta = self._calculate_delta(last_revision, content)
            self.latest_id += 1
            self.revisions[self.latest_id] = {'delta': delta, 'content': content}
        else:
            self.latest_id = 0
            self.revisions[self.latest_id] = {'delta': '', 'content': content}
    
    def get_revision(self, revision_id):
        return self.revisions.get(revision_id, {}).get('content', None)
    
    def get_latest_revision(self):
        return self.revisions[self.latest_id]['content'] if self.latest_id >= 0 else None
    
    def get_all_revisions(self):
        return [(revision_id, rev['content']) for revision_id, rev in self.revisions.items()]
    
    def _calculate_delta(self, old_content, new_content):
        return f"Changes from '{old_content}' to '{new_content}'"
