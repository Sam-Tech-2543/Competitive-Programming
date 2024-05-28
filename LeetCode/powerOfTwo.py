import re

txt = "The rain in Spain"
x=bool(re.match(r"^((0)*+1(0)*)$", input()))
print(x)