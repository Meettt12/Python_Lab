#Convert bytes into KB, MB, and GB.
bytes = float(input("Enter bytes: "))
kb = bytes / 1024
mb = kb / 1024
gb = mb / 1024
print("KB:", kb, "MB:", mb, "GB:", gb)
