def seqentialSearch(list1,item):
    pos=0
    found=False

    while pos<len(list1) and not found:
        if list1[pos]==item:
           print("position of ",item, "is ",pos+1)
           found=True
        else:
            pos=pos+1      
    return found

Elements=[1,3,5,8,10,23,35]
print(seqentialSearch(Elements,10))
print(seqentialSearch(Elements,11))