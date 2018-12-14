import json
jokes = open('jokes.txt', 'r').read().split("\n--\n")
print(jokes)
f = open('jokes.json', 'w')
f.write(json.dumps(jokes))