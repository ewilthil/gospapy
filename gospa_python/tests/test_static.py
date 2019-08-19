import numpy as np
import gospa_python
import matplotlib.pyplot as plt

def test_gospa(target_position, track_position, c=3):
    (gospa,
    assignment,
    gospa_localization,
    gospa_missed,
    gospa_false) = gospa_python.calculate_gospa(
        target_position,
        track_position,
        c=c, p=1)
    print("gospa={}".format(gospa))
    print("loc={}, miss={}, false={}".format(gospa_localization,
        gospa_missed, gospa_false))
    for target_id, track_id in assignment.items():
        print("target {} assigned to track {}".format(target_id, track_id))
    plot_scenario(target_position, track_position, assignment)

def plot_scenario(targets, tracks, assignments):
    fig, ax = plt.subplots()
    for target in targets:
        ax.plot(target[0], target[1], 'ko', ms=12)
    for track in tracks:
        ax.plot(track[0], track[1], 'rD', ms=8)
    for target_index, track_index in assignments.items():
        line_start = targets[target_index]
        line_end = tracks[track_index]
        line_x = [line_start[0], line_end[0]]
        line_y = [line_start[1], line_end[1]]
        ax.plot(line_x, line_y, 'k')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')

def test_case_1():
    target_position = [
            np.array([2, 2]),
            np.array([4, 5]),
            np.array([7, 4])]
    track_position = target_position
    test_gospa(target_position, track_position)

def test_case_2():
    target_position = [
            np.array([2, 2]),
            np.array([4, 5]),
            np.array([7, 4])]
    track_position = target_position[:2]
    test_gospa(target_position, track_position)

def test_case_3():
    target_position = [
            np.array([2, 2]),
            np.array([4, 5]),
            np.array([7, 4])]
    track_position = target_position[:2]
    test_gospa(track_position, target_position)

def test_case_4():
    target_position = [
            np.array([2, 2])]
    track_position = [
            np.array([3, 3])]
    test_gospa(track_position, target_position)


if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    plt.show()
