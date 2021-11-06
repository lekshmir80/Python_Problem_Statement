# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
dicti = {"gfg": 8, "best": 5}
test_list = [["gfg", "best", "gfg", "gfg"],
             ["all", "love", "jjj", "all"]]

dict_all = {}
dict_loc = {}
counta = 0
countb = 0

print(test_list[0].index("gfg"))
test_list[0].index("gfg")
for i in dicti.keys():
    counta = 0
    countb = 0
    for ind, j in enumerate(test_list[0]):
        if i is j:
            print(i, j)
            print(test_list[1][ind])
            if (test_list[1][ind] == "all"):
                counta = counta + 1
            elif (test_list[1][ind] == "love"):
                countb = countb + 1
    dict_all[i] = counta
    dict_loc[i] = countb

print(dict_all)
print(dict_loc)