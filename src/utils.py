import os

def ensure_dir(directory):
    """Ensure a directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)
