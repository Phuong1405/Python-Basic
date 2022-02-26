"""Computer Programming
VU TU PHUONG NGUYEN
Comparing floating-point (decimal) numbers¶
As a result, the floating-point number comparison a == b must be entered as |a − b| < EPSILON, where EPSILON represents a sufficiently small error tolerance, such as 0.000000001.

Implement the function compare_floats that uses two floating point numbers and an epsilon as a parameter and returns information on whether the numbers are same to a sufficient degree (the parameter epsilon) as a truth value.

An example of how the function operates when tested in the interactive mode of the Python interpreter:


>>> EPSILON = 0.000000001
>>> compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON)
True
>>> compare_floats(0.0002, 0.0000002, EPSILON)
False
"""

def compare_floats(a,b,EPS):
    """start calling the float_number and compare"""
    if abs(a-b) < EPS:
        return True
    else:
        return False
if __name__ == "__compare_floats__":
    compare_floats()
