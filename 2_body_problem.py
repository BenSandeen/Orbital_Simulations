import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

p1=np.array([0.0,0.0,0.0])
p2=np.array([-1.0e10,-1.0e10,0.0])
v1=np.array([0.0,2.2e7,0.0])
v2=np.array([0.0,-2.2e7,0.0])
#v2=np.array([0.0,0.0,0.0])
a1=np.array([0.0,0.0,0.0])
a2=np.array([0.0,0.0,0.0])
m1=5.1e35
m2=5.1e35

G = 6.674e-11
sqrt = np.sqrt

def F(point1,point2,mass1,mass2):
	"""Function to calculate the acceleration each of the 2 bodies undergoes
	   using F=m_1*m_2*G/r^2 formula (Newtonian gravity)"""
	# acc1=(mass1*mass2)*(1e-3)/((((point1-point2).dot(point1-point2))**(0.5))**2)
	# acc2=(mass1*mass2)*(1e-3)/((((point1-point2).dot(point1-point2))**(0.5))**2)
	global G

	# we needn't do everything twice, as F_12 = -F_21
	r_12 = point2 - point1
	# r_21 = point1 - point2

	# length_r_12 = np.sqrt(r_12.dot(r_12))
	length_r_12 = sqrt(r_12.dot(r_12))

	# acc1 is F_21 / mass1, so we'll just omit mass1
	acc1 = G * mass2
	acc1 *= r_12/(length_r_12*length_r_12*length_r_12)

	acc2 = -acc1 * (mass1/mass2)

	# acc1*=(point1-point2)/np.sqrt(((point1-point2).dot(point1-point2)))
	# acc2*=(point2-point1)/np.sqrt(((point2-point1).dot(point2-point1)))

	# acc1*=(point2-point1)/np.sqrt(((point2-point1).dot(point2-point1)))
	# acc2*=(point1-point2)/np.sqrt(((point1-point2).dot(point1-point2)))

	# acc1/=mass1
	# acc2/=mass2

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

t0 = time.clock()

for i in xrange(30220):
	a1,a2=F(p1,p2,m1,m2)
	v1+=a1#*0.01
	v2+=a2#*0.01
	p1+=v1#*0.01
	p2+=v2#*0.01
	p1_list_appender(tuple(p1))
	v1_list_appender(tuple(v1))
	a1_list_appender(tuple(a1))
	p2_list_appender(tuple(p2))
	v2_list_appender(tuple(v2))
	a2_list_appender(tuple(a2))

print('time: ',time.clock() - t0)

# thin out the lists to plot only some of the points (much more quickly)
p1_list = [p1_list[i] for i in xrange(len(p1_list)) if i%39==0]
p2_list = [p2_list[i] for i in xrange(len(p2_list)) if i%39==0]

# make 2D plot of positions
# plt.scatter([p1_list[i][1] for i in xrange(len(p1_list))],[p1_list[i][0] for i in xrange(len(p1_list))],c='g',marker='o',s=3,lw=0,alpha=0.1)
# plt.scatter(range(len(v1_list)),[v1_list[i][0] for i in xrange(len(v1_list))],c='b',marker='+')
# plt.scatter(range(len(a1_list)),[a1_list[i][0] for i in xrange(len(a1_list))],c='r',marker='+')
# plt.scatter(p2,range(len(p2)))

# make 3D plot of position
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter([p1_list[i][0] for i in xrange(len(p1_list))],[p1_list[i][1] for i in xrange(len(p1_list))],[p1_list[i][2] for i in xrange(len(p1_list))],marker='+',c='b')
ax.scatter([p2_list[i][0] for i in xrange(len(p2_list))],[p2_list[i][1] for i in xrange(len(p2_list))],[p2_list[i][2] for i in xrange(len(p2_list))],marker='+',c='r')
plt.show()
