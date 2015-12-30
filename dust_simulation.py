import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

positions = np.array([])
velocities = np.array([])
accelerations = np.array([])
masses = np.array([])

appender = np.append

N = 4

###############################################################################
# The error is that the lists of positions, velocities, and accelerations are
# simply [1,2,3,5,...] rather than triplets such as [(1,2,3),(4,5,6)]
###############################################################################

for i in xrange(N):
	for j in xrange(N):
		for k in xrange(N):
			# pos_appender(np.array([i,j,k]))
			# vel_appender(np.array([0,0,0]))
			# acc_appender(np.array([0,0,0]))
			positions = appender(positions,[i+1e4,j+1e4,k+1e4])
			velocities = appender(velocities,[0,0,0])
			accelerations = appender(accelerations,[0,0,0])
			masses = appender(masses,5e30)

big_pos = np.array([0,0,0])
big_vel = np.array([0,0,0])
big_acc = np.array([0,0,0])
big_mass = np.array([0])

G = 6.674e-11
sqrt = np.sqrt

def F(point,mass):
	"""Function to calculate the acceleration each of the 2 bodies undergoes
	   using F=m_1*m_2*G/r^2 formula (Newtonian gravity)"""
	global G
        global big_pos

	# we needn't do everything twice, as F_12 = -F_21
	r = big_pos - point
	# r_21 = point1 - point2
        print('r: ',r)
        
	# length_r_12 = np.sqrt(r_12.dot(r_12))
	length_r = sqrt(r.dot(r))
        print('length_r: ',length_r)
	# acc1 is F_21 / mass1, so we'll just omit mass1
	acc = G * mass
        print('acc: ',acc)
	acc *= r/(length_r * length_r * length_r) # faster than using x^3
        print('acc: ',acc)

	return acc

t0 = time.clock()

# print(len(pos))
for x in xrange(100):
	for i in xrange(N):
        #       print('accel: ', accelerations)
                print('positions: ',positions)
                print('new_acc: ',F(positions[i],masses[i]))
                accelerations[i] = F(positions[i],masses[i])#temp_a
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

