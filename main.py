import sys

# def factorial(n):
# def permutations(n, k):

def smartpermutation(n,k):
  # since we know k is always 2
  return n * (n-1)

def countArrayElems(arr):
  counts = {}
  for el in arr:
    if el in counts:
        counts[el] += 1
    else:
        counts[el] = 1
  return counts


lines = sys.stdin.readlines() # or read() to read the whole thing no line separated

nExperiments = int(lines[0])
lines = lines[1:] 

for i in range(nExperiments):
  nNumbers = int(lines[0])
  numbers = map(int, lines[1].split()) 
  lines = lines[2:]
  counts = countArrayElems(numbers)
  total = 0
  for count in counts.values():
    if count <= 1:
      continue
    else:
      total = total + smartpermutation(count, 2)  
  print total