import unittest
import numpy as np

from reset_rows_and_cols_with_zeros import reset_rows_with_zeros


class TestFromGenesToNetwork(unittest.TestCase):
    @staticmethod
    def create_random_binary_matrix(mat_sz=100):
        binary_matrix = np.random.randint(2, size=(mat_sz, mat_sz))

        print('TEST MATRIX', binary_matrix, '\n')
        return binary_matrix

    # Each method in this class that starts with 'test_' will be run as a test case
    def test_random_run(self):
        test_matrix = self.create_random_binary_matrix(100)
        reset_rows_with_zeros(test_matrix)

    def test_predefine_run(self):
        test_matrix = np.array([
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1]])
        actual_result = reset_rows_with_zeros(test_matrix)
        expected_result = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]])
        self.assertTrue(np.array_equal(actual_result, expected_result))

if __name__ == '__main__':
    t = TestFromGenesToNetwork()
    t.test_predefine_run()
    t.test_random_run()