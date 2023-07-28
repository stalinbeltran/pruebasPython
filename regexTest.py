import re

sentence = "This [is] (some (nested) text) que qir between (external) parentheses."

# Extract text between the most external parentheses
# pattern = r'(?<!\(.*)\((?!.*\))(.+?)(?<!\().*?\)(?!\))'
pattern = r'q(?!u).*'
matches = re.findall(pattern, sentence)

print(matches)


[('[is (some (nested) text) between (external) ]', 'is (some (nested) text) between (external) ')]