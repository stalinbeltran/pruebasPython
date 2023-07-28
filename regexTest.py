import re

sentence = "This [is] (some (nested text) que eir between quien (external parew)ntheses"

# Extract text between the most external parentheses
# pattern = r'(?<!\(.*)\((?!.*\))(.+?)(?<!\().*?\)(?!\))'
pattern = r"\((.)+\)"
matches = re.findall(pattern, sentence, re.DOTALL)

print(matches)


[('[is (some (nested) text) between (external) ]', 'is (some (nested) text) between (external) ')]