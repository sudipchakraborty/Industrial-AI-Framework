#hotel_tool.py
from app.memory.preference_manager import (
    get_preference
)


def search_hotel(city):

    hotel = get_preference(
        "preferred_hotel"
    )

    return {

        "city":
            city,

        "hotel":
            hotel,

        "rating":
            4.5,

        "price":
            3500
    }