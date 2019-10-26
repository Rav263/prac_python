import re

string = input()
pattern = "(?:" + input().replace("@", "){1}(?:\w|\s){1}(?:") + "){1}"

pattern = pattern.replace("(?:){1}", "")
pattern = re.compile(pattern)
searched = pattern.search(string)
print(-1 if searched == None else searched.start())
