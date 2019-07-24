"""
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings,
using a specialized syntax held in a pattern



                                            1.The match Function

This function attempts to match RE pattern to string with optional flags.
re.match(pattern, string, flags=0)


pattern:
This is the regular expression to be matched.

string:
This is the string, which would be searched to match the pattern at the beginning of string.

flags:
You can specify different flags using bitwise OR (|). These are modifiers.


The re.match function returns a match object on success, None on failure.
We usegroup(num) or groups() function of match object to get matched expression.


group(num=0):

This method returns entire match (or specific subgroup num).


groups():

This method returns all matching subgroups in a tuple (empty if there weren't any).



                                    2.The search Function

This function searches for first occurrence of RE pattern within string with optional flags.
Here is the syntax for this function −
re.search(pattern, string, flags=0)

same as above.



Matching Versus Searching
Python offers two different primitive operations based on regular expressions:
match checks for a match only at the beginning of the string, while
search checks for a match anywhere in the string (this is what Perl does by default).


Search and Replace
One of the most important re methods that use regular expressions is sub.

Syntax
re.sub(pattern, repl, string, max=0)

This method replaces all occurrences of the RE pattern in string with repl,
substituting all occurrences unless max provided. This method returns modified string.

"""


# example for match fucntion this is same as for search function also:
"""
import re

line="Cats are smarter than dogs"

matchObj=re.match(r'(.*)are (.*?) .*',line,re.M|re.I)

if matchObj:
    print("matchObj.group(): ",matchObj.group(0))
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
else:
    print("No Match")
    
"""

# example for match vs search function

import re


line="Cats are Smaller than Dogs and sounds like mow mow mow"

matchObj=re.match(r'Cats',line,re.M|re.I)

if matchObj:
    print("match-->matchObj.group()",matchObj.group())
else:
    print("No Match!")


line="Cats are Smaller than Dogs and sounds like mow mow mow"

searchObj=re.search(r'dogs',line,re.M|re.I)

if matchObj:
    print("match-->matchObj.group()",searchObj.group())
else:
    print("No Match!")


# example for Search and replace

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)





# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)


# Regular Expression Patterns

# Except for control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match themselves.
# You can escape a control character by preceding it with a backslash.


"""
^           Matches beginning of line.

$           Matches end of line.

.           Matches any single character except newline. Using m option allows it to match newline as well.

[...]       Matches any single character in brackets

[^...]      Matches any single character not in brackets

re*         Matches 0 or more occurrences of preceding expression.

re+         Matches 1 or more occurrence of preceding expression.

re?         Matches 0 or 1 occurrence of preceding expression.

re{ n}      Matches exactly n number of occurrences of preceding expression.

re{n, }     Matches n or more occurrences of preceding expression.

re{ n, m}   Matches at least n and at most m occurrences of preceding expression


a| b        Matches either a or b.

(re)        Groups regularexpressions and remembers matched text.


(?imx)     Temporarily toggles on i, m, or x options within a regular expression.
            If in parentheses, only that area is affected.


(?-imx)     Temporarily toggles off i, m, or x options within a regular expression.
            If in parentheses, only that area is affected.

(?: re)     Groups regular expressions without remembering matched text.

(?imx: re)  Temporarily toggles on i, m, or x options within parentheses.

(?-imx: re) Temporarily togglesoff i, m, or x options within parentheses.

(?#...)     Comment.

(?= re)     Specifies position using a pattern. Doesn't have a range.

(?! re)     Specifies position using pattern negation.Doesn't have a range

(?> re)     Matches independent pattern without back tracking.

\w          Matches word characters.

\W          Matches nonword characters.

\s          Matches whitespace. Equivalent to [\t\n\r\f].

\S          Matches nonwhitespace.


\d          Matches digits. Equivalentto[0 - 9].

\D          Matches nondigits.

\A          Matches beginning of string.

\Z          Matches end of string. If a newline exists, it matches just before newline.

\z          Matches end of string.

\G          Matches point where last match finished.

\b          Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.

\B          Matches nonword boundaries.


\n, \t, etc. Matches newlines, carriage returns, tabs, etc.

\1...\9     Matches nth grouped subexpression.

\10         Matches nth grouped sub expression if it matched already.
            Otherwise refers to the octal representation of a character code.


                                Regular Expressions  Character classes:

[Pp]ython   Match "Python" or "python"

rub[ye]     Match "ruby" or "rube"

[aeiou]     Match any one lowercase vowel

[0-9]       Match any digit; same as [0123456789]

[a-z]       Match any lowercase ASCII letter

[A - Z]     Match any uppercase ASCII letter

[a-zA-Z0-9] Match any of the above

[^aeiou]    Match anything other than a lowercase vowel


[^0-9]      Match anything other than a digit




                                Special Character Classes


.           Match any character except newline

\d          Match a digit: [0-9]


\D          Match a nondigit: [ ^ 0 - 9]

\s          Match a whitespace character: [ \t\r\n\f]

\S          Match nonwhitespace: [^ \t\r\n\f]

\w          Match a single word character: [A-Za-z0-9_]

\W          Match a nonword character: [^A-Za-z0-9_]


                                Repetition Cases:

ruby?       Match "rub" or "ruby": the y is optional

ruby*       Match "rub" plus 0 or more ys


ruby+       Match "rub" plus 1 or more ys


\d          {3} Match exactly 3 digits

\d{3,}      Match 3 or more digits


\d          {3, 5} Match 3, 4, or 5 digits

                                Nongreedy repetition:

<.*>        Greedy repetition: matches "<python>perl>"

<.*?>       Nongreedy: matches "<python>" in "<python>perl>"

                                Grouping with Parentheses:

\D\d +              No group: + repeats \d

(\D\d)+             Grouped: + repeats \D\d pair


([Pp]ython(, )?)+   Match "Python", "Python, python, python", etc.


                                Backreferences:

([Pp])ython&\1ails      Match python&pails or Python&Pails

(['"])[^\1]*\1          Single or double-quoted string. \1 matches whatever the 1st group matched. '
                        '\2 matches whatever the 2nd group matched, etc


                                Alternatives:

python|perl             Match "python" or "perl"

rub(y|le))              Match "ruby" or "ruble"

Python(!+|\?)           "Python" followed by one or more ! or one ?


                                Anchors:

^Python             Match "Python" at the start of a string or internal line

Python$             Match "Python" at the end of a string or line


\APython            Match "Python" at the start of a string

Python\Z            Match "Python" at the end of a string

\brub\B             \B is nonword boundary: match "rub" in "rube" and "ruby" but not alone

Python(?=!)         Match   "Python", if followed by an exclamation point.

Python(?!!)         Match "Python", if not followed by an exclamation point.


                            Special Syntax with Parentheses:


R(?  # comment)     Matches "R".All the rest is a comment

R(?i)uby            Case-insensitive while matching "uby"

R(?i: uby)          Same as above

rub(?:y|le))        Group only without creating \1 backreference


"""






