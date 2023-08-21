from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt


def plot_transformation(origin, v0, q):

    rot = R.from_quat(q)
    vf = rot.apply(v0)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.quiver(*origin, v0[0], v0[1], v0[2],
              length=0.05, normalize=True,
              label="v0", color='black', linestyle='--')
    ax.quiver(*origin, vf[0], vf[1], vf[2],
              length=0.05, normalize=True,
              label='vf', color='green')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.legend()
    plt.show()
