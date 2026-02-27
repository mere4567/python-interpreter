import code
import sys

class PythonInterpreter:
    def __init__(self):
        self.locals = {}

    def execute(self, code):
        try:
            exec(code, self.locals)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    def repl(self):
        print('Entering REPL mode. Type "exit()" to exit.')
        code.interact(local=self.locals)

    def run_file(self, filename):
        try:
            with open(filename, 'r') as file:
                code = file.read()
                self.execute(code)
        except FileNotFoundError:
            print(f'File {filename} not found.')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    interpreter = PythonInterpreter()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        interpreter.repl()