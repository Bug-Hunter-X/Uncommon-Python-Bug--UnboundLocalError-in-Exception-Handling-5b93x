def function_with_uncommon_error(x):
    result = None  # Initialize the variable outside the try block
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Cannot divide by non-numeric type"
    finally:
        return result # Return value regardless of exception 

# Example usage:
result = function_with_uncommon_error(0)  # Correctly catches ZeroDivisionError
print(result)  # Output: Error: Division by zero

result = function_with_uncommon_error(2)  # No error
print(result)  # Output: 5.0

result = function_with_uncommon_error("hello") # Correctly catches TypeError
print(result)  # Output: Error: Cannot divide by non-numeric type

#The addition of finally ensures result is always defined before being used globally.