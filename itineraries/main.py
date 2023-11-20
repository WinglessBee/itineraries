from fastapi import FastAPI

from .models import ItinerariesToSort, SortedItineraries
from .sorter import sort_itineraries

app = FastAPI()


@app.post("/sort_itineraries")
async def sort_itenerary(data: ItinerariesToSort) -> SortedItineraries:
    return sort_itineraries(data)
