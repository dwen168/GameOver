# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)

n = 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"fibonacci({n}) =  {fibonacci(n)} ")



# N! = N X (N-1) X (N-2) X (N-3) X .... X 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(f"factorial({n}) =  {factorial(n)} ")


def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n-1, auxiliary, target, source)

print(f"hanoi({n},A,C,B)----start")
hanoi(n,'A','C','B')
print(f"hanoi({n},A,C,B)----end")




def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return mid + 1 + binary_search(arr[mid+1:], target)

# example
target = 5
arr = [9,8,7,6,5,4,3,2,1]
print(binary_search(arr, 5))
