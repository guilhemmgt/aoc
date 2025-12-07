def safe_dict_increment(dict, key, incr):
    if key in dict:
        dict[key] += incr
    else:
        dict[key] = incr


def main():
    with open('input') as f:
        input = [line.strip() for line in f][::2] # we dont need the empty lines

    beams = {input[0].index('S'): 1} # for each beam, tracks in how many timelines it exists
    for line in input[1:]:
        new_beams = dict()
        for beam in beams:
            match line[beam]:
                case '.':  # beam goes straight
                    safe_dict_increment(new_beams, beam, beams[beam])
                case '^':  # beam splits
                    safe_dict_increment(new_beams, beam - 1, beams[beam])
                    safe_dict_increment(new_beams, beam + 1, beams[beam])
                case _:
                    raise Exception(f"Unknown symbol {line[beam]}.")
        beams = new_beams

    print(sum(beams[x] for x in beams))


if __name__ == '__main__':
    main()
