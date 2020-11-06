""" Verifies the example against the matlab implementation.

The matfile is generated in matlab, and the GOSPA is calculated independently.
"""
import numpy as np
import gospapy
import matplotlib.pyplot as plt
from scipy.io import loadmat

def mat2list(matrix):
    return [matrix[:,n] for n in range(matrix.shape[1])]

def plot_scenario(targets, tracks, assignments):
    fig, ax = plt.subplots()
    for target_index, target in enumerate(targets):
        ax.plot(target[0], target[1], 'ko', ms=12)
        ax.text(target[0], target[1]-1, target_index)
    for track_index, track in enumerate(tracks):
        ax.plot(track[0], track[1], 'rD', ms=8)
        ax.text(track[0], track[1]-1, track_index)
    for target_index, track_index in assignments.items():
        line_start = targets[target_index]
        line_end = tracks[track_index]
        line_x = [line_start[0], line_end[0]]
        line_y = [line_start[1], line_end[1]]
        ax.plot(line_x, line_y, 'k')
        ax.set_xlim(-8, 10)
        ax.set_ylim(-10, 6)
        ax.set_aspect('equal')

if __name__ == '__main__':
    matlab_values = loadmat('gospa_matlab.mat', squeeze_me=True)
    targets = mat2list(matlab_values['x_mat'])
    tracks = mat2list(matlab_values['y_mat'])
    gospa, assignment, gospa_localization, gospa_missed, gospa_false = (
            gospapy.calculate_gospa( targets, tracks, c=matlab_values['c'],
                p=matlab_values['p'], alpha=matlab_values['alpha']))
    print("matlab={}\n python={}".format(matlab_values['d_gospa'], gospa))
    plot_scenario(targets, tracks, assignment)
    plt.show()
