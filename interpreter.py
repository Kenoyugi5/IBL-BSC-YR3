def main():
    expression = input("Enter expression: ")
    print(calc(expression))

def calc(result):
    result = result.split()
    x = float(result[0])
    y = result[1]
    z = float(result[2])
    if result[1] == "+":
        return float(x + z)
    elif result[1] == "-":
        return float(x - z)
    elif result[1] == "*":
        return float(x * z)
    elif result[1] == "/":
        return float(x / z)
    else:
        print("Sorry, expression not recognized")

main()