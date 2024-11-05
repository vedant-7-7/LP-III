import heapq

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(chars, freq):
    nodes = [Node(symbol, freq) for symbol, freq in zip(chars, freq)]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        combined_node = Node(left.symbol + right.symbol, left.freq + right.freq)
        combined_node.left = left
        combined_node.right = right
        heapq.heappush(nodes, combined_node)

    return nodes[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    if node:
        if not node.left and not node.right:  # Leaf node
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)
    return huffman_codes

if __name__ == "__main__":
    chars = input("Enter characters (separated by a space): ").split()
    freq = [int(f) for f in input("Enter corresponding frequencies (separated by a space): ").split()]

    root = build_huffman_tree(chars, freq)
    huffman_codes = generate_huffman_codes(root)

    print("Huffman Codes:")
    for symbol, code in huffman_codes.items():
        print(f"{symbol} -> {code}")
