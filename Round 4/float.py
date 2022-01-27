"""Computer Programming
VU TU PHUONG NGUYEN
Comparing floating-point (decimal) numbers¶"""

def compare_floats(a,b,EPS):
    """start calling the float_number and compare"""
    if abs(a-b) < EPS:
        return True
    else:
        return False
if __name__ == "__compare_floats__":
    compare_floats()