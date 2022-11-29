import random
import csv
import pandas


def add_emoji(students,emojis) :

    for student in students :
        student["emoji"] = random.choice(emojis)

def add_arrow(students) :

    for student in students :

        if len(student["prenom"]) < 5 :
            student["fleche"] = "⬇"
        elif len(student["prenom"]) > 7 :
            student["fleche"] = "⬆"
        else :
            student["fleche"] = "➡"


def add_gender(students):

    for student in students :

        student["sexe"] = random.choice(["H","F"])

def add_size(students):

    for student in students :

        student["taille"] = f"1,{random.randint(50, 99)} m"

def adapt_emoji(students):

    for student in students :

        if student["sexe"] == "H" :
            student["emoji"] = "♂"

        else :
            student["emoji"] = "♀"

def genders_pourcentage(students):

    woman_count = 0
    man_count = 0

    for student in students :

        if student["sexe"] == "H" :
            man_count += 1

        else :
            woman_count += 1

    women_pourcent = int((woman_count/(len(students)))*100)
    men_pourcent = 100 - women_pourcent

    print("women " + str(women_pourcent) +" %")
    print("man "+str(men_pourcent)+" %")

def update_header_data(header) :

    with open("data.csv",'a') as file:

        dataWriter = csv.writer(file)

        dataWriter.writerow(header)


def add_data(data):

      with open("data.csv",'a') as file:

        dataWriter = csv.writer(file)

        dataWriter.writerows(data)

def read_data() :

    with open("test02.csv",'r') as file :
        dataToRead = pandas.read_csv(file)
        print(dataToRead)

def clear_data() :

    with open("test02.csv",'r') as file :
        dataToRead = pandas.read_csv(file)
        print(dataToRead)
