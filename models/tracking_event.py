from dataclasses import dataclass
from typing import List, Optional
from dataclass_wizard import JSONWizard

from models.location import Location
from models.tracking_status import TrackingStatus


@dataclass
class TrackingEvent(JSONWizard):
    timestamp: Optional[str] = None
    location: Optional[Location] = None
    status_code: Optional[TrackingStatus] = None
    status: Optional[str] = None
    description: Optional[str] = None
    remark: Optional[str] = None
    next_steps: Optional[str] = None
    piece_ids: Optional[List[str]] = None
