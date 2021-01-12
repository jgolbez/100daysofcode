#Nest List in Dict
travel_log = {
    "France" : ["Paris, Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 15
    }
}

#Nest Dict inside a list

travel_log2 = [
    {
      "country" : "France", 
      "cities_visited" : ["Paris", "Lille", "Dijon"], 
      "total_visits" : 12
    },
    {
      "country" : "Germany", 
      "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
      "total_visits" : 15
    }
]
print(travel_log2[0]["country"])

test_cities = travel_log2[1]["cities_visited"] + travel_log2[0]["cities_visited"]
print(test_cities)

for city in test_cities:
    print(city)

