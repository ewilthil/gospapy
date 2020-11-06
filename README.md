## About

gospapy is a Python implementation of the generalized optimal sub-pattern assignment (GOSPA), introduced by [1], also see [2] for a presentation. It is compatible with Python 2.7 and 3.7.

See [abusajana/GOSPA](https://github.com/abusajana/GOSPA) for a Matlab implementation. This implementation has been verified with the example script provided there, see the script in the example folder.

In addition to the GOSPA metric, the method returns the target-to-track assignment and the decomposed cost. See the example folder for usage, and the docstring of the module. 

The Euclidian distance is used as a cost function by default, but any function that takes two elements and return an assignment cost can be used. See the example file `custom_class.py` for how to use this with your own classes.

## Installation

Clone the repo, navigate into it and run `pip install -e .`. The `-e`-flag installs this as editable, which is reccomended if you need to modify it.

## Usage
A typical usage is
```Python
import gospapy
gospa, assignment, loc_err, miss_err, false_err = gospapy.calculate_gospa(
    current_targets, current_tracks, cutoff_distance, order)
```

See the examples for more use cases. Most of the code is documented inline.

## References
[1] A. S. Rahmathullah, A. F. Garcia-Fernandez, and L. Svensson. Generalized optimal sub-pattern assignment metric. In 20th International Conference on Information Fusion (FUSION), July 2017. Available online: https://arxiv.org/abs/1601.05585

[2] L. Svensson, Generalized optimal sub-pattern assignment metric (GOSPA), presentation, 2017. Available online: https://youtu.be/M79GTTytvCM

## Contact
Bugs and suggestions can be reported as issues on Github. For code improvements, pull requests are appreciated. For additional contact info, see ewilthil.github.io.
