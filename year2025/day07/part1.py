def main():
    with open('input') as f:
        input = [line.strip() for line in f][::2] # we dont need the empty lines

    times_split = 0
    beams = set([input[0].index('S')]) # tracks the beams positions
    for line in input[1:]:
        new_beams = set()
        for beam in beams:
            match line[beam]:
                case '.': # beam goes straight
                    new_beams.add(beam)
                case '^': # beam splits
                    new_beams.add(beam - 1)
                    new_beams.add(beam + 1)
                    times_split += 1
                case _:
                    raise Exception(f"Unknown symbol {line[beam]}.")
        beams = new_beams

    print(times_split)


if __name__ == '__main__':
    main()
