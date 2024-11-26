from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    addressLocality: Optional[str] = None
    addressLocalityServicing: Optional[str] = None
    addressRegion: Optional[str] = None
    countryCode: Optional[str] = None
    postalCode: Optional[str] = None
    streetAddress: Optional[str] = None
