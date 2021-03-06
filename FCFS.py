process_fcfs = { "p0":[1,7],
		 "p1":[4,9],
		 "p2":[6,3],
		 "p3":[8,14],
		 "p4":[10,5],
		 "p5":[11,4],
		 "p6":[12,2]
		} 
total_waitingtime = 0
for i in range(7):
    total_waitingtime += process_fcfs[i][1]
process_fcfs.sort(key = lambda process_queue:process_queue[1])

print 'ProcessName\tArrivalTime\tBurstTime'
for i in range(7):
    print process_fcfs[i][0],'\t\t',process_fcfs[i][1],'\t\t',process_fcfs[i][2]
print 'Total waiting time: ',total_waitingtime
print 'Average waiting time: ',(total_waitingtime/7)