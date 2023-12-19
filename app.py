from tools.numbers import simp , comp
from tools.col import myzip

def main():
    
    # Example usage
    num1 = 10
    num2 = 5
    number = 222
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    # Adding two numbers using the function from the simp module
    sum_result = simp.add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")

    # Subtracting two numbers using the function from the simp module
    difference_result = simp.subtruct_numbers(num1, num2)
    print(f"The difference of {num1} and {num2} is: {difference_result}")
    
     # Set the flag to indicate that a function in the simp module has been called
    simp.set_simp_function_called()

    # Wrapper function to call functions in the comp module
    comp_wrapper(number)
    
    # Using the custom myzip function
    result = list(myzip(list1, list2))
    print(result)
    
    
def comp_wrapper(number):
    # Check if a function in the simp module has been called
    if not simp.is_simp_function_called():
        raise Exception("Cannot call functions in comp module before calling at least one function in simp module")

    # Call functions in the comp module
    sum_of_digits = comp.sumofdigits(number)
    print(f"Sum of digits of {number} is: {sum_of_digits}")

    ispal_result = comp.ispal(number)
    print(f"{number} is a palindrome: {ispal_result}")
    
    
if __name__=="__main__":
    main()