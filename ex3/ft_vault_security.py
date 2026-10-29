def secure_archive(
        path: str,
        mode: str = "r",
        content: str = ""
) -> tuple[bool, str]:
    if not path:
        return (False, "No file path provided")
    if mode not in ("r", "w"):
        return (False, "Invalid mode.")
    try:
        with open(path, mode) as archive:
            if mode == "w":
                archive.write(content)
            elif mode == "r":
                content = archive.read()
        if mode == "w":
            return (True, "Content successfully written to file")
        return (True, content)
    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("nonexistent_file.txt"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, content = secure_archive("regular_file.txt")
    print((success, content))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_file.txt", "w", content))
