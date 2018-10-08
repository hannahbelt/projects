#!usr/local/bin/env python3

#python import
from pprint import pprint
# external imports
import requests
#project-level imports
from secret_settings import geojson_stub, geojson_key


def ping_api(address):
    # do stuff
    parameters = {'address': address, 'key': geojson_key}
    #print(return requests.get(geojson_stub, params=parameters))
    return requests.get(geojson_stub, params=parameters)

def get_geolocation_data(address):
    county = ''
    state_long = ''
    state_short = ''
    country = ''

    response = ping_api(address)
    #pprint(response.json())
    #pprint(response.json()['results'][0])
    #pprint(response.json()['results'][0]['address_components'])
    addr_components = response.json()['results'][0]['address_components']
   
    for line in addr_components:
        if line['types'][0] == 'administration_area_level_2':
            county = line['long_name']
        elif line['types'][0] == 'administrative_area_level_1':
            state_long = line['long_name']
            state_short = line['short_name']
        elif line['types'][0] == 'country':
            country = line['long_name']

    geolocator = {}
    geolocator['clean_address'] = response.json()['results'][0]['formatted_address']
    geolocator['latitude'] = response.json()['results'][0]['geometry']['location']['lat']
    geolocator['longitude'] = response.json()['results'][0]['geometry']['location']['lng']
    geolocator['county'] = county
    geolocator['state_long'] = state_long
    geolocator['state_short'] = state_short
    geolocator['country'] = country

    #print(geolocator)
    return geolocator

def write_output_sentence(geolocator):
    print(f'Some stuff about where I live: My address is {geolocator["clean_address"][:-5']}, at latitude {geolocator["latitude"]} and longitude {geolocator["longitude"]}, in {geolocator["county"]}, {geolocator["state_long"]}, {geolocator["country"]}.')


#def geolocate(address):
    geolocator_data = get_geolocation_data(address)
    write_output_sentence(geolocator_data)


if __name__ == '__main__':
    address = '1614 Monterey Street Pittsburgh'
    #geolocate(address)
    #ping_api(address)
    geolocate(address)
