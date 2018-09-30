# python imports
import json
# external imports
import requests
from bs4 import BeautifulSoup



#ids
nat_park_ids = [
    'HAFE',
    'BLUE',
    'AFBG',
    'GETT',
    'YOSE',
    'WHIS',
    'GWCA'
]

#url components
url_stub = 'https://irma.nps.gov'

nps_uri = '/Stats/MvcReportViewer.aspx?_id=6d4c57ec-773a-4be8-a7d7-4410daaa91ad&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fMonthly+Visitation+Comments+By+Park&_39=880px&Park='

def build_url_list():
# main loop
    data_dicts = {}
    for park in nat_park_ids:
        full_url = f'{url_stub}{nps_uri}{park}'
        #print(full_url)
        # build url
        data_dicts.append(full_url)

# def get
def get_page_content(full_url):
    response = requests.get(full_url)
    html = response.content

def parse_html(html):
    #print(html)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', attrs={'cols':'2'})
   # print(table)
    return table

    
    #extract
def extract_data(html):
    # per-page loop
    list_of_rows = []
    for row in table.findAll('tr'):
        #print(row)
        list_of_cells = []
        #loop through rows
        for cell in row.findAll('div'):
            list_of_cells.append(cell.text.strip())

        #print(list_of_cells)
        list_of_rows.append(list_of_cells)
    return list_of_rows

    #print(list_of_rows)

    #jsonify
    #build dicts
    data_dicts[park]= {}
    data_dicts[park]['park_comments'] = []
    for row in list_of_rows:
        #print(row)
        #break
        if len(row) == 2:
            comment = {}
            comment['date']= row[0]
            comment['text']= row[1]
            comment['url']= full_url

           # print(comment['date'])
            data_dicts[park]['park_comments'].append(comment)
    #print(data_dicts[park])

    # loop through rowsto structure data


#write
def write_file(data, row_names, file_location):
    j = json.dumps(data_dicts, sort_keys=True, indent=4)
    #print(j)
    with open('data/park_comments.json', 'w+') as f:
        print(j, file=f)

# do everything together
def scrape_park_comments(full_url, filename, row_names):
    content = get_page_content(full_url)
    formatted_html = parse_html(content)
    data = extract_data(formatted_html)
    write_file(data, row_names, filename)

if __name__== '__main__':
    nat_park_ids = '/Stats/MvcReportViewer.aspx?_id=6d4c57ec-773a-4be8-a7d7-4410daaa91ad&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fMonthly+Visitation+Comments+By+Park&_39=880px&Park='
    filename = 'data/park_comments.json'
    row_names = [
        'date', 'text', 'url'
    ]
    #url components
    url_stub = 'https://irma.nps.gov'

    nps_uri = '/Stats/MvcReportViewer.aspx?_id=6d4c57ec-773a-4be8-a7d7-4410daaa91ad&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fMonthly+Visitation+Comments+By+Park&_39=880px&Park='
    scrape_park_comments(full_url, filename, row_names)

  