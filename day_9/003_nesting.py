capials = {
    "France": "Paris",
    "Germany" : "Benrlin",
} 
#list in dict
"""trave_log = {
    "France" :{"cities_visited":["paris","Liller","Dijon"],"total_visits":12},
    "Germany": ["Berlin","Hamburg","Stuttgart"],
}"""

#dict in list  
travel_log = [
    {
        "coutry":"France",
        "Cities_visited":["Paris","Lille","dijon"],
        "total_visits":12
     },
     {
         "country":"Germany",
         "cities_visited":["Berlin","Hamburg","Stuttgart"],
         "totl_visits":5
     }
]
for i in travel_log:
    print(i)

print(travel_log[0])