name = "Divyam"
greeting = f"Good Morning, {{name}}" # {{ and }} are used to escape curly braces
print(greeting)
greeting = f"Good Morning, {name}"
print(greeting)

# old way
letter = "Hello, my name is {}, and I am {} years old."
print(letter.format("Divyam", 20))

price = 49.0999999
txt = f"for only {price:.2f} dollars!"
print(txt)