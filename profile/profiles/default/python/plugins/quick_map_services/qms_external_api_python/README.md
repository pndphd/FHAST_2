# Python QMS API

## Installation
TODO  
  
## Usage examples

```
from qms_external_api.client import Client

cl = Client()

services_list = cl.get_geoservices()
print '\nAll services: ', services_list

service_info = cl.get_geoservice_info(services_list[0])
print '\nService info: ', service_info

print '\nService icon: '
if service_info['icon']:
    service_icon = cl.get_icon_content(service_info['icon'])
    print service_icon
else:
    service_icon = cl.get_default_icon()
    print service_icon

print '\nSmall default icon: '
service_icon = cl.get_default_icon(width=24, height=24)
print service_icon

searched_list = cl.search_geoservices('osm')
print '\nSearched services ("osm"): ', searched_list

filtered_list = cl.get_geoservices(type_filter=GeoServiceType.GeoJSON)
print '\nOnly Geojson services: ', filtered_list
```

