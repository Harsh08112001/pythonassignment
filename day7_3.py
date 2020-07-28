l = [(1,2,3), [1,2], ['a','hit','less']]
  

output = [] 
  
def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
  

print ('The original list: ', l) 
reemovNestings(l) 
print ('The list after removing nesting: ', output) 
