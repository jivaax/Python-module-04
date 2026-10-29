import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        opened_file: typing.IO[str] | None = None
        try:
            opened_file = open(sys.argv[1], "r")
            print("---\n")
            reading = opened_file.read()
            print(reading, end="")
            print("\n\n---")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if opened_file is not None:
                opened_file.close()
                print(f"File '{sys.argv[1]}' closed.")
