import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

p1=np.array([0.0,0.0,0.0])
p2=np.array([-1.0e10,0.0,0.0])
v1=np.array([0.0,2.2e2,0.0])
v2=np.array([0.0,-2.2e7,0.0])
#v2=np.array([0.0,0.0,0.0])
a1=np.array([0.0,0.0,0.0])
a2=np.array([0.0,0.0,0.0])
m1=5.1e35
m2=5.1e33

p3=np.array([-5.0e10,0.0,0.0])
p4=np.array([-7.0e10,0.0,0.0])
v3=np.array([0.0,1.2e7,0.0])
v4=np.array([0.0,6.2e6,0.0])
#v2=np.array([0.0,0.0,0.0])
a3=np.array([0.0,0.0,0.0])
a4=np.array([0.0,0.0,0.0])
m3=5.1e33
m4=5.1e33

G = 6.674e-11
sqrt = np.sqrt

def F(point1,point2,mass1,mass2):
	"""Function to calculate the acceleration each of the 2 bodies undergoes
	   using F=m_1*m_2*G/r^2 formula (Newtonian gravity)"""
	global G

	# we needn't do everything twice, as F_12 = -F_21
	r_12 = point2 - point1

	length_r_12 = sqrt(r_12.dot(r_12))

	# acc1 is F_21 / mass1, so we'll just omit mass1
	acc1 = G * mass2
	acc1 *= r_12/(length_r_12*length_r_12*length_r_12)

	acc2 = -acc1 * (mass1/mass2)

	return acc1,acc2

p1_list = []
v1_list = []
a1_list = []
p2_list = []
v2_list = []
a2_list = []
p1_list_appender = p1_list.append
v1_list_appender = v1_list.append
a1_list_appender = a1_list.append
p2_list_appender = p2_list.append
v2_list_appender = v2_list.append
a2_list_appender = a2_list.append

p3_list = []
v3_list = []
a3_list = []
p4_list = []
v4_list = []
a4_list = []
p3_list_appender = p3_list.append
v3_list_appender = v3_list.append
a3_list_appender = a3_list.append
p4_list_appender = p4_list.append
v4_list_appender = v4_list.append
a4_list_appender = a4_list.append

t0 = time.clock()

for i in xrange(10220):
	a1,a2=F(p1,p2,m1,m2)
	second_a1,a3=F(p1,p3,m1,m3)
	third_a1,a4=F(p1,p4,m1,m4)
	second_a2,second_a3=F(p2,p3,m2,m3)
	third_a2,second_a4=F(p2,p4,m2,m4)
	third_a3,third_a4=F(p3,p4,m3,m4)	
	v1+=(a1 + second_a1 + third_a1)
	v2+=(a2 + second_a2 + third_a2)
	v3+=(a3 + second_a3 + third_a3)
	v4+=(a4 + second_a4 + third_a4)
	p1+=v1
	p2+=v2
	p3+=v3
	p4+=v4
	p1_list_appender(tuple(p1))
	v1_list_appender(tuple(v1))
	a1_list_appender(tuple(a1))
	p2_list_appender(tuple(p2))
	v2_list_appender(tuple(v2))
	a2_list_appender(tuple(a2))
	p3_list_appender(tuple(p3))
	v3_list_appender(tuple(v3))
	a3_list_appender(tuple(a3))
	p4_list_appender(tuple(p4))
	v4_list_appender(tuple(v4))
	a4_list_appender(tuple(a4))

print('time: ',time.clock() - t0)

# thin out the lists to plot only some of the points (much more quickly)
p1_list = [p1_list[i] for i in xrange(len(p1_list)) if i%39==0]
p2_list = [p2_list[i] for i in xrange(len(p2_list)) if i%39==0]
p3_list = [p3_list[i] for i in xrange(len(p3_list)) if i%39==0]
p4_list = [p4_list[i] for i in xrange(len(p4_list)) if i%39==0]

# make 2D plot of positions
# plt.scatter([p1_list[i][1] for i in xrange(len(p1_list))],[p1_list[i][0] for i in xrange(len(p1_list))],c='g',marker='o',s=3,lw=0,alpha=0.1)
# plt.scatter(range(len(v1_list)),[v1_list[i][0] for i in xrange(len(v1_list))],c='b',marker='+')
# plt.scatter(range(len(a1_list)),[a1_list[i][0] for i in xrange(len(a1_list))],c='r',marker='+')
# plt.scatter(p2,range(len(p2)))

# make 3D plot of position
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter([p1_list[i][0] for i in xrange(len(p1_list))],[p1_list[i][1] for i in xrange(len(p1_list))],[p1_list[i][2] for i in xrange(len(p1_list))],marker='+',c='b')
ax.scatter([p2_list[i][0] for i in xrange(len(p2_list))],[p2_list[i][1] for i in xrange(len(p2_list))],[p2_list[i][2] for i in xrange(len(p2_list))],marker='+',c='g')
ax.scatter([p3_list[i][0] for i in xrange(len(p3_list))],[p3_list[i][1] for i in xrange(len(p3_list))],[p3_list[i][2] for i in xrange(len(p3_list))],marker='+',c='r')
ax.scatter([p4_list[i][0] for i in xrange(len(p4_list))],[p4_list[i][1] for i in xrange(len(p4_list))],[p4_list[i][2] for i in xrange(len(p4_list))],marker='+',c='purple')

plt.show()
