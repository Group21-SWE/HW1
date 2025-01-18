import pytest

from myfile import Test

# Create an instance of the test class
test_instance = Test()
def test_divideNums_pass():
    '''
    This method tests the divideNums method such that
    the test passes
    '''
    try:
        test_instance.divideNums(10, 1)
    except Exception(e):
        pytest.fail(f"Unexpected error: {e}")

def test_divideNums_fail():
    '''
    This method tests the divideNums method such that
    the test fails
    '''
    try:
        test_instance.divideNums(10, 0)
    except ZeroDivisionError:
        pytest.fail(f"Dividing by zero")