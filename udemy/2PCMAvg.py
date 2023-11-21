'''print("Enter Physics Marks:")
physics = input()
print("Enter Chemistry Marks:")
chemistry = input()
print("Enter Mathematics Marks:")
maths = input()

PCMAvg = (physics + chemistry + maths) / 3

print(PCMAvg)
# OUTPUT:
    PCMAvg = (physics + chemistry + maths) / 3
  TypeError: unsupported operand type(s) for /: 'str' and 'int' )
'''

print("Enter Physics Marks:")
physics = int(input())
print("Enter Chemistry Marks:")
chemistry = int(input())
print("Enter Mathematics Marks:")
maths = int(input())

PCMAvg = (physics + chemistry + maths) / 3

print(PCMAvg)
