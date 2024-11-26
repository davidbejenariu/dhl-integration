
# DHL Service Point and Tracking Event Viewer

This Python script allows users to query the last tracking event for a package or print service point locations within a given radius from a city using the DHL API.

## Features
1. **Retrieve the last tracking event** for a given tracking number.
2. **Print service point locations** within a specified radius of a city.

## Approach
This script interacts with the DHL API to provide tracking information and service point locations. The core logic is split into two main functionalities:

### 1. `get_last_tracking_event(api_key, tracking_number)`
   - This method queries the DHL API to retrieve the last tracking event for a given tracking number. 
   - It makes a `GET` request to the `/track/shipments` endpoint and processes the response to extract the most recent tracking event.

### 2. `print_all_service_point_locations_within_radius(api_key, country_code, city, radius=5000)`
   - This method queries the DHL API to retrieve all service point locations within a specified radius from a city. 
   - It calls the `/location-finder/v1/find-by-address` endpoint and filters the response to display the names of the locations.

### Command-Line Interface (CLI)
The script uses the `argparse` library to handle command-line arguments. Users must provide the following required parameters:
- **API Key**: Required for authenticating with the DHL API.
- **Country Code**: The country code where service points are located (e.g., `RO` for Romania).
- **City**: The city where the user wants to search for service points.

Optional parameters:
- **Tracking Number**: If provided, retrieves the last tracking event for the specified package.
- **Radius**: The radius (in meters) for searching service points (defaults to 5000 meters).

### Usage Example:

```bash
$ python script.py --api_key YOUR_API_KEY --tracking_number YOUR_TRACKING_NUMBER
```

### Error Handling
- If the required parameters are not provided or are invalid, the script will print a helpful error message along with the correct usage.

### Structure
- **`DHLClient`**: Handles interactions with the DHL API, including making HTTP requests and parsing responses.
- **`parse_arguments`**: A helper function that uses `argparse` to parse command-line arguments.
- **Main Execution**: In the main body of the script, the parsed arguments are used to invoke either the tracking event or service point location functions.

## Requirements
- Python 3.7 or higher
