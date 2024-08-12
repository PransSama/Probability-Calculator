import random

class Hat:
    def __init__(self, **ball_colors):
        """Initializes the Hat with given colors and quantities."""
        self.contents = []
        for color, count in ball_colors.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        """Draws a specified number of balls randomly from the hat."""
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]  # Copy all remaining balls
            self.contents.clear()  # Remove all balls from the hat
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Runs multiple experiments to estimate the probability of drawing certain balls."""
    
    def matches_expected(draw):
        """Checks if the drawn balls match the expected counts."""
        draw_counts = {color: draw.count(color) for color in expected_balls}
        return all(draw_counts.get(color, 0) >= count for color, count in expected_balls.items())
    
    successful_experiments = 0
    
    for _ in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)
        if matches_expected(drawn_balls):
            successful_experiments += 1
    
    return successful_experiments / num_experiments

# Example usage and test case
if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={'red': 2, 'green': 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print(f"Estimated probability: {probability:.3f}")
