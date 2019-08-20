## About

gospapy is a Python implementation of the generalized optimized sub-pattern assignment (GOSPA), introduced by [1]. It is compatible with Python 2.7 and 3.7.

See abusajana/GOSPA for a Matlab implementation. This implementation has been verified with the example script provided there.

In addition to the GOSPA metric, the method returns the target-to-track assignment and the decomposed cost.

### Q/A
- Can I use this with my own classes?
    - Yes. The Euclidian distance is used as a cost function by default, but any function that takes two elements and return an assignment cost can be used. See the test file `test_customClass.py` for an example.

## References
[1] A. S. Rahmathullah, A. F. Garcia-Fernandez, and L. Svensson. Generalized optimal sub-pattern assignment metric. In 20th International Conference on Information Fusion (FUSION), July 2017. Available online: https://arxiv.org/abs/1601.05585
