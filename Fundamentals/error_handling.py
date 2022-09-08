'''
Try-Except Block: Exception class can be used for all errors, but it's good to use the specific or custom exception child class for the expected error. Examples: ZeroDivisionError, FileNotFoundError, ValueError. Multiple exception classes can be called by wrapping them in brackets. raise keyword creates a new exception class, which is then described in brackets
'''

def simple_div():
    try:
        numerator = float(input('Enter a Numerator: '))
        denominator = float(input('Enter a Denominator: '))
        result = numerator / denominator
        if numerator % 2 == 0:
            raise ValueError('Even Numerator not accepted')
        print(f'{numerator} / {denominator} = {result}')
        return result
    except ZeroDivisionError as e:
        print('An error occurred during the division:', e)
    except ValueError as e:
        print('An error occurred during input:', e)
    finally:
        print('Thank you for using the Simple Divisor')

simple_div()