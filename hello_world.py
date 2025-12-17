import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="World")
    parser.add_argument("--times", type=int, default=1)
    args = parser.parse_args()

    name = (args.name or "").strip()
    if not name:
        name = "World"

    times = args.times
    if times < 1:
        times = 1

    for _ in range(times):
        print(f"Hello, {name}!")

if __name__ == "__main__":
    main()