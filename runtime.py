class Runtime:
    def __init__(self):
        # Initialize the runtime environment
        self.variables = {}

    def execute_statement(self, statement):
        # Handles execution of a single statement
        exec(statement, self.variables)

    def execute_expression(self, expression):
        # Handles execution of an expression
        return eval(expression, self.variables)

    def set_variable(self, name, value):
        # Set a variable in the runtime environment
        self.variables[name] = value

    def get_variable(self, name):
        # Retrieve a variable from the runtime environment
        return self.variables.get(name)

    def clear(self):
        # Clear all variables in the runtime
        self.variables.clear()

    def run_code(self, code):
        # Run a block of code
        exec(code, self.variables)

# Example of a simple usage:
if __name__ == '__main__':
    runtime = Runtime()
    runtime.set_variable('x', 10)
    print(f'Value of x: {runtime.get_variable('x')}')  # Should output 10
    try:
        runtime.execute_statement('print(x * 2)')  # Outputs 20
    except Exception as e:
        print(f'Error: {e}')  # Handles any execution errors

    # Running a piece of code
    runtime.run_code('for i in range(5): print(i)')

    # Clear variables
    runtime.clear()