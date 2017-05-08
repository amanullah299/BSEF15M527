wt=0
p_RR={
	"p1",[0,3],
	"p2",[2,8],
	"p3",[3,4],
	"p4",[5,2]
	}
for i in range(0,len(p_RR)):
	if p_RR 'p1'[1]<p_RR 'p2'[1] & p_RR 'p1'[1]<p_RR 'p3'[1] & p_RR 'p1'[1]<p_RR 'p4'[1]:
		p_RR.enque('p1')
	elif p_RR 'p2'[1]<p_RR 'p1'[1] & p_RR 'p2'[1]<p_RR 'p3'[1] & p_RR 'p2'[1]<p_RR 'p4'[1]:
		p_RR.enque('p1')
	elif p_RR 'p3'[1]<p_RR 'p1'[1] & p_RR 'p3'[1]<p_RR 'p2'[1] & p_RR 'p3'[1]<p_RR 'p4'[1]:
		p_RR.enque('p1')
	else:
		p_RR.enque('p4')
while(p_RR[i+1]!=0):
	if p_RR 'p1'[1]<=3:
		wt+='p1'[0]
	elif p_RR [i][1]<=3:
		wt+='p1'[0]
	else:
		p_RR.enque(p_RR[i])
		p_RR[i]--
	if p_RR[i+1][1]==0:
		wt+=p_RR[i]
		p_RR.deque(p_RR[i])
	if p_RR[i+1]>=p_RR.enque(time):
		p_RR.deque(p_RR[i])
		wt+=p_RR[i]
print('Average waiting Time:',wt/4)
print('Total waiting Time:',wt)