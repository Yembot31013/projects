l = ["[shift]", "[ctrl]", "[enter]"]
w = " h [ctrl] \x03 [ctrl] hhhhjhuhuuh    uuuu [enter]  [ctrl]"

def backspace(ignore, word):
  w = word.split(" ")
  v = ""
  ind = 0
  for index, i in enumerate(w):
    if i not in ignore and i:
      v = i
      ind = index
      print("v: ", v)
      print("ind: ", ind)

  v = v[:-1]
  w.pop(ind)
  w.insert(ind, v)
  w = " ".join(w)
  return w

print(backspace(l, w))
