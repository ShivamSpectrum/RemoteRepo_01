import numpy as np
import pandas as pd

v1 = np.arange(2,21,2)
v2 = np.arange(3,31,3)
v3 = np.arange(4,41,4)

# print(f'{v1}\n{v2}\n{v3}')

df = pd.DataFrame({'T2': v1, 'T3': v2, 'T4': v3})
print(df)
