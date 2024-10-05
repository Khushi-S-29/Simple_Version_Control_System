# Simple Version Control System

This project implements a basic version control system for managing document revisions, similar to collaborative tools like Google Docs.

## Features

- **Add Revision**: Add a new revision of a document.
- **Get Revision**: Retrieve a specific revision by its identifier.
- **Get Latest Revision**: Access the most recent revision.
- **Get All Revisions**: List all revisions in order.

## Implementation

The repository includes two versions of the version control system:

1. **Naive Implementation**: Uses a list to store revisions, resulting in O(n) time complexity for retrieval.
2. **Optimized Implementation**: Utilizes a hash map for O(1) retrieval, improving performance.