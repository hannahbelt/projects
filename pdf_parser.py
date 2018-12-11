import csv
from datetime import date
import pdfplumber


# extract table data
def extract_table_data(pdf):
    with pdfplumber.open(pdf) as pdf:
        # print(pdf)
        # print(len(pdf.pages))
        # test = pdf.pages[1]
        # table = test.extract_table()
        # print(table[0])
        # table_data = table[1:]
        all_pages = pdf.pages[1:]
        for page in all_pages:
            table = page.extract_table()
            table_data = table[1:]

            yield table_data

# clean table data
def clean_table_data(tables):
    for table in tables:
        cleaned_table_data = []
        for line in table:
            cleaned_line = []
            for item in line:
                cleaned_item = item.replace('\n', ' ').replace('  ', ' ')
                cleaned_line.append(cleaned_item)

            cleaned_table_data.append(cleaned_line)
        #print(cleaned_table_data)
        yield cleaned_table_data



# write table data
def write_tables_to_csv(clean_data, csvfile):
    parse_date = date.today()
    with open(csvfile, 'w') as collex_file:
        writer = csv.writer(collex_file)

        col_names = [
            'bizname',
            'license_loc',
            'instate_loc',
            'mailing_loc',
            'license_no',
            'lic_date',
            'status',
            'cr_date',
            'action',
            'parse_date'
        ]

        writer.writerow(col_names)

        for table in clean_data:
            for line in table:
                line.append(parse_date)
                writer.writerow(line)



# run them all together
def scrape_pdf(pdf):
    tables = extract_table_data(pdf)
    clean_data = clean_table_data(tables)
    write_tables_to_csv(clean_data, csvfile)


    # do some journalism if there's time



    # set up global vairables and run the scrape_pdf() function and/or the get_adverse_actions() function
if __name__ == '__main__':
    pdf = 'pdfs/collections.pdf'
    csvfile = 'data/colo_collections.csv'
    #extract_table_data(pdf)
    scrape_pdf(pdf)