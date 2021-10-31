#%%
import numpy as np
import pandas as pd
A = np.random.randint(1, 3, size=(3, 2))
print(A)
B = np.random.randint(1, 3, size=(3, 2))
print(B)
mse = np.mean(np.square(np.subtract(A, B)))
print(mse)
# %%
rmse = np.sqrt(mse)
print(rmse)
def mape(A, B):
    mape = np.mean(np.abs((A - B)/A))*100
    return mape
mape(A, B)
# %%
p_t = np.where(y==1, p, (1-p))
alpha_t = np.where(y==1, alpha, (1-alpha))
CE = -alpha_t*np.log(p_t)
FL = -alpha_t*((1 - p_t)**gamma)*np.log10(p_t)

# %%
np.array([1, 2, 3, 4, 5]) + np.array([6, 7, 8, 9, 10])
# %%
np.array([1, 2, 3, 4, 5]) * 2
np.eye(1)
# %%
arr = np.array([[1],[2],[3]])
arr_2 = np.array([[1, 2]])
arr_3 = arr * arr_2
# %%
arr_3.shape

# %%
np.random.randint(6, 6, 8).reshape(-1, 10)

# %%
np.NAN == np.NINF 
# %%
from yaml import load, FullLoader

def yaml_to_df(path_to_yaml):
    with open(path_to_yaml) as yf:
        yf_contents = load(yf, Loader=FullLoader)
    yaml_df = pd.json_normalize(yf_contents)
    yaml_df.unstack()
    return yaml_df
# %%
from os import getcwd, path

yaml_file = path.join(getcwd(), "/Users/dan/documents/projects/recipe-app-api", "docker-compose.yml")
yaml_to_df(yaml_file)
# %%
