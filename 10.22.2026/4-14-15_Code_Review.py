## PEP 8 – Style Guide for Python Code

" URL: https://peps.python.org/pep-0008/"



# Indentation: Use 4 speces for identention level.

# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


## Line Length
## PEPs 8 Recomends withre comments less than 72 characters per line.
# 

## Blank Lines
# For example, if you have five lines of code that build a list and then another 
# three lines that do something with that list, it’s appropriate to place a
# blank line between the two sections. 

## Other Style Guidelines


