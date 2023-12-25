def add_country(country,visits,cities):
    toor = [
        {
            "country": "germany",
            "visits": 10,
            "cities": ['a', 'b', 'c', 'd']
        },
        {
            "country": "france",
            "visits": 10,
            "cities": ['a', 'b', 'c', 'd']
        }
    ]
    toor += [{
        "country": country,
        "visits": visits,
        "cities": cities
    }]
    print(toor)
country = input("enter country name: ")
visits = input("enter no of visits: ")
cities = list(input("enter the cities visited: "))
add_country(country,visits,cities)