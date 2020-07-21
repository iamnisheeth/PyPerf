import matplotlib.pyplot as plt  
import json
my_list = []
y = []
x = []
time_secs = 0
bandwidth_unit = '*Bits/sec'
with open('result.txt') as f:
    lines = f.readlines() # list containing lines of file
    i = 1
    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if line:
            if i <= 6:
#                 print('/nline # : '+line)
		        i = i + 1
            else:
    		print('\nDATA:' + line)
		tokens = line.split('Bytes')
		length = len(str(line))
		bandwidth_unit = str(line[length-9:length])
		f = float(str(line[length-14:length-10]))
		x.append(time_secs)
		y.append(f) 
		time_secs = time_secs + 1
plt.rcParams['axes.facecolor'] = 'black'
plt.title("Iperf Results")
plt.xlabel("time (sec)")
plt.ylabel(bandwidth_unit)
plt.plot(x, y, "ro", x, y , "r--")
plt.show()
