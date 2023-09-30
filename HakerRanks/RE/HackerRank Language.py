# Enter your code here. Read input from STDIN. Print output to STDOUT

# Method 1 without regex
n = int(input())
List = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(":")
for _ in range(n):
    num,Lan = input().split()
    if Lan in List:
        print("VALID")
    else:
        print("INVALID")

# Method 2 with regex
import re
n = int(input())
S = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"
for _ in range(n):
    num,Lan = input().split()
    if re.search(rf"\b{Lan}\b",S):
        print("VALID")
    else:
        print("INVALID")

template = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"

template = template.split(":")
print(template)

import re

pt1 = re.compile(r'\b[\w]*$')

for __ in range(int(input())):

    data = input()


    mch = pt1.search(data)
    if pt1:

        fragment = mch.group()

        if fragment in template:
            print("VALID")

        else:
            print("INVALID")
