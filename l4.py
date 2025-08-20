import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser, ShiftReduceParser

# ✅ Hardcoded Grammar Rules
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

print("Grammar Rules:")
print(grammar)

# ✅ Input sentence
sentence = input("Enter a sentence: ").strip().split()

# ✅ Top-Down Parsing (Recursive Descent Parser)
print("\n--- Recursive Descent Parser (Top-Down) ---")
rd = RecursiveDescentParser(grammar)
found = False
for tree in rd.parse(sentence):
    found = True
    print(tree)
    tree.pretty_print()

if not found:
    print("No valid parse (Top-Down).")

# ✅ Bottom-Up Parsing (Shift Reduce Parser)
print("\n--- Shift Reduce Parser (Bottom-Up) ---")
sr = ShiftReduceParser(grammar)
found = False
for tree in sr.parse(sentence):
    found = True
    print(tree)
    tree.pretty_print()

if not found:
    print("No valid parse (Bottom-Up).")

