# Regular Expressions

Notes on regular expressions in Python using the [re](https://docs.python.org/3/library/re.html#module-re) module.

## Overview

A regular expression (RE, regex pattern, or regex) is a tiny, highly specialized programming language embedded inside Python. 

Essentially, it is a pattern language for searching and matching text.

You can access it through the [re](https://docs.python.org/3/library/re.html#module-re) module.

You can use regex to set rules for find a set of possible strings. You can also use regex to modify a string or even split it in different ways. You can search if a set of words contain:

- TeX commands
- Email addresses
- English sentences

!!!note

        The regex pattern language is small and restricted hence you can't perform all string processing tasks with it.

## Regex in Action

Now let's take a Python function and use it to search for specific set of characters using regex. We want to extract the first word in a string. The string can start with Meta characters like periods or commas. So we need to ignore these characters and print out the first word alone. However, the word can contain an apostrophe within it.

```python

# importing the re module
import re

# A function to extract words based on set rules
def input_text(text: str) -> str:

    # Setting regex rule to find any sequence of letters (a-z, A-Z) and apostrophes (')
    find_match = re.search(r"[a-zA-Z']+", text)

    if find_match:
        return find_match.group(0)
    return ""


# Let's call the function
input_text("...Let's visit... the new museum")

# Result
"Let's"



```


Here are some common regex symbols and their meaning including example results based on the code above:

| Symbol | Meaning                                | Example                  |
| ------ | -------------------------------------- | ------------------------ |
| `.`    | Match any character except new line    | `.` = all characters minus new line   |
| `[]`   | Match any one character inside         | `[abc]` = 'a', 'b', 'c'  |
| `-`    | Range inside `[]`                      | `[a-z]` = 'a' to 'z'     |
| `+`    | One or more of previous                | `[0-9]+` = "12", "4567"  |
| `*`    | Zero or more of previous               | `[a-z]*` = "", "abc"     |
| `\d`   | Any digit (0-9)                        | `\d+` = "2024"           |
| `\w`   | Any word character (a-z, A-Z, 0-9, \_) | `\w+` = "Hello123"       |
| `.`    | Any character except newline           | `a.b` = "acb", "a9b"     |
| `^`    | Start of string                        | `^Hello` matches "Hello" |
| `$`    | End of string                          | `world$` matches "world" |
