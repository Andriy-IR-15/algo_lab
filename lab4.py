import collections


def find_minimum_depth(graph, root):

    if not graph:
        return 0

    queue = collections.deque([(root, 0)])

    while queue:

        node, depth = queue.popleft()

        if not graph[node]:
            return depth

        for child in graph[node]:

            if child is not None:
                queue.append((child, depth + 1))

    return depth


def main():

    with open("input.txt", "r") as f:

        data = f.readlines()

        root = int(data[0])

        edges = [
            tuple(int(x) if x != "None" else None for x in line.strip().split(","))
            for line in data[1:]
        ]

        graph = collections.defaultdict(list)

        for u, v in edges:

            graph[u].append(v)

        depth = find_minimum_depth(graph, root)

        with open("output.txt", "w") as f:
            f.write(str(depth))


if __name__ == "__main__":
    main()
