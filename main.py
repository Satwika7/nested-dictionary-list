#list in dictionary,dictionary in dictionary
travel_log ={"France":{"cities_visited":["paris","Lille","Dijon"]},
             "Germany":["Berlin","Hamburg","stuttgart"]
            }
#dictionaries in list
travel_logs =[
  {"country":"France",
   "cities_visited":["paris","Lille","Dijon"],
   "Total_visits":12},
  
  {"country":"Germany"
   ,"cities_visited":["Berlin","Hamburg","stuttgart"]
  }
]

print(travel_log["France"]["cities_visited"][2])

print(travel_logs[0]["cities_visited"][1])