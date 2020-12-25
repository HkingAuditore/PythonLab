import zhihuapi as api

with open('cookie') as f:
    api.cookie(f.read())

data = api.user('huang-xiang-88-12').profile()
print(data)