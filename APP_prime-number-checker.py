def prime_checker(number):
    
    is_prime = True # bool checker if a number is prime or not 
                    # when preliminarily set as "None" it worked for is_not_prime
                    # for is_prime needs to be pre-set as "True" to detect prime numbers and print for them

    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime == True:
            print("It's a prime number")
        else:
            print("It's not a prime number")
        
    elif number == 1:
        print("It's a prime number")
    else:
        print("Enter a number larger than 0")

n = int(input("Check this number: "))
prime_checker(number=n)

