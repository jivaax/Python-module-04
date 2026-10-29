import sys
import typing


if __name__ == "__main__":
    reading_successful = False
    write_successful = False
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
            print("[STDERR] Error opening file "
                  f"'{sys.argv[1]}': {e}", file=sys.stderr)
        finally:
            if opened_file is not None:
                try:
                    opened_file.close()
                    print(f"File '{sys.argv[1]}' closed.")
                except OSError as e:
                    reading_successful = False
                    print("[STDERR] Error closing file "
                          f"'{sys.argv[1]}': {e}", file=sys.stderr)
    if reading_successful:
        print("\nTransform data:")
        print("---\n")
        transformed_data = reading.replace("\n", "#\n")
        if reading and not reading.endswith("\n"):
            transformed_data += "#"
        print(transformed_data, end="")
        print("\n\n---")
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_file_name = sys.stdin.readline().rstrip("\n")
        if new_file_name:
            new_file: typing.IO[str] | None = None
            try:
                print(f"Saving data to '{new_file_name}'")
                new_file = open(new_file_name, "w")
            except OSError as e:
                print("[STDERR] Error opening file "
                      f"'{new_file_name}': {e}", file=sys.stderr)

            if new_file is not None:
                try:
                    new_file.write(transformed_data)
                    write_successful = True
                except OSError as e:
                    print("[STDERR] Error writing to file "
                          f"'{new_file_name}': {e}", file=sys.stderr)
                finally:
                    try:
                        new_file.close()
                    except OSError as e:
                        write_successful = False
                        print("[STDERR] Error closing file "
                              f"'{new_file_name}': {e}", file=sys.stderr)

            if write_successful:
                print(f"Data saved in file '{new_file_name}'.")
            else:
                print("Data not saved.")
        else:
            print("Not saving data.")
