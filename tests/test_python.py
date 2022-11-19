import yni

txt = """
.set_is_list:0

#test
[
    os: python(os, system, bash)
]
"""

yn = yni.Yni()
d = yn.from_string(txt)
print(d.test.os) # your operating system