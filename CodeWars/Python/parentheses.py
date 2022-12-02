def valid_parentheses(string):
    a = 0
    for i in range(len(string)) :

        if string[i] == "(" :
            a += 1
        if string[i] == ")" :
            a -= 1

        if i == 0 and string[i] == ")" :
            return False

        if i == len(string)-1 and string[i] == "(" :
            return False

        print(a)
        if a < 0 :
            return False
    if a != 0 :
        return False
    return True



print(valid_parentheses("vl(genljcjcyc(oygzmjafuhqa)ocuz"))
