'''def tower_builder(n_floors):
    # build here
    tower=[]
    for i in range(n_floors):
      blank=n_floors-i-1
      x=' ' * blank + '*' * (i * 2 + 1) + ' ' * blank
      tower.append(x)
    return tower
print(tower_builder(3))'''
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1)/n for i in range(1, n+1)]
#但是换行到现在都没解决 google能力不行 
print(tower_builder(5))