def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Cannot divide by non-numeric type"

# This will raise an UnboundLocalError if the exception is not handled properly.

# Example usage:
result = function_with_uncommon_error(0)  # Correctly catches ZeroDivisionError
print(result)  # Output: Error: Division by zero

result = function_with_uncommon_error(2)  # No error
print(result)  # Output: 5.0

result = function_with_uncommon_error("hello") # Correctly catches TypeError
print(result)  # Output: Error: Cannot divide by non-numeric type

#Example for the UnboundLocalError, the result variable is not defined outside the try block. 
#The try block might raise an exception, therefore result is not defined in the global scope
print(result)