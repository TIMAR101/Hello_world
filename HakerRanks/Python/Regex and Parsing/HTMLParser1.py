# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys
N = int(input())
S = sys.stdin.read()
S = re.sub(r"<!--[\S\s]+?-->","",S)
tags = re.findall(r"<[^/][\S\s]*?>",S)
for tag in tags:
    attrs = re.findall(r'([\w-]+)="(.+?)"',tag)
    print(*re.findall("(?<=<)\w+",tag))
    for attr in attrs :
        print(f"-> {attr[0]} > {attr[1]}")

import re

html = ''
for _ in range(int(input())):
    html += input()

html = re.sub(r'<!--.*?-->', '', html)
tags = re.findall('<([^/].*?)>', html)
for tag in tags:
    print(re.match('[^ ]+', tag).group())
    attrs = re.findall('([^ ]+)="(.+?)"', tag)
    for attr in attrs:
        print(f'-> {attr[0]} > {attr[1]}')

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("{:5} : {}".format("Start",tag))

        #for item in attrs:

            #print(f"-> {item[0]} > {item[1]}")

        for name,value in attrs:
                print(f"-> {name} > {value}")




    def handle_endtag(self, tag):
        print("{:5} : {}".format("End",tag))
    def handle_startendtag(self, tag, attrs):
        print("{:5} : {}".format("Empty",tag))
        for name,value in attrs:
            print(f"-> {name} > {value}")

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for ___ in range(int(input())):

    parser.feed(input())







