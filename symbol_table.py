class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def set(self, name, value):
        if name in self.symbols:
            raise Exception(f"Symbol '{name}' already defined.")
        self.symbols[name] = value

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise Exception(f"Symbol '{name}' not found.")

    def define_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"SymbolTable(symbols={self.symbols})"


class SemanticAnalyzer:
    def __init__(self):
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope

    def enter_scope(self):
        new_scope = SymbolTable()
        new_scope.define_parent(self.current_scope)
        self.current_scope = new_scope

    def exit_scope(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("No parent scope to exit to.")

    def declare_variable(self, name, value):
        self.current_scope.set(name, value)

    def get_variable(self, name):
        return self.current_scope.get(name)

    def __repr__(self):
        return f"SemanticAnalyzer(current_scope={self.current_scope})"


# Example usage:
if __name__ == '__main__':
    analyzer = SemanticAnalyzer()
    analyzer.declare_variable('x', 10)
    print(analyzer.get_variable('x'))  # Outputs: 10
    analyzer.enter_scope()
    analyzer.declare_variable('y', 20)
    print(analyzer.get_variable('y'))  # Outputs: 20
    analyzer.exit_scope()
    print(analyzer.get_variable('x'))  # Outputs: 10