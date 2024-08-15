def show(*args, **kwargs):
    return kwargs

s1 = show(name='john smit')
print(s1)

print(s1.get('name'))
print(s1['name'])