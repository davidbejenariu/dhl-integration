import argparse

from DHL_client import DHLClient

DEFAULT_COUNTRY_CODE = 'RO'
DEFAULT_CITY = 'Bucharest'
DEFAULT_RADIUS = 5000


def get_last_tracking_event(api_key, tracking_number):
    """
    Retrieves the last tracking event for a given tracking number.

    :param api_key: DHL API key
    :param tracking_number: Package tracking number
    :return: The last tracking event data
    """
    client = DHLClient('api-eu.dhl.com', api_key)
    return client.get_last_tracking_event(tracking_number)


def print_all_service_point_locations_within_radius(api_key, country_code, city, radius=5000):
    """
    Prints all service point locations within the specified radius.

    :param api_key: DHL API key
    :param country_code: Country code where service points are located
    :param city: City where service points are located
    :param radius: Search radius in meters (defaults to DEFAULT_RADIUS if None)
    """
    client = DHLClient('api.dhl.com', api_key)

    country_code = country_code or DEFAULT_COUNTRY_CODE
    city = city or DEFAULT_CITY
    radius = radius or DEFAULT_RADIUS

    locations = client.get_all_service_point_location_names(country_code, city, radius)
    for location in locations:
        print(location)


def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description='DHL Service Point and Tracking Event Viewer')

    parser.add_argument('--api_key', required=True, help='DHL API key')
    parser.add_argument('--tracking_number', required=False, help='Package tracking number')

    return parser.parse_args()


def print_args_usage():
    print("Usage: python main.py --api_key <API_KEY> --tracking_number <TRACKING_NUMBER>")


# Sample usage
if __name__ == '__main__':
    try:
        args = parse_arguments()

        if args.tracking_number:
            # Get last tracking event
            last_tracking_event = get_last_tracking_event(args.api_key, args.tracking_number)
            print(last_tracking_event)

            # Print service point locations
            if last_tracking_event.location is not None and last_tracking_event.location.address is not None:
                print_all_service_point_locations_within_radius(args.api_key, last_tracking_event.location.address.countryCode, last_tracking_event.location.address.addressLocality)
            else:
                print_all_service_point_locations_within_radius(args.api_key, DEFAULT_COUNTRY_CODE, DEFAULT_CITY)
        else:
            print_args_usage()
    except argparse.ArgumentError as e:
        print(f"Error: {e}")
        print_args_usage()
