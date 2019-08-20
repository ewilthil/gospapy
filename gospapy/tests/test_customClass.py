import numpy as np
import gospapy

class Estimate(object):
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

def position_difference(first_estimate, second_estimate):
    return np.linalg.norm(first_estimate.position - second_estimate.position)

if __name__ == '__main__':
    n_targets = np.random.randint(10)
    n_tracks = np.random.randint(10)
    targets = [Estimate(10*(np.random.rand()-0.5), np.random.rand()-0.5)
            for _
            in range(n_targets)]
    tracks = [Estimate(10*(np.random.rand()-0.5), np.random.rand()-0.5)
            for _
            in range(n_tracks)]
    (gospa,
    assignment,
    localization_cost,
    miss_cost,
    false_cost) = gospapy.calculate_gospa(
            targets,
            tracks,
            c=3,
            p=1,
            assignment_cost_function=position_difference)
    print(gospa)
