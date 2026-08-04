"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized, and remaining letters lowercased.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

def generate_hashtag(s):
    captalize_string = s.title()
    remove_spaces = captalize_string.replace(" ", "")

    if not len(remove_spaces) >= 140 and remove_spaces:
        return f"#{remove_spaces}"
    else:
        return False
