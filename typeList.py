l = ['a', 'b', 'c', 'd']
sum=0
string=""
#Loop through elements within a list 
for i in l:
		if type(i) == int or isinstance(i,float): #checking for integer or float
			sum+=i		
		elif isinstance(i, str): #checking for string
			string= string + " " +i	
print "Sum:" + str(sum)
print "String:" + string 

 
if sum!=0 and string!="": #checking if sum and string changed, then list is mixed type
	print "The list you entered is mixed type!"
elif sum==0 and string!="": #checking if only string changed, then list is string type
	print "The list you entered is string type!"
elif sum!=0 and string == "": #checking if only sum changed, then list is integer type
	print "The list you entered is integer type!"		

