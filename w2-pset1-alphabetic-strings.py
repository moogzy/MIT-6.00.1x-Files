"""

Find longest alphabetical order substring in a given string.

Author: Adrian Arumugam (apa@moogzy.net)
Date: 2018-01-27

MIT 6.00.1x

"""

s = 'azcbobobegghakl'
currloc = 0
substr = ''
sublist = []
strend = len(s)

# Process the string while the current slice location is less then the length of the string.
while currloc < strend:
  # Append the character from the current location to the substring.
  substr += s[currloc]
  
  # Our base case to ensure we don't try to access invalid string slice locations.
  # If current location is equal to the actual length of the string then increment
  # the current location counter and append the substring to our list.
  if currloc == strend - 1:
    currloc += 1
    sublist.append(substr)
  # Continute processing the substring as we've still got slices in alphabetical order.
  elif s[currloc+1] >= s[currloc]:
    currloc += 1
  # Current slice location broken the alphabetical order requirement.
  # Append the current substring to our list, reset to an empty substring and increment the current location.
  else:
    sublist.append(substr)
    substr = ''
    currloc += 1

print("Longest substring in alphabetical order is: {}".format(max(sublist, key=len)))
