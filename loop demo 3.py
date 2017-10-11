phrase1 = "What's up with that?"

count_t = 0

for each in phrase1:
    print(each)
    if each == "t":
        count_t += 1

print("found", count_t, "t's\n")

phrase2 = "We found a way to bale the hay."

words = phrase2.split()

count_articles = 0
for each in words:
    print(each)
    if each == "a" or each == "the" or each == "an":
        count_articles += 1

print("found", count_articles, "articles")
