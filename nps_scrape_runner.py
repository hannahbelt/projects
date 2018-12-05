# open one file and read it as json
# open other call something else and read it as json 
# treat as dixtorionaries
import json
with open('all_park_comments', 'r') as read_file_comments:
    comments = json.load(read_file_comments)

with open('all_park_visitors', 'r') as read_file_visitors:
    visitors = json.load(read_file_visitors)

# google merge two dictionaries shared keys python