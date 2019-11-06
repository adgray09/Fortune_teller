#This code has errors, debug this code to get it to run without error
#Write in the comments why it was not working
def get_list_sum(num_list):
'''Calculated the sum of a list of numbers'''
    sum = 0
    for number in num_list:
        sum += number
    print(sum)

def get_list_product(num_list):
'''calculates the product of a list of numbers'''
    product = 1
    for number in num_list:
        product *= number
        return product

num_list = [1, 5, 7, 9]
get_list_sum(num_list)
get_list_product(num_list)