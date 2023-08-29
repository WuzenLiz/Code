import math
from collections import defaultdict
import random

class GameState:
    def __init__(self):
        self.main_board = [['.' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def get_legal_actions(self):
        legal_actions = []
        for row in range(3):
            for col in range(3):
                if self.main_board[row][col] == '.':
                    legal_actions.append((row, col))
        return legal_actions

    def apply_action(self, action):
        row, col = action
        if self.main_board[row][col] == '.':
            self.main_board[row][col] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
        else:
            raise ValueError("Invalid action: Square is already occupied")

    def is_terminal(self):
        # Implement terminal state check based on game rules
        # For example, check if there's a winner or if the board is full
        return False

class MCTSNode:
    def __init__(self, state):
        self.state = state
        self.visit_count = 0
        self.action_values = defaultdict(int)
        self.children = []

def select(node):
    while not node.state.is_terminal():
        if len(node.children) < len(node.state.get_legal_actions()):
            # If there are unexplored actions, return a newly expanded node
            return expand(node)
        
        # Choose the child node with the highest UCB value
        best_child = None
        best_ucb_value = -float('inf')
        for child in node.children:
            ucb_value = (
                child.action_values / child.visit_count +  # Q(s, a)
                math.sqrt(math.log(node.visit_count) / child.visit_count)  # UCB term
            )
            if ucb_value > best_ucb_value:
                best_ucb_value = ucb_value
                best_child = child
        
        node = best_child  # Move to the selected child node
    
    return node  

def expand(node):
    legal_actions = node.state.get_legal_actions()
    
    for action in legal_actions:
        new_state = node.state.copy()  # Create a copy of the current state
        new_state.apply_action(action)  # Apply the action to the new state
        new_child = MCTSNode(new_state)  # Create a new child node
        node.children.append(new_child)  # Add the child node to the parent's children
    
    # Return one of the newly created child nodes
    return node.children[0]

def simulate(node):
    current_state = node.state.copy()  # Create a copy of the current state

    while not current_state.is_terminal():
        legal_actions = current_state.get_legal_actions()
        random_action = random.choice(legal_actions)  # Choose a random action
        current_state.apply_action(random_action)  # Apply the action

    # Determine the result of the simulation based on the terminal state
    if current_state.is_winner('X'):  # Replace with your own method for checking a win
        return 1  # You win
    elif current_state.is_winner('O'):  # Replace with your own method for checking a win
        return -1  # Opponent wins
    else:
        return 0

def backpropagate(node, result):
    while node is not None:
        node.visit_count += 1
        # Update action values based on the simulation result
        if node.state.current_player == 'X':
            node.action_values[action] += result
        else:
            node.action_values[action] -= result
        node = node.parent

def get_best_child(node):
    best_child = None
    best_value = -float('inf')

    for child in node.children:
        # Calculate the UCB value or estimated action value
        ucb_value = child.action_values / child.visit_count + math.sqrt(math.log(node.visit_count) / child.visit_count)
        
        if ucb_value > best_value:
            best_value = ucb_value
            best_child = child

    return best_child

def mcts(root_state, num_iterations):
    root_node = MCTSNode(root_state)
    
    for _ in range(num_iterations):
        selected_node = select(root_node)
        expanded_node = expand(selected_node)
        simulation_result = simulate(expanded_node)
        backpropagate(expanded_node, simulation_result)
    
    best_child = get_best_child(root_node)
    return best_child.state

# Game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    valid_actions = []
    for _ in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
        valid_actions.append((row, col))
    
    game_state = GameState()  # Create a new game state
    for action in valid_actions:
        game_state.apply_action(action)
    
    chosen_state = mcts(game_state, num_iterations=1000)
    
    print(chosen_state[0], chosen_state[1])
