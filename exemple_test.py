#Pytest


#1
# import pytest # для всех тестов
# from main import positive_or_negative
#
#
# @pytest.mark.parametrize('x', [15, -1.2, 0.4])
# def test_positive_or_negative_if_positive(x):
#     assert positive_or_negative(x) == 'positive'






#2
# from main import even_or_odd
#
# @pytest.mark.parametrize('x', [-4, 0, 5])
# def test_even_or_odd(x):
#     assert even_or_odd(x) == 'even'





#3
# from main import count_digits
# def test_count_digits():
#     assert count_digits(12345) == 5
#     assert count_digits(-9876) == 4
#     assert count_digits(0) == 1







#4
# from main import sum_list
# def test_sum_list():
#     assert sum_list([1, 3, 2, 6, 4]) == 16
#     assert sum_list([2, 2, 3, 8]) == 15
#     assert sum_list([]) == 0







#5
# from main import sum_number
# def test_sum_number():
#     assert sum_number('12,34,56') == 102










# Unittest

#1
# import unittest
# from unittest import TestCase, main
# from main import convert_date_to_tuple
#
#
# class TestDateConversion(unittest.TestCase):
#     def test_convert_date_to_tuple(self):
#         date = '2025-12-31'
#         expected_result = ('31', '12', '2025')
#         self.assertEqual(convert_date_to_tuple(date), expected_result)
#
#
# if __name__ == '__main__':
#     unittest.main()







#2
# import unittest
# from main import sum_of_list_elements
#
#
# class TestSumOfListElements(unittest.TestCase):
#     def test_sum_of_list_elements(self):
#         lst = ['1', '2', '3', '4', '5']
#         self.assertEqual(sum_of_list_elements(lst), 15)
#
#
# if __name__ == '__main__':
#     unittest.main()








#3
# import unittest
# from main import divide_sum_of_halves
#
#
# class TestDivideSumOfHalves(unittest.TestCase):
#     def test_divide_sum_of_halves(self):
#         self.assertEqual(divide_sum_of_halves([1, 2, 3, 4, 5, 6]), 0.4)
#         self.assertEqual(divide_sum_of_halves([10, 20, 30, 40, 50, 60]), 0.4)
#         self.assertEqual(divide_sum_of_halves([2, 4, 6, 8, 10, 12]), 0.4)
#
#
# if __name__ == '__main__':
#     unittest.main()