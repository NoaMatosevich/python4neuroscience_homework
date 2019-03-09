def is_palindrome(number):
    #number is string
    reversed_str=number[::-1]
    return reversed_str == number
    
def check_palindrome(full_number):
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    first_number = str(full_number)[2:]
    if is_palindrome(first_number):
        # add 1 and check last 5 digits if they are palindromic
        full_number2=full_number+1
        second_number = str(full_number2)[1:]
        if is_palindrome(second_number):
            # add 1 and check if middle 4 digits are palindrome
            full_number3=full_number2+1
            third_number = str(full_number3)[1:5]
            if is_palindrome(third_number):
                # add 1 and check if full number is now a palindrome
                full_number4 = full_number3+1
                if is_palindrome(str(full_number4)):
                    print(full_number)

if __name__ == '__main__':
# Question 2
    print('Question 2 solution:')
    for full_number in range(100000,1000000):
        check_palindrome(full_number)
