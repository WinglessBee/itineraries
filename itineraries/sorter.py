from .convertor import get_amount_in_euros
from .models import Itinerary, ItinerariesToSort, SortedItineraries, SortingTypeOptions


def sort_itineraries(data: ItinerariesToSort) -> SortedItineraries:
    return SortedItineraries(
        sorting_type=data.sorting_type,
        sorted_itineraries=_sort_map[data.sorting_type](data.itineraries),
    )


def _sort_by_price(itineraries: list[Itinerary]) -> list[Itinerary]:
    return sorted(
        itineraries, key=lambda i: get_amount_in_euros(i.price.amount, i.price.currency)
    )


def _sort_by_duration(itineraries: list[Itinerary]) -> list[Itinerary]:
    return sorted(itineraries, key=lambda i: i.duration_minutes)


def _sort_by_price_and_duration(itineraries: list[Itinerary]) -> list[Itinerary]:
    return sorted(
        itineraries,
        key=lambda i: (
            i.duration_minutes * get_amount_in_euros(i.price.amount, i.price.currency)
        ),
    )


_sort_map = {
    SortingTypeOptions.cheapest: _sort_by_price,
    SortingTypeOptions.fastest: _sort_by_duration,
    SortingTypeOptions.best: _sort_by_price_and_duration,
}
