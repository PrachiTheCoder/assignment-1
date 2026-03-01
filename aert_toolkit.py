# A
class StackADT:

    def __init__(self):
        self.items = []   # using list to store elements

    # Push operation (add element to top)
    def push(self, value):
        self.items.append(value)

    # Pop operation (remove top element)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is Empty"

    # Peek operation (see top element)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is Empty"

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return size of stack
    def size(self):
        return len(self.items)
if __name__ == "__main__":
       
    stack = StackADT()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top Element:", stack.peek())
    print("Popped:", stack.pop())
    print("Size:", stack.size())
    print("Is Empty:", stack.is_empty())

# B
def factorial(n):
    if n < 0:
        return "Invalid Input"
    
    
    if n == 0 or n == 1:
        return 1
    

    return n * factorial(n - 1)



print("Factorial Tests")
print("0! =", factorial(0))
print("1! =", factorial(1))
print("5! =", factorial(5))
print("10! =", factorial(10))


# NAIVE FIBONACCI
naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1   # count every function call

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)

for n in [5, 10, 20, 30]:

    naive_calls = 0
    naive_result = fib_naive(n)
    print("Naive Result:", naive_result)
    print("Naive Recursive Calls:", naive_calls)

    # memory fibonacci
    memo_calls = 0

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1   # count every function call

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
memo_calls = 0
memo_result = fib_memo(n)
print("Memoized Result:", memo_result)
print("Memo Recursive Calls:", memo_calls)

# c3
def hanoi(n, source, auxiliary, destination):
 if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks to helper rod
 hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move largest disk
 print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move n-1 disks to destination
 hanoi(n - 1, auxiliary, source, destination)


# Required Test Case
print("===== TOWER OF HANOI (N = 3) =====")
hanoi(3, 'A', 'B', 'C')


# D
def binary_search(arr, key, low, high):

    
    if low > high:
        return -1

    mid = (low + high) // 2

    
    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)
    

print("===== BINARY SEARCH TESTS =====")

arr = [1, 3, 5, 7, 9, 11, 13]

for key in [7, 1, 13, 2]:
    result = binary_search(arr, key, 0, len(arr) - 1)
    print(f"Search {key}:", result)

# Empty list test
print("Search in empty list:",
      binary_search([], 5, 0, -1))

