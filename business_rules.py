MID_TIER_NIGHTS = 4
TOP_TIER_NIGHTS = 14
MID_TIER_RATE = 0.06
TOP_TIER_RATE = 0.18
CLEANING_FEE = 40.00
CLEANING_FEE_LIMIT = 300.00
CREDIT_CHECK_LIMIT = 2000.00
WELCOME_PACKAGE_NIGHTS = 5
WELCOME_PACKAGE_LIMIT = 1000.00


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


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Return the stay total: the discounted cost, plus the cleaning fee when it applies."""
    cost = calculate_room_cost(nightly_rate, nights)
    rate = get_stay_discount(nights, corporate)
    discounted = cost * (1 - rate)
    if discounted <= CLEANING_FEE_LIMIT:
        return discounted + CLEANING_FEE
    return discounted


def requires_credit_check(total: float) -> bool:
    """Return True when the stay total requires a credit check."""
    return total >= CREDIT_CHECK_LIMIT


def gets_welcome_package(nights: int, total: float) -> bool:
    """Return True when the stay gets a welcome package."""
    return nights > WELCOME_PACKAGE_NIGHTS and total >= WELCOME_PACKAGE_LIMIT


def total_reserved(stays: list) -> float:
    """Return the sum of the stay totals for every stay in the list."""
    total = 0.0
    for stay in stays:
        total += calculate_stay_total(
            stay["nightly_rate"], stay["nights"], stay["corporate"]
        )
    return total
