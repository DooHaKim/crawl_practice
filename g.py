from urllib.request import urlopen

text = urlopen('http://doohaproject.tistory.com/attachment/cfile2.uf@25A2F43359777C510E95C5.txt')
string = text.read()
string2 = string.decode('unicode_escape')
print(type(string), string)
print(type(string2), string2)