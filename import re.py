import re

with open("filename.txt", "r") as file:
    contents = file.read()

pattern = r'title="([\w\s\/]+)"'
results = re.findall(pattern, contents)

for result in results:
    print(result)
