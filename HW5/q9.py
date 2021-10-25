def palindrome(word):
    # keep going until there's only one letter left
    if len(word) <= 1:
        return True
    else:
        # check to see if first and last letters match
        if word[0] != word[-1]:
            return False
        else:
            # if first and last match, run the iteration again but by looking at 2nd and 2nd to last letter
            return palindrome(word[1:-1])

palindrome("kayak")

palindrome("hello")
