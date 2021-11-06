# Importing Packages
import pandas as pd
import numpy as np
from rich.prompt import Prompt

# Declaring Variables
dict_id = {}
dict_distress = {}
dict_fall = {}
dict_unautority = {}
alert_dic_total = {}
dict_pro = {}

# 1. Extract the data from csv dataset
print("File is extracting...............")
data = pd.read_csv("/Users/Lekshmi Pillai/Music/Python/Events_All.csv")
print("File extracted..................")

# Creating matrix - 2D
# 2. Create a 2-dimensional matrix data structure with empId and Alert (refer to dataset for both these fields)
data1 = np.array(list([data.empId, data.alert]))
# print(data1.ndim)  # Printing Dimension length
print("Created 2-D matrix")

# mapping each empId to total No: of alerts
print("Mapping each empID to alerts")
print("Waiting....................................")
for i in list(data.empId):
    dict_id[i] = list(data.empId).count(i)
print(dict_id)

for i in dict_id.keys():
    countd = 0
    countf = 0
    countu = 0
    countp = 0
    for ind, j in enumerate(data1[0]):
        if i is j:
            if data1[1][ind] == "DISTRESS":
                countd = countd + 1
            elif data1[1][ind] == "FALL":
                countf = countf + 1
            elif data1[1][ind] == "UNAUTHORIZED_ENTRY":
                countu = countu + 1
            elif data1[1][ind] == "PROACTIVE_OBSERVATION":
                countp = countp + 1
    dict_distress[i] = countd
    dict_fall[i] = countf
    dict_unautority[i] = countu
    dict_pro[i] = countp


def emp_total_alerts_all_emp():

    for key in dict_id.keys():
        alert_dic_total[key] = f"{(dict_id[key] / 12890) * 100}%"
    # Table
    print("---------------------Table 1-----------------------------")
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("EmpID", "DISTRESS", "FALL", "UNAUTHORIZED_ENTRY",
                                                             "PROACTIVE",
                                                             "%alertsToTotal"))
    for key in dict_id.keys():
        EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive, alertsToTotal = key, dict_distress[key], dict_fall[key], dict_unautority[key], dict_pro[key], alert_dic_total[key]
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive,
                                                                 alertsToTotal))


def emp_total_alerts_each_emp():
    for i in dict_id.keys():
        dict_distress[i] = f"{dict_distress[i] / dict_id[i] * 100}%"
        dict_fall[i] = f"{dict_fall[i] / dict_id[i] * 100}%"
        dict_unautority[i] = f"{dict_unautority[i] / dict_id[i] * 100}%"
        dict_pro[i] = f"{dict_pro[i] / dict_id[i] * 100}%"
    print("---------------------Table 2-----------------------------")
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("EmpID", "DISTRESS", "FALL", "UNAUTHORIZED_ENTRY",
                                                             "PROACTIVE",
                                                             "%alertsToTotal"))
    for key in dict_id.keys():
        EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive, alertsToTotal = key, dict_distress[key], dict_fall[key], \
                                                                              dict_unautority[key], dict_pro[key], \
                                                                              dict_id[key]
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(EmpID, DISTRESS, FALL, UNAUTHORIZED_ENTRY, Proactive,
                                                                 alertsToTotal))


def menu():
    print("1. Calculate % of alerts created by each emp against total alerts for all emp ")
    print("2. Calculate % of alerts created by each emp against total alerts by each emp ")
    print("3. Exit")


while True:
    menu()
    ch = Prompt.ask("Enter your option ", choices=["1", "2", "3"])
    if ch == "1":
        emp_total_alerts_all_emp()
    elif ch == "2":
        emp_total_alerts_each_emp()
    elif ch == "3":
        break
