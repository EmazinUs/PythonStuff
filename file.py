# f = open("tfile.txt", "a")
# f.write("all good")
# f.close()
# f = open("tfile.txt", "r")
# print(f.read())
# with open("textFile.txt", "r") as h:
#     print(h.read())

# h = open("textFile.txt", "r")
# print(h.read())
# Write and read tfile.txt
try:
    with open("tfile.txt", "w") as f:  # Use "w" to overwrite instead of appending
        f.write("all good")
    with open("tfile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("tfile.txt not found.")

# Attempt to read textFile.txt
try:
    with open("textFile.txt", "r") as h:
        print(h.read())
except FileNotFoundError:
    print("textFile.txt not found.")
