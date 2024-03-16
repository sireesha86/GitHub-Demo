temp = int(input('Enter the temperature in Degree Celsius:'))
try:
 def degree_to_celsius(temp):
  return temp + 273.15
 def kelvin_to_degrees(temp):
  return temp - 273.15
  choice=print("""Choose from the options given:
                      1.Degrees to Celsius
                      2.Kelvin to Degrees""")
  if choice=='1':
   result=degree_to_celsius(temp)
  elif choice=='2':
   result=kelvin_to_degrees(temp)
  else:
   print('Enter a valid option')
   break
  print(f'Your temperature in kelvin is: {result}')

except Exception as e:
  print(e)
