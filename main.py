from version_control_naive import VersionControlNaive
from version_control_optimized import VersionControlOptimized

def main():
    print("Testing Naive Version Control")
    naive_vcs = VersionControlNaive()
    naive_vcs.add_revision("First revision content")
    naive_vcs.add_revision("Second revision content")
    print(naive_vcs.get_latest_revision())
    print(naive_vcs.get_revision(0))
    print(naive_vcs.get_all_revisions())
    
    print("\nTesting Optimized Version Control")
    optimized_vcs = VersionControlOptimized()
    optimized_vcs.add_revision("First revision content")
    optimized_vcs.add_revision("Second revision content")
    print(optimized_vcs.get_latest_revision())
    print(optimized_vcs.get_revision(0))
    print(optimized_vcs.get_all_revisions())

if __name__ == '__main__':
    main()
