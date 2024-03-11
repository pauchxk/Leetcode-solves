#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibo():

    fib_num = 0
    fib_list = []
    fib_even = []
    counter = 0

    while fib_num < 4000000:

        try:
            fib_num = fib_list[counter-1] + fib_list[counter-2]
            fib_list.append(fib_num)

        except IndexError:

            try:
                fib_num += fib_list[counter-1]
                fib_list.append(fib_num)

            except IndexError:
                fib_num = 1
                fib_list.append(fib_num)

        if fib_num % 2 == 0:
            fib_even.append(fib_num)
        
        counter += 1

    total = 0

    for num in fib_even:
        total += num
    
    print(total)

fibo()