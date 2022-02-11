import json

data = input()
classes = {}
json_data = json.loads(data)
for item in json_data:
    if item['name'] not in classes.keys():
        classes[item['name']] = 0

    for elem in item['parents']:
        if elem in classes.keys():
            classes[elem] += 1
        else:
            classes[elem] = 1

# print(classes)
classes_list = []
for key in classes.keys():
    classes_list.append(key + " : " + str(classes[key] + 1))
classes_list.sort()

for i in classes_list:
    print(i)
