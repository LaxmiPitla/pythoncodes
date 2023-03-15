import re
string="'I AM NOT YELLING',she said####.. Though we knew it not to be true/"
print(string)
new=re.sub('[A-Z]','',string) #sub means substitute
print(new)
new=re.sub('[a-z]','',string)
print(new)
new=re.sub('[.\',]','',string)
print(new)
new=re.sub('[A-Z]','#',string)
print(new)
new=re.sub('[#]','@',string)
print(new)
new=re.sub('[.\',A-Z+" "]','a',string)
print(new)
new=re.sub('[.\',a-z]','',string)
print(new)
string=string+"6789-<4567"
print(string)
new=re.sub('[^0-9]',' ',string) # replacing everything but not numbers
print(new)
