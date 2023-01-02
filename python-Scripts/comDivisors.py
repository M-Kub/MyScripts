comDiv = []
divisors = []

def inputNumber(message):
    while True:
        userInput = input(message)
        return userInput


def commonDivs(*args):
    while True:
        numbers = inputNumber("Please enter a number: ")
        if numbers.isdigit():
            div = [i for i in range(
                1, int(numbers) + 1) if int(numbers) % i ==0]
            divisors.append(numbers)
            comDiv.append(div)
        elif numbers.isalpha():
            print("Not a number! Please try again.")
            continue
        elif numbers == "":
            break


commonDivs()


for i, v in enumerate(divisors):
    print(f"The divisors of {divisors[i]} are {comDiv[i]}.")
print(f"The common divisors are: {set.intersection(*map(set, comDiv))}")
