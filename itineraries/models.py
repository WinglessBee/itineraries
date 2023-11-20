import enum

from annotated_types import Gt
from pydantic import BaseModel
from typing import List, Annotated


class CurrencyOptions(str, enum.Enum):
    CZK = "CZK"
    EUR = "EUR"
    USD = "USD"


class Price(BaseModel):
    amount: Annotated[int, Gt(0)]
    currency: CurrencyOptions


class Itinerary(BaseModel):
    id: str
    duration_minutes: Annotated[int, Gt(0)]
    price: Price


class SortingTypeOptions(str, enum.Enum):
    cheapest = "cheapest"
    fastest = "fastest"
    best = "best"


class ItinerariesToSort(BaseModel):
    sorting_type: SortingTypeOptions
    itineraries: List[Itinerary]


class SortedItineraries(BaseModel):
    sorting_type: SortingTypeOptions
    sorted_itineraries: List[Itinerary]
