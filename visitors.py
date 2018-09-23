

# python imports
import csv
# external imports
import requests
from bs4 import BeautifulSoup

# get
url = 'https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year'
def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print('That was not a good url. You should feel bad for supplying a bad url.')


# parse
def parse_html(page_content):
    # uses the BeautifulSoup library and the lxml parser to find the table element with the data we want
    soup = BeautifulSoup(page_content, 'lxml')
    # that table has a class name of 'stripe'
    table = soup.find('tbody', attrs={'class': 'stripe'})
    # need to figure out the atrrubutes for my table

    # give just the table we care about back to the calling function
    return table


# extract
def extract_data(html):
    # a place to keep all the rows of data to hand off to whatever else will need to use it
    list_of_rows = []
    # go through each row in the table
    for row in html.findAll('tr'):
        # prepare a list of the cells in the table
        list_of_cells = []
        # find each row with a 'td' -- table data -- tag
        for cell in row.findAll('td'):
            # add it to the list of cells
            list_of_cells.append(cell.text)
        # if this isn't empty
        if list_of_cells:
            # make sure we get only the data we want:
            # print(list_of_cells)
            # eh, that last thing in the list is a little iffy, let's access it by index:
            # print(list_of_cells[-1])
            # clean off the whitespace gunk characters:
            # print(list_of_cells[-1].strip())
            # nah, what if we ignore it entirely:
            # print(list_of_cells[:-1])

            # add the list of cells, each list representing a row, to the list of rows -- except the last cell. screw that dude.
            list_of_rows.append(list_of_cells[:-1])

    # give back the list of rows to whatever calls this function
    return list_of_rows


# write
def write_file(data, column_names, file_location):
    # open a file in which to store the data
    with open('visitors.csv', 'w+') as outfile:
        # make sure at a minimum we don't have more columns of data than headers for columns
        if len(column_names) >= len(data[0]):
            # prepare to write to it as a csv file
            writer = csv.writer(outfile)
            # write the first row as the headers we want
            writer.writerow(column_names)

            # write the rows of data
            writer.writerows(data)
        else:
            print('So close. There are not enough column names {len(column_names)} for all the cells in the row ({len(data[0])}).')


# do everything all together
def scrape_jail_records(url, filename, column_names):
    content = get_page_content(url)
    formatted_html = parse_html(content)
    data = extract_data(formatted_html)
    write_file(data, column_names, filename)


if __name__ == '__main__':
    url = 'https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year'
    filename = 'data/visitors.csv'
    column_names = [
        'Park', 'Rank', 'Recreation Visits', 'Percent of Total'
    ]
    scrape_jail_records(url, filename, column_names)