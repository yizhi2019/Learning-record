import pandas as pd
import numpy as np

print(pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ")))


d1 = {"name":["xiaoming","xiaohong","xiaogang"],"age":[11,26,24],"tel":[1100,1008611,10010]}
print(d1)
print("*"*50)
t1 = pd.DataFrame(d1)
print(t1)

d2 = [{"name":"xiaoming","age":12,"tel":10086},{"name":"xiaohong","age":66,"tel":1008611},{"name":"xioalan","age":22}]
t2 = pd.DataFrame(d2)
print(t2)


