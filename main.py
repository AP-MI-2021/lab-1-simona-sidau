'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if n<2:
    return False
  else:
    for i in range (3, n, 2):
      if n%i==0:
        return False
  return True

assert is_prime(7)==True
assert is_prime(2)==True
assert is_prime(1)==False
assert is_prime(29)==True
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  produs = 1
  for i in lst:
    produs = produs * i
  return produs

  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  r = x % y
  while r:
    x = y
    y = r
    r = x % y
  return y

assert get_cmmdc_v1(25, 5) == 5
assert get_cmmdc_v1(1, 13) == 1
assert get_cmmdc_v1(125, 75) == 25
assert get_cmmdc_v1(130, 17) == 1
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''

def get_cmmdc_v2(x, y):
  # codul vostru aici
  while x != y:
    if(x > y):
      x = x - y
    else:
      y = y - x
  return x
assert get_cmmdc_v2(25, 5) == 5
assert get_cmmdc_v2(1, 13) ==1
assert get_cmmdc_v2(125, 75) == 25
assert get_cmmdc_v2(130, 17) == 1

def main():
  # interfata de tip consola aici
  shouldRun = True
  while shouldRun:
    print("1. Determinati daca un numar este prim")
    print("2. Calculati produsul a n numere naturale")
    print("3. CMMDC varianta 1")
    print("4.CMMDC varianta 2")
    print("x. Exit")

    optiune = input("Alegeti optiunea ")
    if optiune == "1":
      a = int (input("Introduceti numarul "))
      if(is_prime(a)):
        print("Numarul dat este prim")
      else:
        print("Numarul dat nu este prim")
    elif optiune == "2":
      n = int (input("Introduceti numarul de numere "))
      lst = []
      print("Introduceti numerele")
      for i in range(n):
        lst.append(int(input()))
      print(get_product(lst))
    elif optiune == "3":
      a = int (input("Introduceti primul numar "))
      b = int (input("Introduceti al doilea numar "))
      print(get_cmmdc_v1( a, b))
    elif optiune == "4":
      a = int(input("Introduceti primul numar "))
      b = int(input("Introduceti al doilea numar "))
      print(get_cmmdc_v2(a, b))
    elif optiune == "x":
      shouldRun = False
    else:
      print("Reincercati")

if __name__ == '__main__':
  main()
