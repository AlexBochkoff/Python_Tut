travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, visit_amnt, city_names):
    add_new_country_dic = {}
    add_new_country_dic["country"] = country_name
    add_new_country_dic["visits"] = visit_amnt
    add_new_country_dic["cities"] = city_names
    travel_log.append(add_new_country_dic)


#🚨 Do not change the code below
add_new_country("Ukraine", 2, ["Kyiv", "Kharkiv"])
print(travel_log)