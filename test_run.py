import numpy as np
from scipy.spatial.transform import Rotation as R
import averageQuaternions as aquat
import plotQuaternions as pquat

# Q is a Nx4 numpy matrix and contains the quaternions to average in the rows.
# The quaternions are arranged as (w,x,y,z), with w being the scalar
# The weight vector w must be of the same length as the number of rows in the
# quaternion maxtrix Q

q1 = R.from_euler('xyz', [90, 0, 0], degrees=True).as_quat().reshape(1, 4)
q2 = R.from_euler('xyz', [0, 90, 0], degrees=True).as_quat().reshape(1, 4)
q3 = R.from_euler('xyz', [0, 0, 90], degrees=True).as_quat().reshape(1, 4)
q0 = R.from_euler('xyz', [0, 0, 0], degrees=True).as_quat().reshape(1, 4)

q_list = [q1, q2, q3, q0]
w = [1, 1, 1, 0]

Q = np.concatenate(q_list, axis=0)
assert len(q_list) == Q.shape[0]

# q_avg = aquat.weightedAverageQuaternions(Q, w)
q_avg = aquat.averageSimplified(Q, w)

origin = np.array([0, 0, 0])  # origin of vector
v0 = [0, 0, 1]  # Initial orientation of vector

pquat.plot_transformation(origin, v0, q_avg)
