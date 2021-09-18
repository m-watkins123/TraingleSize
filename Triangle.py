
def classifyTriangle(a,b,c):
A = input ("Enter side A")
B = input ("Enter side B")
C = input ("Enter side C")
    try:
      input("Select number between 0 to 200:")
    while True:
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    and
    a a <= 0 or b <= b or c <= 0:
        return 'InvalidInput' 
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
 
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotTriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
