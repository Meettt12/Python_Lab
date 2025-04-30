name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

vcard = "BEGIN:VCARD\n"
vcard += "VERSION:3.0\n"
vcard += "FN:" + name + "\n"
vcard += "TEL;TYPE=CELL:" + phone + "\n"
vcard += "EMAIL:" + email + "\n"
vcard += "END:VCARD"

f = open("contact.vcf", "w")
f.write(vcard)
f.close()

print("Contact saved to contact.vcf!")
