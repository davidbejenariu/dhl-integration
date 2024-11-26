import enum


class TrackingStatus(enum.Enum):
    DELIVERED = "delivered"
    FAILURE = "failure"
    PRETRANSIT = "pre-transit"
    TRANSIT = "transit"
    UNKNOWN = "unknown"