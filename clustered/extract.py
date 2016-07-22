import pandas as pd
import json

df = pd.read_csv('jupyter.csv')
dct = df.to_dict()

with open('jjs.js','w') as f:
    f.write('var addressPoints = '+json.dumps([[ll,l,u] for u,l,ll in zip(dct['user'].values(),dct[' longitude'].values(), dct[' latitude'].values())], indent=2)+';')
