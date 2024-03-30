def counter():
    y = 0
    while True:
        y += 1
        yield y

        
# counter()
views = counter()
print(next(views))
print(next(views))
