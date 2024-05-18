import random

class Agent:
    def __init__(self, environment, x_coordinate, y_coordinate):
        self.environment = environment
        self.x = x_coordinate
        self.y = y_coordinate

    def locate_empty_space(self):
        empty_spaces = self.environment.find_empty_spaces()
        return random.choice(empty_spaces) if empty_spaces else None

    def relocate(self, new_location):
        if new_location:
            self.environment.grid[self.y][self.x] = 0  # Mark the old position as empty
            self.x, self.y = new_location
            self.environment.grid[self.y][self.x] = 1  # Mark the new position as occupied

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
        self.agents = []

    def place_agent(self, x, y):
        agent = Agent(self, x, y)
        self.agents.append(agent)
        self.grid[y][x] = 1

    def find_empty_spaces(self):
        return [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == 0]

    def run_simulation(self, num_steps):
        for _ in range(num_steps):
            for agent in self.agents:
                new_location = agent.locate_empty_space()
                agent.relocate(new_location)

    def display_grid(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

def main():
    grid_width, grid_height, agent_count, simulation_steps = 5, 5, 3, 10
    environment = Environment(grid_width, grid_height)

    while len(environment.agents) < agent_count:
        x, y = random.choice(environment.find_empty_spaces())
        environment.place_agent(x, y)

    print("Initial grid:")
    environment.display_grid()

    environment.run_simulation(simulation_steps)

    print(f"\nGrid after {simulation_steps} steps:")
    environment.display_grid()

if __name__ == "__main__":
    main()



