from calculator import solve

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