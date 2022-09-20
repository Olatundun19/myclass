fruits = ['mango','pine-apple','apple','lemon','grape']

fruits.append('orange')
fruits.append('watermelon')

fruits.insert(0,'guava')

s = fruits.copy()

foods = ['rice','beans','yam']
foods.extend(fruits)

foods.remove('watermelon')

foods.pop()

print(foods)