import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="World")
    args = parser.parse_args()

    name = (args.name or "").strip()
    if not name:
        name = "World"

    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()