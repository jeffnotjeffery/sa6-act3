strings = ['brioche', 'wheat', 'white', 'pumpernickel', 'sesameseed']

stringsorter = sorted(strings, key=lambda x: (len(x), x))

print(stringsorter)