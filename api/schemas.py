from pydantic import BaseModel


class GetRecommendations(BaseModel):
    event_id: int
    score: float
    event_title: str
    event_organizer: str
    event_buy_link: str
    event_buy_link_additional: str


