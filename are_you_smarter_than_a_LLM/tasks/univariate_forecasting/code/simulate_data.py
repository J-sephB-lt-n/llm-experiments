"""
Simulate univariate time series data and exports it in
CSV format to assets/simdata.csv

Run this script from the /univariate_forecasting/ folder:
$ python -m code.simulate_data
"""
from collections import namedtuple
import csv
import itertools
import random

YearMonth = namedtuple("YearMonth", ["year", "month"])

ANNUAL_PATTERN: tuple[int, ...] = (2, 6, 10, 8, -2, -6, -10, 2, 8, -5, 7, 9)
BASE_VALUE: float = 69
END_YEAR_MONTH: YearMonth = YearMonth(year=2027, month=9)
START_YEAR_MONTH: YearMonth = YearMonth(year=2025, month=1)

def generate_random_noise() -> float:
    """Returns a random float"""
    return random.uniform(-5, 5)

#trend_generator = itertools.cycle([2, 2, 2, 2, -1, -1, 3, 3, 3, 3, -2, -2])
trend_generator = itertools.repeat(0.3) 

current_yearmonth: YearMonth = START_YEAR_MONTH
value: float = 20.1
cumulative_trend: float = 0

with open("./assets/simdata.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["YearMonth", "Sales (m)"])
    while (current_yearmonth.year + current_yearmonth.month / 12) <= (
        END_YEAR_MONTH.year + END_YEAR_MONTH.month / 12
    ):
        cumulative_trend += next(trend_generator)
        value = (
            BASE_VALUE
            + cumulative_trend
            + ANNUAL_PATTERN[current_yearmonth.month - 1]
            + generate_random_noise()
        )
        csv_writer.writerow(
            [f"{current_yearmonth.year}-{current_yearmonth.month}", f"{value:.5f}"]
        )
        if current_yearmonth.month == 12:
            current_yearmonth = YearMonth(current_yearmonth.year + 1, 1)
        else:
            current_yearmonth = YearMonth(
                current_yearmonth.year, current_yearmonth.month + 1
            )
