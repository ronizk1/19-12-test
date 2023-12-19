# # Flag to track whether a function in the simp module has been called
_simp_function_called = False

# def simp_function():
#     global simp_module_called
#     simp_module_called = True
#     # Your simp function implementation here


def add_numbers(num1,num2):
    result = num1 + num2
    return result

def subtruct_numbers(num1,num2):
    result = num1 - num2
    return result

def set_simp_function_called():
    global _simp_function_called
    _simp_function_called = True

def is_simp_function_called():
    return _simp_function_called