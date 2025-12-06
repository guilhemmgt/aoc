def incl_range_from(a):
    """
    Builds a range from a two-elements array. The range is positive and inclusive.
    """
    return range(min(int(a[0]), int(a[1])), max(int(a[0]), int(a[1])) + 1)


def union(a, b):
    """
    Returns the range representing the union of two intersecting ranges.
    """
    if intersects(a, b):
        return range(min(a[0], b[0]), max(a[-1], b[-1]) + 1)
    else:
        raise Exception("intervals are disjoints")


def contains(a, b):
    """
    Returns `True` is range a contains range b; `False` otherwise.
    """
    return a[0] <= b[0] and b[-1] <= a[-1]


def intersects(a, b):
    return a[0] in b or a[-1] in b or b[0] in a or b[-1] in a


def add_to_set(set, range_to_add):
    """
    Add a range to a set.
    Assumes the ranges inside the input set are pairwise disjoints, and ordered.
    Returns a set with such properties.
    """

    for i in range(0, len(set)):
        # 'range_to_add' is already included in 'set'
        if contains(set[i], range_to_add):
            return set

        # 'range_to_add' is inbetween two ranges of 'set'
        if range_to_add[-1] < set[i][0]:
            return set[:i] + [range_to_add] + set[i:]

        # 'range_to_add' intersects 1+ range(s) of 'set'
        # 'range_to_add' and the range(s) it intersects must be merged into 1 range
        if intersects(range_to_add, set[i]):
            new_range = union(range_to_add, set[i])
            j = i + 1
            while j < len(set) and intersects(range_to_add, set[j]):
                new_range = union(new_range, set[j])
                j += 1
            return set[:i] + [new_range] + set[j:]

    # elements of 'set' < elements of 'range'
    return set + [range_to_add]


def main():
    with open('input') as f:
        input = [line.strip() for line in f]
    input_ranges = input[: input.index("")]

    ranges = [incl_range_from(r.split("-")) for r in input_ranges]

    # represents the ID ranges as a set of pairwise disjoints ranges
    set = []
    for r in ranges:
        set = add_to_set(set, r)

    # len of all ranges in the set = nb of fresh ingredients
    freshs = sum(len(r) for r in set)

    print(freshs)


if __name__ == '__main__':
    main()
