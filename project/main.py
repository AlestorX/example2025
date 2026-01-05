from models.artist import artist_menu


def main():
    artists = artist_menu()
    print("\nArtists received in main.py")
    for a in artists:
        a.show()

if __name__ == "__main__":
    main()