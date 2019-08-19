import numpy as np
import gospa_python
from scipy.stats import multivariate_normal

def generate_tracks(num_generate, distributions):
    if len(distributions) < num_generate:
        raise ValueError("Cannot generate {} targets from {} distributions"
                .format(num_generate, len(distributions)))
    else:
        tracks = []
        for track_idx in range(num_generate):
            tracks.append(distributions[track_idx].rvs())
        return tracks

def test_case_Rahmatullah2017():
    target_position = [
            np.array([-6, -6]),
            np.array([0, 3])]
    true_track_position = [
            np.array([-6.7, -5.1]),
            np.array([-1.8, 2.9])]
    false_track_position = [
            np.array([22, 18]),
            np.array([-10, 18]),
            np.array([35, 42]),
            np.array([38, 0]),
            np.array([50, 35]),
            np.array([7, 28]),
            np.array([-15, -19]),
            np.array([17, 17]),
            np.array([42, 30]),
            np.array([20, 15])]
    target_distribution = [multivariate_normal(pos, np.identity(2)) for pos in target_position]
    true_track_distribution = [multivariate_normal(pos, np.identity(2)) for pos in true_track_position]
    false_track_distribution = [multivariate_normal(pos, np.identity(2)) for pos in false_track_position]

    N_misses = [0, 1, 2]
    N_false = [0, 1, 3, 10]
    N_MC = 1000
    gospa_values = dict()
    for n_miss in N_misses:
        for n_false in N_false:
            gospa_values[n_miss, n_false] = np.zeros(N_MC)

    for n_mc in range(N_MC):
        for n_miss in N_misses:
            for n_false in N_false:
                chosen_targets = generate_tracks(2, target_distribution)
                chosen_true_tracks = generate_tracks(2-n_miss,
                        true_track_distribution)
                chosen_false_tracks = generate_tracks(n_false,
                        false_track_distribution)
                chosen_tracks = chosen_true_tracks + chosen_false_tracks
                (gospa,
                assignments,
                localization,
                gospa_missed,
                gospa_false) = gospa_python.calculate_gospa(
                        chosen_targets,
                        chosen_tracks,
                        c=8, p=1)
                for target_id, track_id in assignments.items():
                    if target_id != track_id:
                        print target_id, track_id
                gospa_values[n_miss, n_false][n_mc] = gospa

    for n_miss in N_misses:
        for n_false in N_false:
            mean_gospa = np.mean(gospa_values[n_miss, n_false])
            print("GOSPA={} for {} miss, {} false alarms".format(
                    mean_gospa, n_miss, n_false))
    return gospa_values

if __name__ == '__main__':
    gospa_values = test_case_Rahmatullah2017()
