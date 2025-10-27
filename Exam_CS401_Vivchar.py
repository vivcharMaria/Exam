temps = [
  {"date" : "27 october", "morning" : 12, "day" : 14, "evening" : 11, "status" : "rainy"},
  {"date" : "28 october", "morning" : 11, "day" : 15, "evening" : 13, "status" : "cloudy"},
  {"date" : "29 october", "morning" : 11, "day" : 14, "evening" : 12, "status" : "cloudy"},
  {"date" : "30 october", "morning" : 10, "day" : 14, "evening" : 14, "status" : "cloudy"},
  {"date" : "31 october", "morning" : 14, "day" : 17, "evening" : 14, "status" : "sunny"},
  {"date" : "1 november", "morning" : 15, "day" : 17, "evening" : 13, "status" : "cloudy"},
  {"date" : "2 november", "morning" : 11, "day" : 13, "evening" : 11, "status" : "cloudy"},
  {"date" : "3 november", "morning" : 11, "day" : 13, "evening" : 10, "status" : "cloudy"},
  {"date" : "4 november", "morning" : 10, "day" : 13, "evening" : 11, "status" : "cloudy"},
  {"date" : "5 november", "morning" : 12, "day" : 14, "evening" : 12, "status" : "cloudy"}
]

for day in temps:
    day["average temp"] = round((day["morning"] + day["day"] + day["evening"]) / 3, 1)

print("Прогноз погоди на 10 днів для вашого міста: Париж\n")
for day in temps:
    print(day["date"], "/", day["status"], "/", day["average temp"], "C")

