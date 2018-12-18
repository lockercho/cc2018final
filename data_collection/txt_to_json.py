import json
import random
jokes = open('jokes.txt', 'r').read().split("\n--\n")
print(jokes)
random.seed(1024)
random.shuffle(jokes)
print(jokes)
f = open('jokes-shuffled.json', 'w')
f.write(json.dumps(jokes))