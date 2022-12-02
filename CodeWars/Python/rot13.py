def rot13(message):

    n = "0123456789"
    s = " ?./§&é'<>°+¨£%µ(-è_çà)=^$ù*,;:!~#}|][{`\@¤"
    l = []
    r = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    def triage(i) :

        for j in n :
            if i == j :
                return i
        for k in s :
            if i == k :
                return i

        if i.isupper() :

            for h in range(len(r)) :
                if r[h] == i.lower() :
                    return r[h + 13].upper()

        else :
            for h in range(len(r)) :
                if r[h] == i :
                    return r[h + 13]
        return "error"

    for i in message :
        l.append(triage(i))

    print(''.join(l))

rot13("aA bB zZ 1234 *!?%")
# nN oO mM 1234 *!?%
