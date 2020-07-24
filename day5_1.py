test_list = ['0','1','2','10','4','1','0','56','2','0','1','3','0','56','0','4'] 
print ("The original list is : " + str(test_list)) 
test_list.append(test_list.pop(test_list.index('0'))) 
print ("The modified element moved list is : " + str(test_list)) 
