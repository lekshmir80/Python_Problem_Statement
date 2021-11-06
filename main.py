# Importing Packages
import pandas as pd
import numpy as np

# Declaring Variables
dicti = {}
dict_distress = {}
dict_fall = {}
dict_unautority = {}
dict_pro = {}

# Reading csv File
data = pd.read_csv("/Users/Lekshmi Pillai/Music/Python/Events_All.csv")

# Creating matrix - 2D
data1 = np.array(list([data.empId, data.alert]))
print(data1.ndim)  # Printing Dimension length


# print(data1)
# print(type(data1))
for i in list(data.empId):
    dicti[i] = list(data.empId).count(i)
print(dicti)

for i in dicti.keys():
    countd = 0
    countf = 0
    countu = 0
    countp = 0
    for ind, j in enumerate(data1[0]):
        if i is j:
            if (data1[1][ind] == "DISTRESS"):
                countd = countd + 1
            elif (data1[1][ind] == "FALL"):
                countf = countf + 1
            elif (data1[1][ind] == "UNAUTHORIZED_ENTRY"):
                countu = countu + 1
            elif (data1[1][ind] == "PROACTIVE_OBSERVATION"):
                countp = countp + 1
    dict_distress[i] = countd
    dict_fall[i] = countf
    dict_unautority[i] = countu
    dict_pro[i] = countp
# print(dict_distress)
# print(dict_fall)
# print(dict_unautority)

# %total alert calculation
alert_dic_total = {}
dict_alert_sum = {}
for i in dicti.keys():
    alert_dic_total[i] = f"{(dicti[i] / 12890) * 100}%"
print("---------------------Table 1-----------------------------")
print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("EmpID", "DISTRESS", "FALL", "UNAUTHORIZED_ENTRY", "Proactive",
                                                         "%alertsToTotal"))
for key in dicti.keys():
    EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive, alertsToTotal = key, dict_distress[key], dict_fall[key], \
                                                                          dict_unautority[key], dict_pro[key], \
                                                                          alert_dic_total[key]
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive,
                                                             alertsToTotal))

for i in dicti.keys():
    dict_distress[i] = f"{dict_distress[i] / dicti[i] * 100}%"
    dict_fall[i] = f"{dict_fall[i] / dicti[i] * 100}%"
    dict_unautority[i] = f"{dict_unautority[i] / dicti[i] * 100}%"
    dict_pro[i] = f"{dict_pro[i] / dicti[i] * 100}%"
# print(dict_alert_sum)
# print(alert_dic_total)

# print(dict_distress)
# print(dict_fall)
# print(dict_unautority)
print("---------------------Table 2-----------------------------")
print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("EmpID", "DISTRESS", "FALL", "UNAUTHORIZED_ENTRY", "Proactive",
                                                         "%alertsToTotal"))
for key in dicti.keys():
    EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive, alertsToTotal = key, dict_distress[key], dict_fall[key], \
                                                                          dict_unautority[key], dict_pro[key], \
                                                                          alert_dic_total[key]
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive,
                                                             alertsToTotal))
