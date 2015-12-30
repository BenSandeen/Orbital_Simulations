import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

positions = []
pos_appender = positions.append
velocities = []
vel_appender = velocities.append
accelerations = []
acc_appender = accelerations.append
masses = []
mass_appender = masses.append

N = 4

for i in xrange(N):
	for j in xrange(N):
		for k in xrange(N):
			# pos_appender(np.array([i,j,k]))
			# vel_appender(np.array([0,0,0]))
			# acc_appender(np.array([0,0,0]))
			positions.append(np.array([i,j,k]))
			velocities.append(np.array([0,0,0]))
			accelerations.append(np.array([0,0,0]))
			mass_appender(5e30)

G = 6.674e-11
sqrt = np.sqrt

def F(point1,point2,mass1,mass2):
	"""Function to calculate the acceleration each of the 2 bodies undergoes
	   using F=m_1*m_2*G/r^2 formula (Newtonian gravity)"""
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

	return acc1,acc2

t0 = time.clock()

# print(len(pos))
for x in xrange(100):
	for i in xrange(N):
		for j in xrange(i,N):
			print('positions: ',len(positions))
			temp_a1, temp_a2 = F(positions[i],positions[j],masses[i],masses[j])
			accelerations[i] += temp_a1
			accelerations[j] += temp_a2
			print('accelerations: ',len(accelerations))
	velocities = [velocities[z] + accelerations[z] for z in xrange(len(velocities))] # velocities + accelerations
	positions = [positions[z] + velocities[z] for z in xrange(len(velocities))] # positions += velocities
	print('positions: ',len(positions))
	print('velocities: ',len(velocities))
	print('accelerations: ',len(accelerations))

	# for i in xrange(3000):
	# 	a1,a2=F(p1,p2,m1,m2)
	# 	v1+=a1
	# 	v2+=a2
	# 	p1+=v1
	# 	p2+=v2
	# 	p1_list_appender(tuple(p1))
	# 	v1_list_appender(tuple(v1))
	# 	a1_list_appender(tuple(a1))
	# 	p2_list_appender(tuple(p2))
	# 	v2_list_appender(tuple(v2))
	# 	a2_list_appender(tuple(a2))

	print('time: ',time.clock() - t0)

	# thin out the lists to plot only some of the points (much more quickly)
	# p1_list = [p1_list[i] for i in xrange(len(p1_list)) if i%39==0]
	# p2_list = [p2_list[i] for i in xrange(len(p2_list)) if i%39==0]

	# make 2D plot of positions
	# plt.scatter([p1_list[i][1] for i in xrange(len(p1_list))],[p1_list[i][0] for i in xrange(len(p1_list))],c='g',marker='o',s=3,lw=0,alpha=0.1)
	# plt.scatter(range(len(v1_list)),[v1_list[i][0] for i in xrange(len(v1_list))],c='b',marker='+')
	# plt.scatter(range(len(a1_list)),[a1_list[i][0] for i in xrange(len(a1_list))],c='r',marker='+')
	# plt.scatter(p2,range(len(p2)))

	# make 3D plot of position
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')

	ax.scatter([a[0] for a in positions],[b[1] for b in positions],[c[2] for c in positions])
	plt.savefig('step'+str(x)+'.png')

