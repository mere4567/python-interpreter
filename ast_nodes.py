class ASTNode:
    pass

class Module(ASTNode):
    def __init__(self, body):
        self.body = body

class FunctionDef(ASTNode):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

class Assign(ASTNode):
    def __init__(self, targets, value):
        self.targets = targets
        self.value = value

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Call(ASTNode):
    def __init__(self, func, args):
        self.func = func
        self.args = args

# Additional AST node class definitions can go here.
