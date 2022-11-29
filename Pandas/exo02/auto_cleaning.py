import pandas as pd
import numpy as np

csv = "Automobiles.csv"

df = pd.read_csv(csv)


def color() :

    def del_color(x) :
        if type(x) == str :
            x = x.replace("-", " ")
            l = x.split()
            if l[1] == "blac" :
                return "black"
            return l[1]
        return x

    df["color"] = df["color"].apply(del_color)


def rename_columns() :

    df.rename(columns={"nbSeats":"email","wheel-base-style-circum-diam":"wheel_diameter","average-mileage":"mileage","num-of-cylinders" : "num_of_cylinders"},inplace=True)

def num_of_cylinders() :

    def clean_cylinders(x) :
        l = "[@_!#$%^&*()<>?}{~:]"
        if type(x) == str :
            if x == "BuG" :
                return np.nan
            for i in x :
                if i.isdigit() :
                    x = x.replace(str(i),"")
                    continue
                for j in l :
                    if i == j :
                        x = x.replace(str(i),"")
            return x
        return x


    df["num_of_cylinders"] = df["num_of_cylinders"].apply(clean_cylinders)

def isolate_toyota() :

    def bob(id) :

        if df.iloc[int(id),"company"] == "toyota" :

            return "ok"
        return "no"




    df["test_id"] = df["id"].apply(bob)



def main() :

    #print(df.describe())
    #rename_columns()
    #color()
    #num_of_cylinders()

    company_test = df[df["company"] == "toyota"]
    print(company_test)
    #print(df["company"].value_counts())

    #print(df.head(10))

main()

#(df.count()/df.shape[0] * 100)
