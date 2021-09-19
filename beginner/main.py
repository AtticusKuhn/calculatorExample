def isNumber(num:str)-> bool:
    try:
        int(num)
        return True
    except:
        return False
def isOperator(char:str)-> bool:
    return char in ["+", "-"]

def solve(problem: str) -> int:
    accumulator:int = 0
    for (index, character) in enumerate(problem):
        if isNumber(character):
            accumulator =  int(str(accumulator) + character)
        elif isOperator(character):
            if(character == "+"):
                print("going down + path, and accumulator=", accumulator)
                print("solve(problem[index+1:]) = ",solve(problem[index+1:]))
                accumulator += solve(problem[index+1:])
                break
            elif(character == "-"):
                accumulator -= solve(problem[index+1:])
                break
        else:
            raise ValueError(f'unknown character in problem "{character}"')
    return accumulator




def main():
    while True:
        print("give me a math problem to compute")
        user_input = input("> ")
        try:
            solution = solve(user_input)
            print(f'{user_input} = {solution}')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()