numbers = input() # this gets the user input
x=0 #this makes it possible to iterate over a list

num = []    #these two lists contain numbers the original and then the positive ones
posnum = []

for i in numbers.split(): # this adds the input to the num list
    num.append(int(i))
    
num.sort() #this sorts the numbers in the list low to high

for pos, val in enumerate(num): #this adds all positive numbers to posnum list
    if val >= 0:
        posnum.append(val)
        
for nums in posnum:
    print(posnum[x],end=' ') #this prints all the numbers in pos num on 1 line
    x +=1