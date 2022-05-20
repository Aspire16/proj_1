from pprint import pprint

dict = {
    "name": "first name",
    "age": 24,
    "summ": 320
}
dict["street"] = "siit"
dict["age"] = 32
#print (dict)
#print (len(dict))
#print (dict["age"])
#print (dict.get("sity", "Нету"))
lis_ras = ["lis 1", "lis 2", "lis 3", "lis 4", "lis 5"]
dict["som"] = lis_ras
pprint (dict)
dict["som"].append("slis 6")
pprint (dict)