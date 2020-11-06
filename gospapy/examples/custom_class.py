""" Example of custom classes.

This file shows the usage of the module in cases where you work on more
advanced data structures than arrays, such as an estimate class. In the
following, only the position of the Estimate is used to calculate the GOSPA.

This is done using the `assignment_cost_function`-argument to the method, which
takes two elements of the class and outputs the error between them.

Further, if you have two different classes with different attributes, you must
handle the input in your assignment cost function accordingly. The first/second
argument to the cost function will always be elements of the first/second
argument to the `calculate_gospa` function, respectively. This is highly
discouraged, and may frequently lead to comparing apples to oranges.
"""
import numpy as np
import gospapy

class Estimate(object):
    """ Dummy class for example purposes. """
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

def position_difference(first_estimate, second_estimate):
    return np.linalg.norm(first_estimate.position - second_estimate.position)

class RelativeEstimate(object):
    """ Relative estimate to some observer. """
    def __init__(self, relative_position, velocity):
        self.relative_position = relative_position
        self.velocity = velocity
        pass

    def get_position(self, observer_position):
        return observer_position + self.position

def relative_to_absolute_position(target, relative_track, observer_position):
    track_pos = observer_position + relative_track.position
    return np.linalg.norm(track_pos-target.position)

if __name__ == '__main__':
    n_targets = np.random.randint(10)
    n_tracks = np.random.randint(10)
    targets = [Estimate(10*(np.random.rand()-0.5), np.random.rand()-0.5)
            for _ in range(n_targets)]
    tracks = [Estimate(10*(np.random.rand()-0.5), np.random.rand()-0.5)
            for _ in range(n_tracks)]
    observer_position = 5
    relative_tracks = [RelativeEstimate(estimate.position-observer_position,
                estimate.velocity)
        for estimate in tracks]
    gospa, assignment, localization_cost, miss_cost, false_cost = (
            gospapy.calculate_gospa(targets, tracks, c=3, p=1,
                assignment_cost_function=position_difference))
    print(gospa)
    relative_assignment = (lambda (x, y): 
            relative_to_absolute_position(x, y, observer_position))
    gospa, assignment, localization_cost, miss_cost, false_cost = (
            gospapy.calculate_gospa(targets, relative_tracks, c=3, p=1,
                assignment_cost_function=relative_assignment))
    print(gospa)
