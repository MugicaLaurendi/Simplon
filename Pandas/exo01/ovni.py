import pandas as pd

def main() :
    csv = "cleaning_copy.csv"

    file = pd.read_csv(csv, index_col=0)
    df = pd.DataFrame(file)

    df["hour"] = "00:00"
    #print(df.iloc[0])

    print(df.iloc[4])
    del df.iloc[4]


    add_to_csv(df,csv)

def add_to_csv(df,csv) :

    print("add to csv ? y/n")
    addcsv = input()
    if addcsv == "y" :
        df.to_csv(csv, index=False)

main()
