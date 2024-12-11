import heapq
import pandas as pd


def generate_huffman_table_step_by_step(probabilities):
    # Initialize min-heap with symbols and probabilities
    heap = [[weight, symbol] for symbol, weight in probabilities.items()]
    heapq.heapify(heap)

    steps = [sorted([[prob, symbol] for prob, symbol in heap], key=lambda x: x[0], reverse=True)]

    while len(heap) > 1:
        # Sort heap to get the step in order
        heap.sort(key=lambda x: x[0])

        # Take two smallest probabilities
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)

        # Merge the two symbols
        merged_symbol = f"({low1[1]}+{low2[1]})"
        merged_probability = low1[0] + low2[0]

        # Append the merged result to the heap
        heapq.heappush(heap, [merged_probability, merged_symbol])

        # Capture the current step in a list (descending order)
        step_snapshot = sorted([[prob, symbol] for prob, symbol in heap], key=lambda x: x[0], reverse=True)
        steps.append(step_snapshot)

    steps_transposed = []
    for step in steps:
        steps_transposed.append([f"{p[0]:.2f}" for p in step] +
                                [""] * (len(probabilities) - len(step)))

    columns = [f"{i}" for i in range(len(steps))]
    huffman_table_df = pd.DataFrame(list(map(list, zip(*steps_transposed))), columns=columns)

    return huffman_table_df


symbols_probabilities = {
    "m1": 0.20,
    "m2": 0.19,
    "m3": 0.16,
    "m4": 0.14,
    "m5": 0.11,
    "m6": 0.10,
    "m7": 0.08,
    "m8": 0.02
}

huffman_table_step_by_step = generate_huffman_table_step_by_step(symbols_probabilities)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

print(huffman_table_step_by_step)
