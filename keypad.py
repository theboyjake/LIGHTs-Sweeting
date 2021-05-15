
import RPi.GPIO as io
import time

io.setmode(io.BCM)
pad = [[ 1,2,3,'A'],
       [ 4,5,6,'B'],
       [ 7,8,9,'C'],
       ['*',0,'#','D']]
row = [6,13,19,26]
col = [12,16,20,21]

for i in rang(4);
	io.setup(col[i],io.OUT)
	io.setup(col[i],I)
	io.setup(row[i],io.IN, pull_up_down = io.PUD_UP)

while I:
	for i in range(4):
		io.output(col[i],0)
		for j in range(4):
			if io.input(row[j]) == 0 :
				print pad[j][i]
				time.sleep(0.2)
		io.output(col[i],1)
