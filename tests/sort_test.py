from bot.utils.sort import sort_files
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        known_extensions, unknown_extensions = sort_files(folder_path)

        print("Known extensions:")
        for ext in known_extensions:
            print(ext)

        print("\nUnknown extensions:")
        for ext in unknown_extensions:
            print(ext)
