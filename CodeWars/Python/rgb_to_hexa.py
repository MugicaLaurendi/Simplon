def rgb(r,g,b) :

    rgb = [r,g,b]
    hexa = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    l = []

    print(rgb)
    a = 0
    b = 0
    c = 0
    for i in rgb :

        if int(i) < 0 :
            b = 0
            c = 0

        elif int(i) > 255 :
            b = "F"
            c = "F"

        else :
            a = int(i)/16
            b = int(a)
            c = int(a%1 * 16)

            b = hexa[b]
            c = hexa[c]

        print(b,c)
        l.append(f"{b}{c}")

    print("".join(l))

rgb(254, 253, 252)
