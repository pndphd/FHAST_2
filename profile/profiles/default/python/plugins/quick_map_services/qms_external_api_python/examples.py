from __future__ import absolute_import, print_function
from .client import Client, GeoServiceType

cl = Client()

services_list = cl.get_geoservices()
print('All services: ', services_list, '\n')

service_info = cl.get_geoservice_info(services_list[0])
print('Service info: ', service_info, '\n')

print('Service icon: ')
if service_info['icon']:
    service_icon = cl.get_icon_content(service_info['icon'])
    print(service_icon, '\n')
else:
    service_icon = cl.get_default_icon()
    print(service_icon, '\n')

print('Small default icon: ')
service_icon = cl.get_default_icon(width=24, height=24)
print(service_icon, '\n')

searched_list = cl.search_geoservices('osm')
print('Searched services ("osm"): ', searched_list, '\n')

filtered_list = cl.get_geoservices(type_filter=GeoServiceType.GeoJSON)
print('Only Geojson services: ', filtered_list, '\n')
