import math
import sys
import inspect
def my_tracer(frame, event, arg):
	function_code = frame.f_code
	function_name = function_code.co_name
	lineno = frame.f_lineno
	vars = frame.f_locals
	source_lines, starting_line_no = inspect.getsourcelines(frame.f_code)
	loc = f"{function_name}:{lineno} {source_lines[lineno -starting_line_no].rstrip()}"
	vars = ", ".join(f"{name} = {vars[name]}" for name in vars)
	print(f"{loc:50} ({vars})")
	return my_tracer

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

sys.settrace(my_tracer)
me(p,q,r,s)
sys.settrace(None)

