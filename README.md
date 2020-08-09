# session4-Gaju27
session4-Gaju27 created by GitHub Classroom

# Floats: Coercing to Integers
  
  Different way to configure the data loss
  
  like Truncation, floor, ceiling, round
  
  Truncation --> remove the floating part and returns the integer
  
  Floor --> Largest integer less than or equal to the number
  
  Ceiling --> Smallest integer greater than or equal to number
	
# Floats: Rounding
  Rouding is the Built-in function in python
  
# Decimals
  
  Refect Pep 327
  
  Decimal “is based on a floating-point model which was designed with people in mind, and necessarily has a paramount guiding principle – computers must provide an arithmetic that works in the same way as the arithmetic that people learn at school.” – excerpt from the decimal arithmetic specification.
  
# Decimals: Constructors and Contexts
  
  In accordance with the standard, the decimal module provides two ready to use standard contexts, BasicContext and ExtendedContext. The former is especially useful for debugging because many of the traps are enabled:
  
  ctx=decimal.getcontext() --> this is global contexts
  
  ctx.prec
  
  ctx.rouding --> different way of rounding can be seen here
  
  The Decimal class is in the module decimal as below
	
  from decimal import Decimal
	
  Type of decimals
  
	  integes  --> a = Decimal(10)
	  string   --> a = Decimal('10')
	  tuple    --> a = Decimal((1,(3,1,4,1,5),-1)
	  
# Context Precision and the Constructors
  Context precision affects mathematical operations
  Context precision does not affect the constructor  
  
# Decimals: Math Operations
  Some arithmetic operator dont work the same as float or integers
  
  
# Decimals: Performance Considerations
  There are some drawbacks to the Decimal class vs the float class
 
 Those are: 
 
	1. Not as easy to code: construction vis strings or tuples
	2. Not all mathematical function that exist int he math module have a Decimal counterpart
	3. More memory overhead
	4. Performance: much slower than float
	
	
# Complex Numbers
  
  Complex numbers are represented as k+3j 
  
  here k is real part and j is imaginary part
  
  these are stored as float we must be very careful while testing
  
  Arimaetic Operations --> Support (+,-,/,*,**)
  
  Real and complex numbers can be mixed
  
  // and % operators dont support complex numbers
  
  == and != operator are supported
  
  comparision operators not supported
  
  function in the math module will not work hence we have to use cmath module

  Some instance properites and methods are: 
 
  	1. .real 				    --> returns the real part
  	2. .imag 				    --> returns the imaginary part
    3. .conjugate()			--> returns the complex conjugate

	
# Booleans
 
 Python has a concrete bool class that is used to represent boolean values
 
 bool is subclass of the int class and it inherist all the properites of int class
 
 where True is 1 and False is 0

# Booleans: Precedence and Short-Circuiting
  
  The boolean Operator: not and, or
  
  Operator precidence: BODMAS



# Final output

C:\Users\gajanana_ganjigatti\Documents\Gaju_data\github\session4-Gaju27>pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.7.0b3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- c:\users\gajanana_ganjigatti\appdata\local\programs\python\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\gajanana_ganjigatti\Documents\Gaju_data\github\session4-Gaju27
collected 14 items

test_session4.py::test_readme_exists PASSED                                                                      [  7%]
test_session4.py::test_readme_contents PASSED                                                                    [ 14%]
test_session4.py::test_readme_proper_description PASSED                                                          [ 21%]
test_session4.py::test_readme_file_for_formatting PASSED                                                         [ 28%]
test_session4.py::test_indentations PASSED                                                                       [ 35%]
test_session4.py::test_invalid_real_Exception_provides_relevant_message PASSED                                   [ 42%]
test_session4.py::test_addition PASSED                                                                           [ 50%]
test_session4.py::test_in_equality PASSED                                                                        [ 57%]
test_session4.py::test_class_repr PASSED                                                                         [ 64%]
test_session4.py::test_function_name_had_cap_letter PASSED                                                       [ 71%]
test_session4.py::test_less_than_equal PASSED                                                                    [ 78%]
test_session4.py::test_less_than PASSED                                                                          [ 85%]
test_session4.py::test_and_assertion PASSED                                                                      [ 92%]
test_session4.py::test_or_assertion PASSED                                                                       [100%]

================================================= 14 passed in 0.08s ==================================================



and,
or,
repr,
str,
add,
eq,
float,
ge,
gt,
invertsign,
le,
lt,
mul,
sqrt,
bool,


