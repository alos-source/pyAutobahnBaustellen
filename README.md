# pyAutobahnBaustellen

## get_construction_sites
A function to retrieve information about construction sites on a given highway.

### Inputs
highway: string - the name of the highway (e.g. "A3").
reference_point_lat: float - the latitude of the reference point used to filter the construction sites.
reference_point_long: float - the longitude of the reference point used to filter the construction sites.
radius: float - the radius (in kilometers) around the reference point used to filter the construction sites.

### Outputs
A list of dictionaries, where each dictionary corresponds to a construction site and contains information about the site, such as its location, description, and subtitle.

### Example usage

```` python
reference_point_lat = 50.0
reference_point_long = 8.0
radius = 20
highway = "A3"
construction_sites = get_construction_sites(highway, reference_point_lat, reference_point_long, radius)
print(construction_sites)
````

### Requirements
This function requires the requests library to be installed. You can install it by running pip install requests.