import ast
import copy
def convert2Expression(Expr):
        Expr.line = 0
        Expr.offset = 0
        result = ast.Expression(Expr.value, line=0, offset = 0)

        return result
def exec_with_return(code):
    code_ast = ast.parse(code)

    start_ast = copy.deepcopy(code_ast)
    start_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]
    
    exec(compile(start_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convert2Expression(last_ast.body[0]), "<ast>", "eval"),globals())
    else:
        print(3)
        exec(compile(last_ast, "<ast>", "exec"),globals())
