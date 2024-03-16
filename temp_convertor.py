temp = int(input('Enter the temperature in Degree Celsius:'))
try:
 def degree_to_celsius(temp):
  return temp + 273.15
 print(f'Your temperature in kelvin is: {degree_to_celsius(temp)}')

except Exception as e:
  print(e)
