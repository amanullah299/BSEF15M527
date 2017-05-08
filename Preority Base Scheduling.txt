total_wt=0
process_p={
	"p0",[1,7,2],
	"p1",[4,9,1],
	"p2",[6,3,3]
	}
for i in range(3):
	if (process_p[i][2]<process_p[i+1][2] & process_p[i][2]<process_p[i+2][2]):
		total_wt+=process_p[i][1]
	elif (process_p[i+1][2]<process_p[i][2] & process_p[i+1][2]<process_p[i+2][2]):
		total_wt+=process_p[i+1][1]
	else:
		total_wt+=process_p[i+2][1]
print('Total waiting Time',total_wt)
print('Average waiting Time',(total_wt)/3)