#ZIP function take two iterables and combine them and then return them


#EXAMPLE-1

languages = ["Python", "Javascript", "Java", "swift"]

versions = [1, 2, 3, 4]

zipped = zip(languages, versions)
print(list(zipped))

zipped2 = zip(versions, languages)
print(list(zipped2))




