import re

# Helper function to sanitize session name
def sanitize(name):
    return re.sub(r'[^a-zA-Z0-9_]', '', name)
