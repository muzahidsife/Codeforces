a = int(input())
b = input()[1:].split()
c = input()[1:].split()


if len(set(b+c))==a:
      print("I become the guy.")
else:
      print("Oh, my keyboard!")