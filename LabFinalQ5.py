

import ast
import inspect

class CustomNodeTransformer(ast.NodeTransformer):
    def visit_Assign(self, node):
        print("\nvisit_Assign")
        print(node.__dict__)
        print(node.targets[0].__dict__)
        print(node.value.__dict__)
        return node
    def visit_AugAssign(self, node):
        print("\nvisit_AugAssign")
        print(node.__dict__)
        print(node.target.__dict__)
        print(node.value.__dict__)
        return node

nodes = ast.parse(''' 
def ab(z, y):
    return math.log2(z)/math.log2(y)
def cd(y,a,c,n):
    return y*n/a*c
def me(a,b,c,d):
    a=ab(a,b)
    b=ab(b,a)
    c=ab(c,d)
    d=ab(c,d)
    return cd(a,b,c,d)
p=10
q=5
r=3
s=1
me(p,q,r,s)
''')



names = sorted({node.id for node in ast.walk(nodes) if isinstance(node, ast.Name)})
print(names)
CustomNodeTransformer().visit(nodes)