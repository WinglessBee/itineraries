from itineraries.models import (
    CurrencyOptions,
    Itinerary,
    ItinerariesToSort,
    SortingTypeOptions,
    Price,
)
from itineraries.sorter import sort_itineraries
import pytest


@pytest.mark.parametrize(
    "sorting_type,itineraries,first_result",
    [
        pytest.param(
            SortingTypeOptions.cheapest,
            [
                Itinerary(
                    id="rural_trip",
                    duration_minutes=499,
                    price=Price(amount=699, currency=CurrencyOptions.EUR),
                ),
                Itinerary(
                    id="urban_escape",
                    duration_minutes=285,
                    price=Price(amount=399, currency=CurrencyOptions.EUR),
                ),
            ],
            Itinerary(
                id="urban_escape",
                duration_minutes=285,
                price=Price(amount=399, currency=CurrencyOptions.EUR),
            ),
            id="same_currency",
        ),
        pytest.param(
            SortingTypeOptions.cheapest,
            [
                Itinerary(
                    id="sunny_beach_bliss",
                    duration_minutes=330,
                    price=Price(amount=90, currency=CurrencyOptions.EUR),
                ),
                Itinerary(
                    id="rocky_mountain_adventure",
                    duration_minutes=140,
                    price=Price(amount=830, currency=CurrencyOptions.EUR),
                ),
                Itinerary(
                    id="urban_heritage_odyssey",
                    duration_minutes=275,
                    price=Price(amount=620, currency=CurrencyOptions.CZK),
                ),
            ],
            Itinerary(
                id="urban_heritage_odyssey",
                duration_minutes=275,
                price=Price(amount=620, currency=CurrencyOptions.CZK),
            ),
            id="currency_mismatch",
        ),
        pytest.param(
            SortingTypeOptions.fastest,
            [
                Itinerary(
                    id="floral_ride",
                    duration_minutes=285,
                    price=Price(amount=400, currency=CurrencyOptions.USD),
                ),
                Itinerary(
                    id="pine_cove_tour",
                    duration_minutes=120,
                    price=Price(amount=100, currency=CurrencyOptions.USD),
                ),
                Itinerary(
                    id="riverside_zen",
                    duration_minutes=180,
                    price=Price(amount=200, currency=CurrencyOptions.USD),
                ),
            ],
            Itinerary(
                id="pine_cove_tour",
                duration_minutes=120,
                price=Price(amount=100, currency=CurrencyOptions.USD),
            ),
            id="fastest",
        ),
        pytest.param(
            SortingTypeOptions.best,
            [
                Itinerary(
                    id="express",
                    duration_minutes=100,
                    price=Price(amount=500, currency=CurrencyOptions.EUR),
                ),
                Itinerary(
                    id="cheap",
                    duration_minutes=140,
                    price=Price(amount=200, currency=CurrencyOptions.EUR),
                ),
                Itinerary(
                    id="smart",
                    duration_minutes=120,
                    price=Price(amount=220, currency=CurrencyOptions.EUR),
                ),
            ],
            Itinerary(
                id="smart",
                duration_minutes=120,
                price=Price(amount=220, currency=CurrencyOptions.EUR),
            ),
            id="best",
        ),
    ],
)
def test_sort_itineraries(sorting_type, itineraries, first_result):
    result = sort_itineraries(
        ItinerariesToSort(sorting_type=sorting_type, itineraries=itineraries)
    )
    assert result.sorting_type == sorting_type
    assert result.sorted_itineraries[0] == first_result
