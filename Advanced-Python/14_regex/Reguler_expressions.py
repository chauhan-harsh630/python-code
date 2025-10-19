import re

text  = "My number is 9368745615"

match = re.search("number",text)
m = re.findall("\d{10}", text)
r = re.sub("\d{7}", "XXXXXXX", text)


if match:
    print("Found!")
else:
    print("Not Found!")

if m:
    print("Found using findall:", m)
else:
    print("Not Found using findall")

if r:
    print("After substitution:", r)
else:
    print("Substitution failed")



    #A few useful patterns

# | Pattern | Meaning                          | Example Match              |
# | ------- | -------------------------------- | -------------------------- |
# | `\d`    | Any digit                        | `5` in `"Room 5"`          |
# | `\w`    | Any letter, number or underscore | `A` in `"A1_"`             |
# | `\s`    | Any whitespace (space, tab)      | space in `"Hello World"`   |
# | `.`     | Any character except newline     | `e` in `"Hello"`           |
# | `+`     | One or more                      | `123` in `"123"`           |
# | `*`     | Zero or more                     | `""` or `"abc"`            |
# | `^`     | Start of string                  | `"Hello"` starts with `^H` |
# | `$`     | End of string                    | `"world"` ends with `d$`   |
# | `{n}`   | Exactly n occurrences            | `\d{3}` matches `123`      