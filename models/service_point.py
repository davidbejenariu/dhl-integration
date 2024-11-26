from dataclasses import dataclass
from typing import Optional


@dataclass
class ServicePoint:
    url: Optional[str] = None
    label: Optional[str] = None