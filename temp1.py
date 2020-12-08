print("Введіть речення: ")
mystr = input()

def unique_count(words):
    p = 0
    count = {}
    for s in mystr:
      if s not in count:
        count[s] = 1
      else:
        count[s] += 1

    for key in count:
      if count[key] == 1:
        p = p+1
    return(p)


print(unique_count(mystr))
