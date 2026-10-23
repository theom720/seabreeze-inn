from business_rules import (
    calculate_room_cost,
    calculate_stay_total,
    get_stay_discount,
    gets_welcome_package,
    requires_credit_check,
)


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


def test_cleaning_fee_at_exactly_300():
    assert round(calculate_stay_total(300.00, 1), 2) == 340.00


def test_no_cleaning_fee_just_above_300():
    assert round(calculate_stay_total(301.00, 1), 2) == 301.00


def test_credit_check_at_exactly_2000():
    assert requires_credit_check(2000.00) is True


def test_no_credit_check_just_below_2000():
    assert requires_credit_check(1999.99) is False


def test_welcome_package_at_exactly_6_nights():
    assert gets_welcome_package(6, 2000.00) is True


def test_no_welcome_package_at_5_nights():
    assert gets_welcome_package(5, 2000.00) is False


def test_welcome_package_at_exactly_1000_total():
    assert gets_welcome_package(10, 1000.00) is True


def test_no_welcome_package_just_below_1000_total():
    assert gets_welcome_package(10, 999.99) is False
