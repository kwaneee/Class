def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

#first second and third are local variables, as are parameters a,b,c and 
#parameters and local variables are created in the activation frame when the assigment statemntstsa re executed
# BUT the parameters and local variables dissapear when quadratic reurns and its activation frame is removed
# SO when the function returns, the activation frame is removed