import pandas as pd
print(pd.__version__)
x=pd.read_json(r'D:\python_training\4thDay\write_Json.json')
print(x)
print("Data Frame")
print(pd.DataFrame(x))