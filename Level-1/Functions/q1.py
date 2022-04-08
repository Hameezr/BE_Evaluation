def fibonacci(num):
    sum1 = 1
    sum2 = 1
    if num == 0 or num == 1:
        print(num)
    elif num>1:
        next = 0
        print(sum1, sum2, end=' ')
        for x in range(num-2):
            next = sum1 + sum2
            print(next, end=' ')
            sum1 = sum2
            sum2 = next
    else: 
        print('Not a valid number')

def fibonacci_recursive(num):
    if num == 0 or num == 1: 
        return num
    else: 
        return fibonacci_recursive(num-1) + fibonacci_recursive(num - 2)

def main():
    choice = int(input('Choose the function, Enter the number\n1. Iterative Function\n2. Recursive Function\n'))
    fib_input = int(input("Enter a number: "))
    if (choice == 1): 
        fibonacci(fib_input)
    else: 
        for index in range(fib_input):
            print(fibonacci_recursive(index))
    
if __name__ == "__main__":
    main()
