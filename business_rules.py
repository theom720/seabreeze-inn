MID_TIER_NIGHTS = 4
TOP_TIER_NIGHTS = 14
MID_TIER_RATE = 0.06
TOP_TIER_RATE = 0.18


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Return the room cost before any discount."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if nights >= TOP_TIER_NIGHTS:
        return TOP_TIER_RATE
    elif nights >= MID_TIER_NIGHTS or corporate:
        return MID_TIER_RATE
    else:
        return 0.0
