# Environment.py

class Environment:
    def __init__(self):
        self.scope = {}  # Dictionary to hold variable names and values
        self.symbol_table = {}  # Dictionary to hold symbol information

    def set_variable(self, name, value):
        """
        Set a variable in the environment.
        :param name: Name of the variable
        :param value: Value of the variable
        """
        self.scope[name] = value

    def get_variable(self, name):
        """
        Get a variable from the environment.
        :param name: Name of the variable
        :return: Value of the variable if exists, otherwise None
        """
        return self.scope.get(name, None)

    def set_symbol(self, name, symbol_info):
        """
        Set a symbol in the symbol table.
        :param name: Name of the symbol
        :param symbol_info: Information regarding the symbol
        """
        self.symbol_table[name] = symbol_info

    def get_symbol(self, name):
        """
        Get symbol information from the symbol table.
        :param name: Name of the symbol
        :return: Symbol information if exists, otherwise None
        """
        return self.symbol_table.get(name, None)