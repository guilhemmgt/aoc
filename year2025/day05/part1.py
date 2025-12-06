def main():
    with open('input') as f:
        input = [line.strip() for line in f]
    input_ranges = input[: input.index("")]
    input_ids = input[input.index("") + 1:]

    ranges = [[int(n) for n in r.split("-")] for r in input_ranges]
    ids = [int(id) for id in input_ids]

    freshs = 0
    for id in ids:
        for range in ranges:
            if range[0] <= id and id <= range[1]:
                freshs += 1
                break

    print(freshs)


if __name__ == '__main__':
    main()
