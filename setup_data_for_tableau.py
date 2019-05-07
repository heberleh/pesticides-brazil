import pandas as pd

# extract the Pesticide Name from a column name
def getPesticide(colName):
    return colName.split(" VMP: ")[0]


# Extracts the VMP float value.
# VMP stands for "Valor Máximo Permitido", in English: Maximum Value Allowed
def getVMP(colName):
    name = colName.replace(" µg/L","")        
    return float(name.split(" VMP: ")[1])


# column names
def getPesticideColNames(csv):
    names = []
    for colName in csv.columns: 
        if "VMP"in colName:
            names.append(colName)
    return names

def getNonPesticideColNames(csv):
    names = []
    for colName in csv.columns: 
        if "VMP" not in colName:
            names.append(colName)
    return names



# ... pesticide, concentration, VMP, percentage of VMP

csv = pd.read_csv("pesticides_original.csv")

pestCols = getPesticideColNames(csv)
nonPestCols = getNonPesticideColNames(csv)

header = nonPestCols + ["pesticide", "concentration", "VMP", "percentage of VMP"]
matrix = []
for index, row in csv.iterrows():
    for pestCol in pestCols:        
        if not pd.isna(row[pestCol]):
            newRow = []
            for col in nonPestCols:
                newRow.append(row[col]) #add general attributes

            newRow.append(getPesticide(pestCol)) #pesticide name
            newRow.append(row[pestCol]) #concentration
            newRow.append(getVMP(pestCol)) #max value permitted
            newRow.append(float(row[pestCol])/getVMP(pestCol)) #percentage ox max value
            
            matrix.append(newRow) # store the new line
        
pd.DataFrame(matrix, columns=header).to_csv("pesticides_tableau.csv")