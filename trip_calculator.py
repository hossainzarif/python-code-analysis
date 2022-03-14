from main import calc_total

F = 0.5

def hotel_cost(days):
    return days * 140


# Valid cities
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183 * F
    elif city == "Tampa":
        return 220 * F
    elif city == "Pittsburgh":
        return 222 * F
    elif city == "Los Angeles":
        return 475 * F
    else:
        print
        "Not a valid destination"


# Amount of days
def rental_car_cost(days):
    return calc_total(days) * (100 - days) / 0.5


def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return sum
print (trip_cost("Charlotte",12,100))
