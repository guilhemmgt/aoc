import re

PAIRS_TO_CONNECT = 10


def main():
    with open('input') as f:
        input = [line.strip() for line in f]

    boxes = [[int(x) for x in re.findall(r'\d+', l)] for l in input] # boxes coordinates

    pairs = []
    # calculate distances between each pair of boxes
    for i in range(0, len(boxes)):
        box_i = boxes[i]
        for j in range(i + 1, len(boxes)):
            box_j = boxes[j]
            dist = sum((box_i[n] - box_j[n])**2 for n in range(0, 3))
            pairs.append([i, j, dist]) # (box1, box2, distance_between_the_two)[]
    pairs.sort(key=lambda x: x[2])  # sort by distance
    pairs = [(i, j) for i, j, _ in pairs] # we dont really need the distances, we just need to have the pairs sorted

    # each box starts in its own individual circuit
    circuits = {i: [i] for i in range(0, len(boxes))} # circuit id -> list of box (circuit) ; all circuits are disjoints
    boxes_circuits = {i: i for i in range(0, len(boxes))}  # box -> its circuit id

    # connections !!!
    connected = 0
    while (len(circuits) != 1):
        (box_i, box_j) = pairs[connected]
        connected += 1

        box_i_circuit_id = boxes_circuits[box_i]
        box_j_circuit_id = boxes_circuits[box_j]

        # if theyr already are in the same circuit, nothing more happens...
        if (box_i_circuit_id == box_j_circuit_id):
            continue

        # the circuit of box j is merged into the circuit of box i
        for box in circuits[box_j_circuit_id]:
            boxes_circuits[box] = box_i_circuit_id
            circuits[box_i_circuit_id].append(box)
        circuits.pop(box_j_circuit_id)

    res = boxes[pairs[connected - 1][0]][0] * boxes[pairs[connected - 1][1]][0]
    print(res)

if __name__ == '__main__':
    main()
