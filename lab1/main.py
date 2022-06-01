from cache import LRUCache

#%% Пример 1

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse'))  
cache.rem('Walter')
print(cache.get('Walter')) 

print(cache)

#%% Пример 2

cache = LRUCache(3)

cache.set('A', 'B')
cache.set('C', 'D')
cache.set('E', 'F')

cache.get('A')
cache.get('E')
cache.set('G', 'H') 

print(cache) 