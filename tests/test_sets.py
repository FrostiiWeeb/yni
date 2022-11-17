import yni

txt = """
.set_is_list:0

#test
[
	tokens: {a, b}
]
"""

yn = yni.Yni()
d = yn.from_string(txt)
print(d.test.tokens) # {b, a} -> sets are not in order