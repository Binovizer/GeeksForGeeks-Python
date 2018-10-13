# MATHS
# from print_table import printTable
# from series_ap import ap
# from series_gp import gp
# from closest_no import closest_number
# from math import floor
# from armstrong import is_armstrong, is_armstrong_number;
# from sum_of_digit_pallindrome import sum_of_digit_is_pallindrome
# from reverse_digits import reverse
# from kth_digit import kth_digit
# from binary_to_decimal import bin_to_dec
# from jumping_no import is_jumping_no
# from factorial import factorial
# from npr import npr
# from ncr import ncr
# from largest_prime_factor import largest_prime_factor
# from perfect_no import is_perfect_no
# from perfect_no import optimised_is_perfect_no;
# from pair_cube_count import pair_cube_count;
# from prime_number import is_prime
# from sieve_of_eratosthenes import generate_primes
# from sum_of_primes import sum_of_primes

# PUZZLES
# from overlapping_rectangles import are_overlapping
# from trailing_zeros import trailing_zeros
# from angle_between_hour_minute import angle_between_hour_minute
# from triangular_no import is_triangular_no
# from nth_even_fib_no import nth_even_fib_no
# from last_2_digit_fib import last_2_digit

# ARRAYS
# from arrays.operating_an_array import searchEle
# from arrays.second_largest import second_largest
# from arrays.reverse import custom_rev
# from arrays.rotate import rotate
# from arrays.remove_duplicates_sorted import remove_duplicate
# from arrays.count_possible_triangles import count
# from arrays.leaders import leaders
# from arrays.leaders import leaders_optimised
# from arrays.min_distance_xy import min_distance
# from arrays.sorted_subseq import seq
# from arrays.maximum_sub_array import max_sub_array
# from arrays.maximum_sub_array import max_sub_array_sum
# from arrays.majority_element import majority_element
# from arrays.wave_array import wave_array
# from arrays.maximum_index import max_index
# from arrays.maximum_index import max_index_optimized
# from arrays.max_sum_path import max_sum_path
# from arrays.product_array import product_array
# from arrays.print_duplicates import print_duplicates
# from arrays.buy_sell_stocks import buy_sell_stocks
# from arrays.trapping_rain_water import water
# from arrays.pair_with_given_sum import find_pairs
# from arrays.chocolate_distribution_problem import find_diff
from arrays.longest_subsequence import get_length

# MATHS
# printTable(9);
# print(gp(1, 2, 2))

# closest_number(9, 2);
# print(is_armstrong(input()))
# print(is_armstrong_number(int(input())))
# print(sum_of_digit_is_pallindrome(98))
# print(reverse(371))
# print(bin_to_dec(input()))
# print(is_jumping_no(434))
# print(factorial(5))
# print(npr(10, 4))
# print(largest_prime_factor(69))
# print(is_perfect_no(21))
# print(optimised_is_perfect_no(6));
# print(pair_cube_count(28))
# print("Yes" if is_prime(24) else "No")
# print(sum_of_primes(10))

# PUZZLES
# print(are_overlapping(rect1, rect2))
# print(trailing_zeros(50))
# print(nth_even_fib_no(5))
# print(last_2_digit(0))

# ARRAYS
# print(searchEle([1,2,3,4,5], 10))
# print(second_largest([1,2,3,4,5]))
# print(rotate([1, 2, 3, 4, 5], 2))
# arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# n = remove_duplicate(arr)
# for i in range(0, n):
#     print (" %d "%(arr[i]), end = " ")
# print(count([4, 6, 3, 7]))
# print(leaders([1, 4, 3, 2]))
# print(leaders_optimised([1, 4, 3, 2]))
# print(
#     min_distance([
#         98, 78, 10, 12, 59, 37, 45, 18, 1, 56, 37, 14, 3, 32, 85, 10, 69, 89,
#         29, 93, 44, 16, 26, 13, 50, 75, 79, 21, 20, 33, 55, 17, 63, 64, 80, 21,
#         52, 24, 90, 52, 80, 26, 18, 34, 57, 2, 95, 25, 42, 23, 17, 85, 39, 94,
#         50, 40, 21, 28, 12, 40, 61, 67, 9, 23, 30, 88, 95, 34, 64, 85, 85, 95,
#         62, 54, 28, 19, 55, 22, 95, 49, 97, 64, 33
#     ], 34, 56))
# print(seq([1, 1, 3]))
# print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
# print(max_sub_array([-2, -3, 4, -1, -2, 1, 5, -3]))
# print(majority_element([1, 2, 3, 3, 1, 3, 3]))
# print(wave_array([5,7,3,2,8]))
# print(max_index([3, 5, 4, 2]))
# print(max_index_optimized([3, 5, 4, 2]))
# print(max_sum_path([2, 3, 7, 10, 12, 15, 30, 34], [1, 5, 7, 8, 10, 15, 16, 19]))
# print(product_array([10, 3, 5, 6, 2]))
# print(print_duplicates([2, 3, 1, 2, 3]))
# print(buy_sell_stocks([23, 13, 25, 29, 33, 19, 34, 45, 65, 67]))
# print(buy_sell_stocks([100, 180, 260, 310, 40, 535, 695]))
# print(water([6, 9, 9]))
# print(find_pairs([1, 3, 4, 7, 9, 12, 15, 16], 96))
# print(find_diff([7, 3, 2, 4, 9, 12, 56], 3))
print(get_length([86, 77, 15, 93, 35, 86, 92, 49, 21, 62, 27, 90, 59, 63, 26, 40, 26, 72, 36, 11, 68, 67,
                  29, 82, 30, 62, 23, 67, 35, 29, 2, 22, 58, 69, 67, 93, 56, 11, 42, 29, 73, 21, 19, 84,
                  37, 98, 24, 15, 70, 13, 26, 91, 80, 56, 73, 62, 70, 96, 81, 5, 25, 84, 27, 36, 5, 46,
                  29, 13, 57, 24, 95, 82, 45, 14, 67, 34, 64, 43, 50, 87, 8, 76, 78, 88]))
print(get_length([]))


