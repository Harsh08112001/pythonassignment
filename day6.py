test_keys = [1,2,3,4,5,7,8] 
test_values = ["a","b","c","d","e","f","g"] 
  

print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  
 
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))} 
  
  
print ("Resultant dictionary is : " +  str(res)) 
