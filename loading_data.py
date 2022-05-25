import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
# print(data["A"][0]["Atrial fibrillation"]["Diagnosis"])
# print(data["A"][0]["Atrial fibrillation"]["Treatment"])
  
a_z_zero_arr = [*range(65,91)]
tot = 0
for i in a_z_zero_arr:
    tot += (len(data[chr(i)]))
print(tot)
# Closing file
f.close()