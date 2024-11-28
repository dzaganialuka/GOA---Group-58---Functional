def reverse(text):
 rev = ""
 for i in text.split(" "):
    rev = i + rev
 return rev
rev = "goa is the best accademy"
print(reverse(rev))