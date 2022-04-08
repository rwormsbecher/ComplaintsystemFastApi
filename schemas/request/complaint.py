from schemas.base import BaseComplaint


class ComplaintIn(BaseComplaint):
    title: str
    description:  str
    photo_url: str
    amount: float
