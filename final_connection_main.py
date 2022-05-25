import json
import ast

from pip import main





# Opening JSON file
f1 = open('data_K.json')
f2 = open('data_N.json')
f3 = open('data_0.json')
  
# returns JSON object as 
# a dictionary
data1 = json.load(f1)
data2 = json.load(f2)
data3 = json.load(f3)

# for i in list(data1.keys()):
#     print(data1[i])

# dict1 = {"a":{"asd":"sad","sd":"df dsf"},"b":"sdfsf"}

# for i in dict1:
#     # print(i, dict1[i],end="\n")
#     for j in dict1[i]:
#         print([j])

import pandas as pd


Diagnosis_arr = []
Treatment_arr = []

# for p_id, p_info in data1.items():   
#     try: 
#         for key in p_info:
#             if str(key) == "Diagnosis":
#                 # print(str(key) + ':' + str(p_info[key]))
#                 Diagnosis_arr.append(str(p_info[key]))
#             elif str(key) == "Treatment":
#                 Treatment_arr.append(str(p_info[key]))

#     except:
#         pass

min_dict = {}
for a_key, a_value in data1.items():   
    for b_key, b_value in a_value.items():
        # "Single Quotes" wrapped string to "Double Quotes" wrapped String
        # b_value = b_value.replace("\'", "\"")
        # b_value = ast.literal_eval(b_value)
        # b_value = json.loads(b_value)
        # b_value = json.loads(b_value.replace("\\", r"\\"))
        # b_value = json.loads(r"{}".format(b_value))
        # b_value = b_value.replace('""', '')
        # b_value_json = json.loads(b_value)
        # print(b_value.pre)
        print()
        print("----- {} -----".format(b_key))
        print()

        for c_key , c_value in b_value.items():
            try:

                if c_key == "Diagnosis":
                    print()
                    print("-----> Diagnosis")
                    print(c_value["Diagnosis"])
                    print()

                if c_key == "Treatment":
                    print()
                    print("-----> Treatment")
                    print(c_value)
                    print()
                


            except:
                pass

# main_json = {}

# for a_key, a_value in data1.items():   
#     for b_key, b_value in a_value.items():
#         main_json.update({str(b_key):str(b_value)})

# for a_key, a_value in data2.items():   
#     for b_key, b_value in a_value.items():
#         main_json.update({str(b_key):str(b_value)})

# for a_key, a_value in data3.items():   
#     for b_key, b_value in a_value.items():
#         main_json.update({str(b_key):str(b_value)})

# print(main_json)
# for i,j in main_json.items():
#     print(i)

# df = pd.DataFrame.from_dict(main_json.items())
# df.columns = ['Disease', 'Parameters']
# df.to_csv("a.csv")


# for p_id, p_info in data2.items():   
#     try: 
#         for key in p_info:
#             if str(key) == "Diagnosis":
#                 # print(str(key) + ':' + str(p_info[key]))
#                 Diagnosis_arr.append(str(p_info[key]))
#             elif str(key) == "Treatment":
#                 Treatment_arr.append(str(p_info[key]))

#     except:
#         pass

# for p_id, p_info in data3.items():   
#     try: 
#         for key in p_info:
#             if str(key) == "Diagnosis":
#                 # print(str(key) + ':' + str(p_info[key]))
#                 Diagnosis_arr.append(str(p_info[key]))
#             elif str(key) == "Treatment":
#                 Treatment_arr.append(str(p_info[key]))

#     except:
#         pass

# print(Diagnosis_arr)
# print(pd.DataFrame({"Diagnosis":Diagnosis_arr,"Treatment":Treatment_arr}))
