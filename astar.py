import sys
from math import sqrt
import numpy as np
import random

# GLOBALS
N = 3
HEURISTIC = 1
GOAL_STATE = []


# Returns node which has the lowest score.
# If two nodes have the same f score, returns the one which has bigger g (actual) score.
def get_lowest_scored_node(nodes):
    lowest_scored_node = nodes[0]
    for i in range(1, len(nodes)):
        if nodes[i].f == lowest_scored_node.f:
            if nodes[i].g > lowest_scored_node.g:
                lowest_scored_node = nodes[i]
            continue

        if nodes[i].f < lowest_scored_node.f:
            lowest_scored_node = nodes[i]

    return lowest_scored_node


# A* algorithm. Returns solution node and number of nodes visited.
def astar(start_node):
    # Creating lists for opened and closed nodes
    global N, GOAL_STATE
    opened_nodes = []
    closed_nodes = []
    step = 0

    # Configuring start and end nodes
    start_node.g = start_node.h = start_node.f = 0
    GOAL_STATE = make_goal_state(N)
    end_node = Node(None, [N - 1, N - 1], GOAL_STATE)
    end_node.g = end_node.h = end_node.f = 0

    # Adding first node / starting node to the opened list
    opened_nodes.append(start_node)

    while opened_nodes:
        current_node = get_lowest_scored_node(opened_nodes)
        closed_nodes.append(current_node)
        if np.array_equal(current_node.state, end_node.state):
            return current_node, step

        for successor_node in current_node.children():
            node_already_exists = search_for_node_by_state(opened_nodes, successor_node)
            if node_already_exists:

                if successor_node.f < node_already_exists.f:
                    opened_nodes.remove(node_already_exists)

            node_already_exists = search_for_node_by_state(closed_nodes, successor_node)
            if node_already_exists:
                if successor_node.f < node_already_exists.f:
                    closed_nodes.remove(node_already_exists)

            opened_nodes.append(successor_node)
        opened_nodes.remove(current_node)
        step += 1


# Returns node if it is in the list.
# Otherwise returns None.
def search_for_node_by_state(node_list, node):
    for x in node_list:
        if np.array_equal(x.state, node.state):
            return x
    return None


# Returns position of given value in the goal_state.
def get_goal_position_of(value):
    global GOAL_STATE
    for i in range(0, N):
        for j in range(0, N):
            if GOAL_STATE[i][j] == value:
                return i, j


# Helper class
class Node:
    global N, HEURISTIC
    states = [[-1, 1, 0, 0],
              [0, 0, -1, 1]]
    SPACE = 0

    # Constructor
    def __init__(self, parent=None, position=None, state=None):
        self.parent = parent
        self.position = position

        if self.parent:
            self.g = self.parent.g + 1  # actual

        self.h = 0  # hypothetical
        self.f = 0  # total
        self.state = state

    # Calculates h score
    def calculate_hypothetical_cost(self):
        cost = 0
        if HEURISTIC == 1:
            # Wrong tiles count
            for i in range(0, N):
                for j in range(0, N):
                    if self.state[i][j] != GOAL_STATE[i][j]:
                        cost += 1

        else:
            # Manhattan distance
            for i in range(0, N):
                for j in range(0, N):
                    goal_i, goal_j = get_goal_position_of(self.state[i][j])
                    cost += abs(goal_i - i) + abs(goal_j - j)

        return cost

    # Generates and returns children nodes.
    def children(self):
        children = []
        for i in range(0, 4):
            new_space_coordinates = [self.position[0] + self.states[0][i], self.position[1] + self.states[1][i]]
            if new_space_coordinates[0] < 0 or new_space_coordinates[0] > N - 1 \
                    or new_space_coordinates[1] < 0 or new_space_coordinates[1] > N - 1:
                continue

            movement = self.state[new_space_coordinates[0]][new_space_coordinates[1]]
            new_state = np.copy(self.state)
            new_state[new_space_coordinates[0]][new_space_coordinates[1]] = self.SPACE
            new_state[self.position[0]][self.position[1]] = movement

            ch = Node(parent=self, position=new_space_coordinates, state=new_state)
            ch.h = ch.calculate_hypothetical_cost()
            ch.f = ch.g + ch.h
            children.append(ch)
            # ch.print_state()
        return children

    # Pretty prints state of a node.
    def print_state(self):
        for i in range(0, N):
            for j in range(0, N):
                if self.position[0] == i and self.position[1] == j:
                    print("__", end=' ')
                else:
                    print(self.state[i][j], end=' ')
            print("\n")
        print(" - - - - - - ")

    # Generates M stepped random state by the moving the space.
    def generate_map_M_step(self, steps):
        nodes = np.zeros((steps, N, N))
        idx = 0
        step_counter = 0
        while True:
            step_counter += 1
            eq_found = False
            while True:
                i = random.randint(0, 3)
                new_space_coordinates = [self.position[0] + self.states[0][i], self.position[1] + self.states[1][i]]
                if 0 <= new_space_coordinates[0] <= N - 1 \
                        and 0 <= new_space_coordinates[1] <= N - 1:
                    break
            saved_state = np.copy(self.state)
            saved_position = np.copy(self.position)
            movement = self.state[new_space_coordinates[0]][new_space_coordinates[1]]
            self.state[new_space_coordinates[0]][new_space_coordinates[1]] = self.SPACE
            self.state[self.position[0]][self.position[1]] = movement
            self.position = new_space_coordinates
            for x in nodes:
                if np.array_equal(x, self.state):
                    eq_found = True

            if eq_found:
                step_counter -= 1
                self.state = np.copy(saved_state)
                self.position = np.copy(saved_position)
            else:
                nodes[idx] = np.copy(self.state)
                idx += 1

            if step_counter == steps:
                break

        return self

    # Returns the position of the space, denoted by SPACE constant.
    def find_space(self):
        for i in range(0, N):
            for j in range(0, N):
                if self.state[i][j] == self.SPACE:
                    return i, j


# Generates and returns goal state as a matrix.
def make_goal_state(rows):
    return np.append(np.arange(1, rows * rows), 0).reshape((rows, rows))


# Generates state matrix from array.
def make_state_from_array(array, dimension):
    return array.reshape((dimension, dimension))


# Recursive function to print solution sequence.
def print_solution_sequence(node):
    if node.parent:
        print_solution_sequence(node.parent)
    else:
        print("*Including original state*")
    node.print_state()


# Configures A* algorithm, responsible for fulfilling the switch requirements (printing out, reading console input etc)
def astar_strategy(heuristic, write_solution_seq, write_cost, write_visited_node_counter, input_file):
    global N, HEURISTIC

    HEURISTIC = heuristic

    if input_file:
        f = open(input_file, "r")
        arr = list(map(int, f.read().split()))
    else:
        print(
            "Please type in the numbers in the same line separated by a space."
            "The space in the puzzle must be indicated with a 0")
        arr = list(map(int, input().split()))

    # Making start node
    N = int(sqrt(len(arr)))
    start_node = Node(None, None, make_state_from_array(np.asarray(arr), N))
    i, j = start_node.find_space()
    start_node.position = [i, j]
    # start_node.print_state() # optional for printing original state

    # Running A* algorithm
    node, steps = astar(start_node)

    # Results
    print("*************************** Solution found! ***************************")
    if write_visited_node_counter:
        print("Visited nodes:", steps)
    if write_cost:
        print("Cost of solution is:", node.f)
    if write_solution_seq:
        print("Solution sequence is:")
        print_solution_sequence(node)


# Main, handles switch inputs.
def main(args):
    global N
    write_solution_seq = False
    write_cost = False
    write_visited_node_counter = False
    heuristic = 1
    input_file = None
    for i in range(0, len(args)):
        if args[i] == "-h":
            i += 1
            heuristic = int(args[i])
            print("Heuristic: ", heuristic)
            continue

        if args[i] == "-input":
            i += 1
            input_file = args[i]
            print("Reading map from file named: ", input_file)
            continue

        if args[i] == "-solseq":
            write_solution_seq = True
            print("Solution sequence will be printed...")
            continue

        if args[i] == "-pcost":
            write_cost = True
            print("Cost of the solution will be printed...")
            continue

        if args[i] == "-nvisited":
            write_visited_node_counter = True
            print("Visited node counter will be printed...")
            continue

        if args[i] == "-rand":
            i += 1
            N = int(args[i])
            i += 1
            m_steps = int(args[i])
            print("Random map will be generated with size of ", N, " and ", m_steps, " steps...")

            goal_state = make_goal_state(rows=N)
            node = Node(state=goal_state, position=[N - 1, N - 1])
            node.generate_map_M_step(m_steps).print_state()
            return

    astar_strategy(heuristic, write_solution_seq, write_cost, write_visited_node_counter, input_file)


if __name__ == "__main__":
    main(sys.argv[1:])
