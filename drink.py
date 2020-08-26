details = {
"ZC": 3.8,
"TY": 0,
"NY": 5.5+9.8,
"LY": 0,
"FT": 4.5,
"JT": 3.8,
"YW": 3.37,
}

paid = 26.37
total = sum([details[person] for person in details])

print("total : %.02f" % total)
print("paid  : %.02f" % paid)

for person, share in details.items():
    print("%-8s: %.02f [%.02f]" % (person, share / total * paid, share))
