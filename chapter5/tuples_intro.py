# t = ("a", "b", "c")
# print(t)

linkin_park = ("Hybrid Theory", "Linkin Park", 2000)
ac_dc = ("Back in Black", "AC/DC", 1980)
gun_n_roses = ("Appetite for Destruction", "Gun 'n Roses", 1987)
green_day = ("American Idiot", "Green Day", 2004)
band_maid = ("Unseen World", "Band Maid", 2021)

# Unpack tuple
# print(linkin_park)
# print(linkin_park[0])
# print(linkin_park[1])
# print(linkin_park[2])

# Better way to unpack tuple
# title, artist, year = linkin_park
# print(title)
# print(artist)
# print(year)

albums = [
    ("Hybrid Theory", "Linkin Park", 2000),
    ("Back in Black", "AC/DC", 1980),
    ("Appetite for Destruction", "Gun 'n Roses", 1987),
    ("American Idiot", "Green Day", 2004),
    ("Unseen World", "Band Maid", 2021)
]

for album in albums:
    title, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(title, artist, year))


# for title, artist, year in albums:
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(title, artist, year))