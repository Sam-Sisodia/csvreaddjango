
import pandas as pd 


import time

def measure(hell):
        def inner(*args):
                start_time = time.time()
                hell(*args)
                end_time = time.time()
                timetake = end_time- start_time
                print("Time Take  : ", timetake)
                return  a
        return inner



def  hell(a,b):
        c = a+b
        return c


a =hell(3,5)
print(a)









hell(123,333)





# col_list = ["name"]
# # df = pd.read_csv("/home/visiontrek-pc/Sajal/ProjectCSV/country1.csv",usecols=col_list)

# # print(df["name"])



# df = pd.read_csv("/home/visiontrek-pc/Sajal/ProjectCSV/country1.csv", )

# dictionary = df.to_dict(orient="index")
# #print(dictionary)
# for key in dictionary:
#         print(key, '->', dictionary[key])

# # for index ,row in df.iterrows():
# #         pass
        


# # print(row)

# # {0: {'name ': 'sajal', 'address': 'Ambala'}, 
# #  1: {'name ': 'Ankit', 'address': 'US'},
# #  2: {'name ': 'Sam', 'address': 'Delhi'}}
        

# # print("===========================")


# # #print(type(df))

# # print(row["name"])
# print(type(row))







#https://stackoverflow.com/questions/14365542/import-csv-file-as-a-pandas-dataframe