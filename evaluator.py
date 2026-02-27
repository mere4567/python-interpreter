import ast

class ASTEvaluator(ast.NodeVisitor):
    def __init__(self):
        self.variables = {}

    def visit_Number(self, node):
        return node.n

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        else:
            raise NotImplementedError(f"Operation {ast.dump(node.op)} not implemented")

    def visit_Assign(self, node):
        value = self.visit(node.value)
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables[target.id] = value
                return value

    def visit_Name(self, node):
        return self.variables.get(node.id, None)

    def visit_Expr(self, node):
        return self.visit(node.value)

    def evaluate(self, code):
        tree = ast.parse(code)
        return self.visit(tree)

# Example usage:
# evaluator = ASTEvaluator()
# evaluator.evaluate("x = 1\ny = x + 2\nprint(y)")

