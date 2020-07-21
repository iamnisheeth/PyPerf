import matplotlib.pyplot as plt  
import json
my_list = [];
y = [];
#x =[0,5,10,15,20,25,30] 
x = []; 
time_secs = 0
with open('result.txt') as f:
    lines = f.readlines() # list containing lines of file
    i = 1
    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if line:
            if i <= 6:
                print('/nline # : '+line)
		i = i + 1
            else:
    		print('\nDATA:' + line)
		tokens = []
		tokens = line.split('Bytes')
		length = len(str(line))
#		print(' \n\t sub -10 : '+line[length-14:length-10])
		f = float(str(line[length-14:length-10]))
		x.append(time_secs)
		y.append(f) 
		time_secs = time_secs + 1 		
  
plt.scatter(x, y, c ="blue") 
  
# To show the plot 
plt.show()
