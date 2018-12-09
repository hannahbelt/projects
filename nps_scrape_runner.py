# open one file and read it as json
# open other call something else and read it as json 
# treat as dixtorionaries
import json
with open('all_park_comments', 'r') as read_file_comments:
    comments = json.load(read_file_comments)

with open('all_park_visitors', 'r') as read_file_visitors:
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

j = json.dumps(data_dicts_visitors, indent=4)
#print(j)
with open('data/comments_and_visitors.json', 'w+') as f:
    print(j, file=f)    
    
        # add to full dict for ID to new dict

#  Loop through the visitors' keys

# -- For each key in visitors, check the comments dictionary to see if there are any comments for that park id

# -- If there aren't, skip it and keep going. Nothing to do

# -- If there are, add the full dictionary for that park id to the new dictionary we're creating

# -- Slice off the year from the comment date to determine which year's visitors data is relevant  -- so depending on the structure you have, you may need to loop through those comments to check each date

# -- In the new dictionary we're creating, add a 'comments' key to that year's data -- so keys will be like 'January', 'February', [... snip ...] 'Total', and 'comments' -- with a value of an empty dictionary

# -- Set keys for that 'comments' dictionary to another dictionary with keys of 'date' and 'comment'