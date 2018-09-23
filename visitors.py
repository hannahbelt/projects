

# python imports
import csv
# external imports
import requests
from bs4 import BeautifulSoup

# get
url = 'https://irma.nps.gov/Stats/MvcReportViewer.aspx?_id=6e6a7e3e-f0b1-4104-9c2d-6c1869661672&_m=Remote&_r=%2fNPS.Stats.Reports%2fNational+Reports%2fAnnual+Park+Ranking+Report+(1979+-+Last+Calendar+Year)&_39=880px'
response = requests.get(url)
html = response.content
#print(response.content)

# parse
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', attrs={'cols':'4'})
#print(table)


# extract
#def extract_data(html):
    # a place to keep all the rows of data to hand off to whatever else will need to use it
list_of_rows = []
    # go through each row in the table
for row in table.findAll('tr'):
        # prepare a list of the cells in the table
    list_of_cells = []
    if row.find('div') is not None:
        for cell in row.findAll('div'):
            # add it to the list of cells
            list_of_cells.append(cell.text)
print(list_of_cells)      

        # if this isn't empty
        #if list_of_cells:
            # make sure we get only the data we want:
            # print(list_of_cells)
            # eh, that last thing in the list is a little iffy, let's access it by index:
            # print(list_of_cells[-1])
            # clean off the whitespace gunk characters:
            # print(list_of_cells[-1].strip())
            # nah, what if we ignore it entirely:
            # print(list_of_cells[:-1])

            # add the list of cells, each list representing a row, to the list of rows -- except the last cell. screw that dude.
        #list_of_rows.append(list_of_cells[:-1])

    # give back the list of rows to whatever calls this function
    #return list_of_rows


# write
#def write_file(data, column_names, file_location):
    # open a file in which to store the data
#outfile = open('data/visitors.csv', 'w+')
    #with open('visitors.csv', 'w+') as outfile:
#writer = csv.writer(outfile)
#writer.writerow(['Park', 'Rank', 'Recreation Visits', 'Percent of Total'])
        # make sure at a minimum we don't have more columns of data than headers for columns
    #if len(['Park', 'Rank', 'Recreation Visits', 'Percent of Total']) >= len(data[0]):
            # prepare to write to it as a csv file
#writer = csv.writer(outfile)
            # write the first row as the headers we want
#writer.writerow(['Park', 'Rank', 'Recreation Visits', 'Percent of Total'])

            # write the rows of data
#writer.writerows(list_of_rows)
    #else:
       # print('So close. There are not enough column names {len(column_names)} for all the cells in the row ({len(data[0])}).')


# do everything all together
#def scrape_jail_records(url, filename, column_names):
#content = get_page_content(url)
#formatted_html = parse_html(content)
#data = extract_data(formatted_html)
#write_file(data, column_names, filename)


#if __name__ == '__main__':
   # url = 'https://irma.nps.gov/Stats/Reserved.ReportViewerWebControl.axd?OpType=Resource&Version=11.0.2802.16&Name=ViewerScript'
    #filename = 'data/visitors.csv'
    #column_names = [
       # 'Park', 'Rank', 'Recreation Visits', 'Percent of Total'
   # ]
    #scrape_jail_records(url, filename, column_names)