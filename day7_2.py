ls= [(1,2), (3,4), (5,6)]
finallist = []
for tuple in ls:
     listt = list(tuple)
     summ = 0
     for m in listt:
         summ+=m
     finallist.append(summ)
print(finallist) 