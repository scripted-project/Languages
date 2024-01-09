# Variables
Variables are made up of 3 things:
- A identifier
- A value
- A type
## Parts of a variable
### Identifiers
**Identifiers** are the names of the variables. These identifiers can be used to access variable values.
### Values
Variable **values** are the actual values of the variables.
### Types
Variable **types** are the type of variables. More on that [here](#types-1).
## Usage
- Creating variables: `var [type] [identifier] = [value]`  
- Deleting variables: `del var [identifier]`  
- Changing variables: `[identifier] = [value]` (make sure the value complies with the type)  
- Accessing variables: `[...][identifier][...]`

Identifiers return the value of the variable
# Constants
Constants are like variables in most ways. However, you cannot change their value.  
Creating constants: `const [type] [name] = [value]`
# Types
A type is a type of value.
## Character (char)
A single character.  
example: `var char character = 'a'`
## String (str)
A array of characters  
example: `var str string = "abcdefg"`
## Integer (int)
A whole number.  
example: `var int integer = 1`  
note: Characters are actually integers representing characters.
### List (list)
A List of values or variables
example: `var list list_example = ["abc", 1, 'a', ["list"]]`
# What now?
[Next](4_base-functions.md)  
[Home](1_getting-started.md)  
[Previous](3_variables.md)