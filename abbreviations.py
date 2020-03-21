def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0] 
    return result.upper()

print(initials("Universal Serial Bus")) # USB
print(initials("local area network")) # LAN
print(initials("Operating system")) # OS
