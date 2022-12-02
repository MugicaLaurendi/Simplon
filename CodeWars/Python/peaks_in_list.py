from codecs import BOM_BE


l = [1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]
bob = {"pos" : [] , "peaks" : []}
for i in range(1,len(l)-1) :
    print(i)
    if l[i-1] < l[i] and l[i] > l[i+1] :
        bob["pos"].append(i)
        bob["peaks"].append(l[i])
    elif l[i-1] < l[i] and l[i] == l[i+1] :
        bob["pos"].append(i)
        bob["peaks"].append(l[i])

print(bob)
