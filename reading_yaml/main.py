import yaml

with open('./reading_yaml/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

print(data)
