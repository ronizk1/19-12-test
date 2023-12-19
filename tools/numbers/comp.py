# # Import the simp module
# import simp

# def comp_function():
#     if not simp.simp_module_called:
#         raise Exception("Cannot call functions in comp module before calling at least one function in simp module")
    
#     # Your comp function implementation here


def sumofdigits(number):
    # if not simp.is_simp_function_called():
    #     raise Exception("Cannot call functions in comp module before calling at least one function in simp module")
    # Convert the number to a string to iterate through its digits
    str_number = str(number)
    # Sum the individual digits
    digit_sum = sum(int(digit) for digit in str_number)
    return digit_sum

def ispal(number):
    # Convert the number to a string
    # if not simp.is_simp_function_called():
    #     raise Exception("Cannot call functions in comp module before calling at least one function in simp module")
    str_number = str(number)
    
    # Check if the string is equal to its reverse
    return str_number == str_number[::-1]