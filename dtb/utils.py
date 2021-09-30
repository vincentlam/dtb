# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import json
from functools import reduce


# %%
def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

def deep_set(dictionary, keys, value):
    d = dictionary
    keys = keys.split('.')
    latest = keys.pop()
    for key in keys:
        d = d.setdefault(key, {})
    d[latest] = value

paths = []
def get_paths(dictionary, parent_path=''):
    global paths
    for k, v in dictionary.items():
        current_path = f"{parent_path}.{k}" if parent_path else k
        if isinstance(v, dict):
            get_paths(v, current_path)
        else:
            paths.append(current_path)
    return paths


# %%
target = {}
records = []
with open('./FormReport.json','r') as f:
    for line in f:
        records.append(json.loads(line))

for record in records:
    for path in get_paths(record):
        record_value = deep_get(record, path)
        target_value = deep_get(target, path)
        if not target_value:
            deep_set(target, path, record_value)
        else:
            if len(str(record_value)) > len(str(target_value)):
                deep_set(target, path, record_value)


with open('./combined_FR.json', 'w') as f:
    f.write(json.dumps(target))