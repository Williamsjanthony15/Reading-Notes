# Regular Expression

# See bottom for reference table

## Useful functions provided by the re library, such as: 

compile()
search()
findall()
sub() for search and replace
split()

## Basic Patterns: Ordinary Characters
 
They match themselves exactly and do not have a special meaning in their regular expression syntax.

Examples are 'A', 'a', 'X', '5'.

Ordinary characters can be used to perform simple exact matches:

pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
    print("Match!")
else: print("Not a match!")

Match!


The match() function returns a match object if the text matches the pattern. Otherwise, it returns None. 

'r' at the start of "cookie" on line 19
This is called a raw string literal. It changes how the string literal is interpreted. Such literals are stored as they appear.

\ is just a backslash when prefixed with an r rather than being interpreted as an escape sequence

Sometimes, the syntax involves backslash-escaped characters, and to prevent these characters from being interpreted as escape sequences; you use the raw r prefix.



# Wild Card Characters: Special Characters

## search()

With the search function, you scan through the given string/sequence, looking for the first location where the regular expression produces a match.



## group()

The group function returns the string matched by the re. You will see both these functions in more detail later.


## Special Characters

. - A period. Matches any single character except the newline character.

re.search(r'Co.k.e', 'Cookie').group()
'Cookie'

^ - A caret. Matches the start of the string.


re.search(r'^Eat', "Eat cake!").group()

## However, the code below will not give the same result. Try it for yourself:
# re.search(r'^eat', "Let's eat cake!").group()
'Eat'


$ - Matches the end of string.

re.search(r'cake$', "Cake! Let's eat cake").group()

## The next search will return the NONE value, try it:
# re.search(r'cake$', "Let's get some cake on our way home!").group()

'cake'


[abc] - Matches a or b or c.

[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).


re.search(r'[0-6]', 'Number: 5').group()
'5'
## Matches any character except 5
re.search(r'Number: [^5]', 'Number: 0').group()

## This will not match and hence a NONE value will be returned
#re.search(r'Number: [^5]', 'Number: 5').group()
'Number: 0'

\ - Backslash.


If the character following the backslash is a recognized escape character, then the special meaning of the term is taken (Scenario 1)
Else if the character following the \ is not a recognized escape character, then the \ is treated like any other character and passed through (Scenario 2).

\ can be used in front of all the metacharacters to remove their special meaning (Scenario 3).

## (Scenario 1) This treats '\s' as an escape character, '\s' defines a space
re.search(r'Not a\sregular character', 'Not a regular character').group()
'Not a regular character'

## (Scenario 2) '\' is treated as an ordinary character, because '\r' is not a recognized escape character
re.search(r'Just a \regular character', 'Just a \regular character').group()
'Just a \regular character'

## (Scenario 3) '\s' is escaped using an extra `\` so its interpreted as a literal string '\s'
re.search(r'Just a \\sregular character', 'Just a \sregular character').group()
'Just a \\sregular character'


\w - Lowercase 'w'. Matches any single letter, digit, or underscore.

\W - Uppercase 'W'. Matches any character not part of \w (lowercase w).

print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())

## Matches any character except single letter, digit or underscore

print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())

## Uppercase W won't match single letter, digit

print("Uppercase W won't match, and return:", re.search(r'Co\Wk\We', 'Cookie'))

Lowercase w: Cookie

Uppercase W: C@ke

Uppercase W won't match, and return: None

\s - Lowercase 's'. Matches a single whitespace character like: space, newline, tab, return.

\S - Uppercase 'S'. Matches any character not part of \s (lowercase s).


print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())

print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

Lowercase s: Eat cake

Uppercase S: cookie

\d - Lowercase d. Matches decimal digit 0-9.

\D - Uppercase d. Matches any character that is not a decimal digit.

# Example for \d

print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())
How many cookies do you want?  100




\t - Lowercase t. Matches tab.
\n - Lowercase n. Matches newline.
\r - Lowercase r. Matches return.
\A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
\Z - Uppercase z. Matches only at the end of the string.
TIP: ^ and \A are effectively the same, and so are $ and \Z. Except when dealing with MULTILINE mode. Learn more about it in the flags section.

\b - Lowercase b. Matches only the beginning or end of the word.

# Example for \t
print("\\t (TAB) example: ", re.search(r'Eat\tcake', 'Eat    cake').group())

# Example for \b
print("\\b match gives: ",re.search(r'\b[A-E]ookie', 'Cookie').group())
\t (TAB) example:  Eat    cake
\b match gives:  Cookie



## Repetitions

+ - Checks if the preceding character appears one or more times starting from that position.

re.search(r'Co+kie', 'Cooookie').group()
'Cooookie'
* - Checks if the preceding character appears zero or more times starting from that position.

# Checks for any occurrence of a or o or both in the given sequence
re.search(r'Ca*o*kie', 'Cookie').group()
'Cookie'
? - Checks if the preceding character appears exactly zero or one time starting from that position.

# Checks for exactly zero or one occurrence of a or o or both in the given sequence
re.search(r'Colou?r', 'Color').group()
'Color'
But what if you want to check for an exact number of sequence repetition?

For example, checking the validity of a phone number in an application. re module handles this very gracefully as well using the following regular expressions:

{x} - Repeat exactly x number of times.
{x,} - Repeat at least x times or more.
{x, y} - Repeat at least x times but no more than y times.

re.search(r'\d{9,10}', '0987654321').group()
'0987654321'


# Grouping in Regular Expressions

statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)
Email address: support@datacamp.com
Username: support
Host: datacamp.com

statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)
if statement:
  print("Email address:", match.group('email'))
  print("Username:", match.group('username'))
  print("Host:", match.group('host'))
Email address: support@datacamp.com
Username: support
Host: datacamp.com

### TIP: You can always access the named groups using numbers instead of the name. But as the number of groups increases, it gets harder to handle them using numbers alone. So, always make it a habit to use named groups instead.


## Greedy vs. Non-Greedy Matching

pattern = "cookie"
sequence = "Cake and cookie"

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*>', heading).group()
'<h1>TITLE</h1>

The pattern <.*> matched the whole string, right up to the second occurrence of >.

However, if you only wanted to match the first <h1> tag, you could have used the greedy qualifier *? that matches as little text as possible.

Adding ? after the qualifier makes it perform the match in a non-greedy or minimal fashion; That is, as few characters as possible will be matched. When you run <.*>, you will only get a match with <h1>.

heading  = r'<h1>TITLE</h1>'
re.match(r'<.*?>', heading).group()
'<h1>'

Character(s)	What it does
.	A period. Matches any single character except the newline character.
^	A caret. Matches a pattern at the start of the string.
\A	Uppercase A. Matches only at the start of the string.
$	Dollar sign. Matches the end of the string.
\Z	Uppercase Z. Matches only at the end of the string.
[ ]	Matches the set of characters you specify within it.
\	∙ If the character following the backslash is a recognized escape character, then the special meaning of the term is taken.
∙ Else the backslash () is treated like any other character and passed through.
∙ It can be used in front of all the metacharacters to remove their special meaning.
\w	Lowercase w. Matches any single letter, digit, or underscore.
\W	Uppercase W. Matches any character not part of \w (lowercase w).
\s	Lowercase s. Matches a single whitespace character like: space, newline, tab, return.
\S	Uppercase S. Matches any character not part of \s (lowercase s).
\d	Lowercase d. Matches decimal digit 0-9.
\D	Uppercase D. Matches any character that is not a decimal digit.
\t	Lowercase t. Matches tab.
\n	Lowercase n. Matches newline.
\r	Lowercase r. Matches return.
\b	Lowercase b. Matches only the beginning or end of the word.
+	Checks if the preceding character appears one or more times.
*	Checks if the preceding character appears zero or more times.
?	∙ Checks if the preceding character appears exactly zero or one time.
∙ Specifies a non-greedy version of +, *
{ }	Checks for an explicit number of times.
( )	Creates a group when performing matches.
< >	Creates a named group when performing matches.

