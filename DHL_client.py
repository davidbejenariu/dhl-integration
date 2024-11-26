import http.client
import json
import urllib.parse
from typing import Dict, Optional, Any, List
from models.tracking_event import TrackingEvent


class DHLClient:
    """
    A client to interact with the DHL API.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the DHL client with a base URL and an API key.

        :param base_url: The base URL for the DHL API.
        :param api_key: API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint: str, params: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """
        Makes an HTTPS GET request to the specified endpoint with the given parameters.

        :param endpoint: The API endpoint to access.
        :param params: Query parameters for the request.
        :return: Parsed JSON response as a dictionary or None in case of errors.
        """
        try:
            query = urllib.parse.urlencode(params)
            headers = {
                "Accept": "application/json",
                "DHL-API-Key": self.api_key,
            }

            connection = http.client.HTTPSConnection(self.base_url)
            connection.request("GET", f"{endpoint}?{query}", headers=headers)

            response = connection.getresponse()
            response_data = response.read()
            if response.status == 200:
                return json.loads(response_data)
            else:
                self._log_error(response, response_data)
        except Exception as e:
            print(f"Exception occurred: {e}")
        finally:
            connection.close()

        return None

    @staticmethod
    def _log_error(response: http.client.HTTPResponse, response_data: bytes) -> None:
        """
        Logs errors from the API response.

        :param response: The HTTP response object.
        :param response_data: Raw response data.
        """
        try:
            error_message = response_data.decode()
        except Exception:
            error_message = "Unable to decode error message."

        print(
            f"Error: {response.status} {response.reason}\n"
            f"Response Data: {error_message}"
        )

    def get_last_tracking_event(self, tracking_number: str) -> Optional[TrackingEvent]:
        """
        Fetches the last tracking event for a given tracking number.

        :param tracking_number: The tracking number to query.
        :return: The last tracking event or None if not found.
        """
        endpoint = "/track/shipments"
        params = {"trackingNumber": tracking_number}

        data = self._make_request(endpoint, params)
        if data and "shipments" in data:
            try:
                events = data["shipments"][0].get("events", [])
                if events:
                    return TrackingEvent.from_json(json.dumps(events[0]))
            except (KeyError, IndexError, ValueError):
                print("Invalid response structure while fetching tracking event.")
        return None

    def get_all_service_point_location_names(
        self, country_code: str, city: str, radius: int
    ) -> List[str]:
        """
        Retrieves all service point location names within a specific radius.

        :param country_code: Country code where the service points are located.
        :param city: City name where the service points are located.
        :param radius: Search radius in meters.
        :return: List of service point location names.
        """
        endpoint = "/location-finder/v1/find-by-address"
        params = {
            "countryCode": country_code,
            "addressLocality": city,
            "radius": radius,
            "locationType": "servicepoint",
        }

        data = self._make_request(endpoint, params)
        if data and "locations" in data:
            try:
                return [location["name"] for location in data["locations"]]
            except (KeyError, TypeError):
                print("Invalid response structure while fetching locations.")
        return []
