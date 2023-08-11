#!/usr/bin/python3
# exercise 2 for day 8 of 100 days of python 
# Dictionary in List

travel_log = [
    {
        "country": 'France}',
        "visits": 12,
        "cities": ["Paris", "Little", "Dijon"]
    },
    {
        "country": 'Germany',
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]


def add_new_country(country="", visits=0, places=[]):
    travel_log.append({"country": country, "visits": visits, "cities": places})
    print("You've visited {:s} {:d} times.".format(travel_log[-1]["country"], travel_log[-1]["visits"]))
    
    print("You've been to ", end=" ")
    for item in travel_log[-1]['cities']:
        print(item, end=', ')


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
