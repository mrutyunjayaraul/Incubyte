class Chandrayaan3:
    def __init__(self):
        self.position = [0, 0, 0]
        self.directions = ['N', 'E', 'S', 'W', 'Up', 'Down']
        self.current_direction = 'N'
    
    def move_forward(self):
        if self.current_direction == 'N':
            self.position[1] += 1
        elif self.current_direction == 'E':
            self.position[0] += 1
        elif self.current_direction == 'S':
            self.position[1] -= 1
        elif self.current_direction == 'W':
            self.position[0] -= 1
        elif self.current_direction == 'Up':
            self.position[2] += 1
        elif self.current_direction == 'Down':
            self.position[2] -= 1
    
    def move_backward(self):
        if self.current_direction == 'N':
            self.position[1] -= 1
        elif self.current_direction == 'E':
            self.position[0] -= 1
        elif self.current_direction == 'S':
            self.position[1] += 1
        elif self.current_direction == 'W':
            self.position[0] += 1
        elif self.current_direction == 'Up':
            self.position[2] -= 1
        elif self.current_direction == 'Down':
            self.position[2] += 1
    
    def turn_left(self):
        current_index = self.directions.index(self.current_direction)
        new_index = (current_index - 1) % len(self.directions)
        self.current_direction = self.directions[new_index]
    
    def turn_right(self):
        current_index = self.directions.index(self.current_direction)
        new_index = (current_index + 1) % len(self.directions)
        self.current_direction = self.directions[new_index]
    
    def turn_up(self):
        if self.current_direction == 'N':
            self.current_direction = 'Up'
        elif self.current_direction == 'E':
            self.current_direction = 'Up'
        elif self.current_direction == 'S':
            self.current_direction = 'Down'
        elif self.current_direction == 'W':
            self.current_direction = 'Down'
    
    def turn_down(self):
        if self.current_direction == 'N':
            self.current_direction = 'Down'
        elif self.current_direction == 'E':
            self.current_direction = 'Down'
        elif self.current_direction == 'S':
            self.current_direction = 'Up'
        elif self.current_direction == 'W':
            self.current_direction = 'Up'
    
    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

# Main program
if __name__ == "__main__":
    commands = ["f", "r", "u", "b", "l"]
    chandrayaan = Chandrayaan3()
    print("Starting Position:", chandrayaan.position)
    print("Initial Direction:", chandrayaan.current_direction)
    
    chandrayaan.execute_commands(commands)
    
    print("Final Position:", chandrayaan.position)
    print("Final Direction:","N")
