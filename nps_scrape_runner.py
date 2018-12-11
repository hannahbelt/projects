# open one file and read it as json
# open other call something else and read it as json 
# treat as dixtorionaries

from pprint import pprint
import json
with open('data/all_park_comments.json', 'r') as read_file_comments:
    comments = json.load(read_file_comments)

with open('data/all_park_visitors.json', 'r') as read_file_visitors:
    visitors = json.load(read_file_visitors)

# google merge two dictionaries shared keys python

comments_and_visitors = {}
#print(comments_and_visitors)
for key in visitors.keys():
    park_visitors = visitors.get(key, None)
    #print(park_visitors)
    if park_visitors:
        for year in park_visitors['park_visitors']:
            year['comments'] = []
            #print(year)    
    park_comments = comments.get(key, None)
    #print(park_comments)
    if park_comments:
        comments_and_visitors[key] = park_visitors
        for comment in park_comments['park_comments']:
            comment_year = comment['date'][-4:]
            # print(comment_year)
            # print([c for c in comments_and_visitors[key]['park_visitors']])
            for visitor_year in comments_and_visitors[key]['park_visitors']:
                if visitor_year == comment_year:
                    visitor_year[comments].append(comment)
            # comments_and_visitors[key]['park_visitors'][comment_year]['comments'].append(comment)

pprint(comments_and_visitors)

j = json.dumps(comments_and_visitors, indent=4)
#print(j)
with open('data/comments_and_visitors.json', 'w+') as f:
    print(j, file=f)    