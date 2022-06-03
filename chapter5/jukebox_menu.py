from nested_data import albums

SONG_LIST = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST]
        for index, song in enumerate(song_list):
            print(f"{index + 1}, {song[SONG_TITLE_INDEX]}")
        song_choice = int(input("Pick a song that you like: "))
        if 1 <= song_choice <= len(song_list):
            song_to_play = song_list[song_choice - 1]
            print(f"Playing {song_to_play[SONG_TITLE_INDEX]}")
        print("=" * 40)
    elif choice == -1:
        print("See you later!")
        break
    else:
        print("Ops, invalid choice. Please try again")
