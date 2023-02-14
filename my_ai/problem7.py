
print('you can calculate the area of square, triangle and rectangle')

shape = input('enter the shape you want to calculate: ').lower()

def area(a, b=1):
  if shape == 'square':
    return a**2

  elif shape == 'triangle':
    return (a*b)/2

  elif shape == 'rectangle':
    return (a*b)

  else:
    return None

if shape == 'square':
  length = int(input('enter the length in cm: '))
  p=area(length)
  print(f'the area of {shape} is {p}')
elif shape == 'triangle':
  base=int(input('enter the base in cm: '))
  height=int(input('enter the height in cm: '))
  p=area(base, height)
  print(f'the area of {shape} is {p}')
elif shape == 'rectangle':
  length=int(input('enter the length in cm: '))
  breath=int(input('enter the breath in cm: '))
  p=area(length, breath)
  print(f'the area of {shape} is {p}')
else:
  print('[-] you input the wrong shape')
  print(f'{shape} is not among the expected shapes')


