import ast

class ASTParser:
    def __init__(self, code):
        self.code = code

    def parse(self):
        # Parse the code into an abstract syntax tree
        tree = ast.parse(self.code)
        return tree

    def visit(self, node):
        # Visit a node in the AST
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        # Generic visitor for all nodes
        for child in ast.iter_child_nodes(node):
            self.visit(child)

    def visit_Module(self, node):
        # Visit a Module node
        print(f'Visiting Module: {node}')
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Visit a FunctionDef node
        print(f'Visiting Function: {node.name}')
        self.generic_visit(node)

    def visit_If(self, node):
        # Visit an If node
        print('Visiting If statement')
        self.generic_visit(node)  

# Example of how to use the ASTParser
if __name__ == '__main__':
    code = """
    def example_function():
        if True:
            print('Hello, World!')
    """
    parser = ASTParser(code)
    tree = parser.parse()
    parser.visit(tree)