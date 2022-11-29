import Commun

students = [{"prenom":"Thomas"},
            {"prenom":"Nariné"},
            {"prenom":"Esperence"},
            {"prenom":"Mathieu"},
            {"prenom":"Louise"},
            {"prenom":"Hémon"}]

emojis = ["🙂","😀","😄","😂","😎","🧐"]



def main() :

    #etape 1

    # attriution emoji
    Commun.add_emoji(students,emojis)

    # attribution fleches
    Commun.add_arrow(students)


    # etape 2

    #enrichir la base de données

    Commun.add_gender(students)

    Commun.add_size(students)

    #adapter l'apparition des emojies

    Commun.adapt_emoji(students)

    #repartition homme/femme

    Commun.genders_pourcentage(students)

    #etape 3

    # ...

    print(students)



main()
