process_sjf = { "p0":[1,7],
		 "p1":[4,9],
		 "p2":[6,3],
		 "p3":[8,14],
		 "p4":[10,5],
		 "p5":[11,4],
		 "p6":[12,2]
		}
for i in range(0,len(process_sjf[i][1])-1):  #applying bubble sort to sort process according to their burst time
	for j in range(0,len(process_sjf[i][1])-i-1):
  		if(process_sjf[j][1]>process_sjf[j+1][1]):
   			temp=process_sjf[j]
   			bt[j]=bt[j+1]
   			process_sjf[j][1]=process_sjf[j+1][1]
   			process_sjf[j+1][2]=temp
   			process_sjf[j]=process_sjf[j+1]
  			temp=process_sjf[i][1]
waitingtime=[]    
averagewaitingtime=0  
turnaroundtime=[]    
averageturnaroundtime=0   
waitingtime.insert(0,0)
turnaroundtime.insert(0,process_sjf[0])
for i in range(1,len(process_sjf)):  
	waitingtime.insert(i,wt[i-1]+process_sjf[i-1])
 	turnaroundtime.insert(i,wt[i]+process_sjf[i])
 	averagewaitingtime+=waitingtime[i]
 	averageturnaroundtime+=tat[i]
	averagewaitingtime=float(averagewaitingtime)/7
	averageturnaroundtime=float(avgtat)/7
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
	print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
 	print("\n")
print("Average Waiting time is: "+str(averagewaitingtime))
print("Average Turn Around Time is: "+str(averageturnaroundtime))