# env(..., ...) needs dotenv module

import yni

txt = """
#test
[
	token: env(./tests/.env, token)
]
"""

yn = yni.Yni()
d = yn.from_string(txt)
print(d.test.token) # a