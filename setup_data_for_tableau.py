import pandas as pd

def getPesticide(colName):
    return colName.split(" VMP: ")[0]

def getVMP(colName):
    name = colName.replace(" µg/L","")        
    return float(name.split(" VMP: ")[1])

def getPesticideColNames(csv):
    names = []
    for colName in csv.columns: 
        if "VMP"in colName:
            names.append(colName)
    return names


csv = pd.read_csv("Vigilancia - Agrotóxicos 2014_2017.csv")

# ... pesticide, concentration, percentage of VMP

header = []
for index, row in csv.iterrows():
    newRow = []
