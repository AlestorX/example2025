from models.artist import artist_menu
from models.event import Event


def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1) Artists")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            artist_menu()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Something went wrongTry again or make another choice.")


if __name__ == "__main__":
    main()
