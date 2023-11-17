import requests

bases_available = ["2", "8", "10", "16"]

min = ""
while not min.isdigit() or int(min) < -1000000000:
  min = input("enter minimum here => ")
  
max = ""  
while not max.isdigit() or int(max) > 1000000000 or max <= min:
  max = input("enter maximum here => ")

amount = ""
while not amount.isdigit() or int(amount) < 1 or int(amount) > 10000:
  amount = input("Enter the amount of numbers to generate (1, 10,000) => ")

baseType = ""
while baseType not in bases_available or not baseType.isdigit():
  baseType = input(f"Enter base here ({', '.join(bases_available)}) => ")

r = requests.get('https://www.random.org/integers', params = {
  'num': amount,
  'min': min,
  'max': max,
  'col': 1,
  'base': int(baseType),
  'format': 'plain',
  'rnd': 'new'
})

htmlText = r.text

if "Error" in htmlText:
  print(htmlText)
  exit()

print(htmlText.strip().replace("\n", ", "))