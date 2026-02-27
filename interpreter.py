class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate(self, expression):
        # Simplified evaluation logic
        try:
            result = eval(expression, {}, self.variables)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def assign(self, var_name, value):
        self.variables[var_name] = value

    def clear(self):
        self.variables.clear()

if __name__ == "__main__":
    interpreter = Interpreter()
    while True:
        try:
            user_input = input(">> ")
            if user_input.lower() == 'exit':
                break
            print(interpreter.evaluate(user_input))
        except EOFError:
            break
