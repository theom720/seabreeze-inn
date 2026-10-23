from business_rules import calculate_room_cost, get_stay_discount


def test_room_cost_is_rate_times_nights():
    assert calculate_room_cost(110.00, 2) == 220.00


def test_no_discount_below_4_nights():
    assert get_stay_discount(3) == 0.0


def test_six_percent_at_exactly_4_nights():
    assert get_stay_discount(4) == 0.06


def test_six_percent_at_13_nights():
    assert get_stay_discount(13) == 0.06


def test_eighteen_percent_at_exactly_14_nights():
    assert get_stay_discount(14) == 0.18


def test_corporate_under_4_nights_gets_six_percent():
    assert get_stay_discount(2, corporate=True) == 0.06


def test_14_nights_beats_corporate_floor():
    assert get_stay_discount(14, corporate=True) == 0.18
