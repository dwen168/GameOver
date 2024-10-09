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




def binary_search(arr, target, low, high):
    if low > high:
        return -1  # not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # found return index
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # search right part
    else:
        return binary_search(arr, target, low, mid - 1)   # search left part

# example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)  
