from functools import cache
class State:
    def __init__(self):
        self.transitions = {}  # A dictionary to store transitions to other states
        self.is_final = False  # Indicates if this state is the end of a recognized word
        self.value = None  # The value of the state (if it is a final state)

    def __repr__(self):
        return f"State({self.transitions}, {self.is_final})"

class DAFSA:
    def __init__(self):
        self.start = State()  # The starting state of the DAFSA
    
    def __repr__(self):
        return f"DAFSA({self.start})"


def add_word(dafsa, word):
    current = dafsa.start
    for char in word:
        if char not in current.transitions:
            current.transitions[char] = State()
        current = current.transitions[char]
        current.value = char
    current.is_final = True

# visit each node in the graph and count the number of nodes visited. visited is a list of characters that have been visited
def node_count(node,visited=[]):
    print(f"\n\nVisiting node {node}. Visited: {visited}")
    count = 1  # Count the current node
    for next_node in node.transitions.values():
        if next_node.value not in visited:
            visited.append(next_node.value)
            count += node_count(next_node,visited)
    return count

if __name__ == "__main__":
    dafsa = DAFSA()

    n = int(input())
    for _ in range(n):
        add_word(dafsa, input())

    print(f"{dafsa}")

    # Count nodes in the DAFSA
    node_count_result = node_count(dafsa.start)
    print(f"{node_count_result}")