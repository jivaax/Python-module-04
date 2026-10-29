import sys
import typing


if __name__ == "__main__":
    reading_successful = False
    write_successful = False
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        opened_file: typing.IO[str] | None = None
        try:
            opened_file = open(sys.argv[1], "r")
            print("---\n")
            reading = opened_file.read()
            reading_successful = True
            print(reading, end="")
            print("\n\n---")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if opened_file is not None:
                opened_file.close()
                print(f"File '{sys.argv[1]}' closed.")
    if reading_successful:
        print("\nTransform data:")
        print("---\n")
        transformed_data = reading.replace("\n", "#\n")
        if reading and not reading.endswith("\n"):
            transformed_data += "#"
        print(transformed_data, end="")
        print("\n\n---")
        print("Enter new file name (or empty): ")
        new_file_name = input()
        if new_file_name:
            new_file: typing.IO[str] | None = None
            try:
                print(f"Saving data to '{new_file_name}'")
                new_file = open(new_file_name, "w")
                new_file.write(transformed_data)
                write_successful = True
            except OSError as e:
                print(f"Error saving data to file '{new_file_name}': {e}")
            finally:
                if new_file is not None:
                    new_file.close()
                    if write_successful:
                        print(f"Data saved in file '{new_file_name}'.")
        else:
            print("Not saving data.")
