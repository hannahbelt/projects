#!usr/local/bin/env python3

# external imports
from pprint import pprint
import requests
# project-level imports
from secret_settings import geojson_stub, geojson_key


# Gets the address from the API from Google
def pull_api(address):
    p = {'address': address, 'key': geojson_key}
    return requests.get(geojson_stub, params=p)


# creates function to 
def get_geolocation_data(address):
        county = ''
        state_long = ''
        state_short = ''
        country = ''

        response = pull_api(address)
        if response.status_code == 200:
            # print(response.json())

            # addresses are self-reported and human-entered; they will always be
            # a little messy and the API will always miss a few
            try:
                #['address_components'])
                address_components = response.json()['results'][0]['address_components']

                for line in address_components:
                    if line['types'][0] == 'administrative_area_level_2':
                        county = line['long_name']
                    elif line['types'][0] == 'administrative_area_level_1':
                        state_long = line['long_name']
                        state_short = line['short_name']
                    elif line['types'][0] == 'country':
                        country = line['long_name']

               # organizes the list within the API stuff
                geolocator = {}

                # narrows down the list to only be what we need
                geolocator['clean_address'] = response.json()['results'][0]['formatted_address']
                geolocator['latitude'] = response.json()['results'][0]['geometry']['location']['lat']
                geolocator['longitude'] = response.json()['results'][0]['geometry']['location']['lng']
                geolocator['county'] = county
                geolocator['state_long'] = state_long
                geolocator['state_short'] = state_short
                geolocator['country'] = country

                # print(geolocator)
                return geolocator

            except IndexError:
                return None

# creates the sentence format about the address
def write_output_sentence(geolocator):
    # print(geolocator)
    print(f'The address for the Media Innovation Center is {geolocator["clean_address"][:-5]}, at latitude {geolocator["latitude"]} and longitude {geolocator["longitude"]}, in {geolocator["county"]}, {geolocator["state_long"]}, {geolocator["country"]}.')

# gets the data to put in the sentence 
def geolocate(address):
    geolocator_data = get_geolocation_data(address)
    if geolocator_data:
        write_output_sentence(geolocator_data)
    else:
        print(geolocator_data)


# allows you to use code for any address
if __name__ == '__main__':
    address = '62 MORRILL WAY MORGANTOWN, WV 26506'
    # address = '62 MORRILL WAY MORGANTOWN, WV 26506'
    geolocate(address)