note = input("Write a note: ")
with open("my_notes.txt", "a") as file:
    file.write(note + "\n")
with open("my_notes.txt", "r") as file:
    saved = file.read()
print("--- SAVED NOTES ---")
print(saved)
