# argparse is a module for parsing command line arguments
# 1 positional arguments
# 2 optional arguments
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help=" first number")
    parser.add_argument("--number2", help=" second number")
    parser.add_argument("--operation", help=" operation to perform: add, sub, mul, div",
                        choices=["add", "sub", "mul", "div"], default="add")


    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1=int(args.number1)
    n2=int(args.number2)
    result=None

    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "sub":
        result = n1 - n2   
    elif args.operation == "mul":
        result = n1 * n2    
    elif args.operation == "div":
        result = n1 / n2
    else:
        print("Invalid operation")
    
    print("Result:", result)

# to make optional argument use --- before argument name

 