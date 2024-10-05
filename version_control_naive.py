class VersionControlNaive:
    def __init__(self):
        self.revisions = []
    
    def add_revision(self, content):
        if self.revisions:
            last_revision = self.revisions[-1]['content']
            delta = self._calculate_delta(last_revision, content)
            self.revisions.append({'id': len(self.revisions), 'delta': delta, 'content': content})
        else:
            self.revisions.append({'id': 0, 'delta': '', 'content': content})
    
    def get_revision(self, revision_id):
        return self.revisions[revision_id]['content'] if 0 <= revision_id < len(self.revisions) else None
    
    def get_latest_revision(self):
        return self.revisions[-1]['content'] if self.revisions else None
    
    def get_all_revisions(self):
        return [(revision['id'], revision['content']) for revision in self.revisions]
    
    def _calculate_delta(self, old_content, new_content):
        return f"Changes from '{old_content}' to '{new_content}'"
