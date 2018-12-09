# open one file and read it as json
# open other call something else and read it as json 
# treat as dixtorionaries
import json
with open('data/all_park_comments.json', 'r') as read_file_comments:
    comments = json.load(read_file_comments)

with open('data/all_park_visitors.json', 'r') as read_file_visitors:
    visitors = json.load(read_file_visitors)

# google merge two dictionaries shared keys python

comments_and_visitors = {}
for key in visitors.keys():
    park_visitors = visitors.get(key, None)
    if park_visitors:
        for year in park_visitors:
            year['comments'] = []
        park_comments = comments.get(key['park_comments'], None)
        if park_comments:
            comments_and_visitors[key] = park_visitors
            for comment in park_comments:
                comment_year = comment['date'][-4:]
                comments_and_visitors[key][park_visitors][comment_year]['comments'].append(comment)

j = json.dumps(comments_and_visitors, indent=4)
#print(j)
with open('data/comments_and_visitors.json', 'w+') as f:
    print(j, file=f)    
    
        # add to full dict for ID to new dict
