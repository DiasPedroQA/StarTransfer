import os

def is_valid_path(path):
    if os.path.exists(path):
        return f"The path '{path}' is valid and exists."
    else:
        return f"The path '{path}' is not a valid path or does not exist."
