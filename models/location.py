from dataclasses import dataclass
from typing import Optional

from models.address import Address
from models.service_point import ServicePoint


@dataclass
class Location:
    address: Optional[Address] = None
    servicePoint: Optional[ServicePoint] = None