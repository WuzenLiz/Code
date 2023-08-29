"""he game is played on a map 16000 units wide and 9000 units high. The coordinate X=0, Y=0 is the top left pixel.

The checkpoints work as follows:
The checkpoints are circular, with a radius of 600 units.
The disposition of the checkpoints is selected randomly for each race.
The pods work as follows:
If none of your pods make it to their next checkpoint in under 100 turns, you are eliminated and lose the game.
The pods may move normally outside the game area.

Rules
The circuit of the race is made up of checkpoints. To complete one lap, your vehicle (pod) must pass through each checkpoints in order and back through the start. The first player to reach the starting checkpoint on the final lap wins.

The pods work as follows:
To pass a checkpoint, the center of a pod must be inside the radius of the checkpoint.
To move a pod, you must print a target destination point followed by a thrust value. Details of the protocol can be found further down.
The thrust value of a pod is its acceleration and must be between 0 and 100.
You can use 1 acceleration boost in the race, you need only replace the thrust value by the BOOST keyword.
The pods have a circular force-field around their center, with a radius of 400 units, which activates in case of collisions with other pods.
"""


def boost(thrust, angle, Ox, Oy, Dist,boosted):
    """
    Improve the boost logic beyond opponent and next checkpoint.
    """
    if angle > 90 or angle < -90:
        return 0
    if (Ox - Ox) ** 2 + (Oy - Oy) ** 2 < 640000 and not boosted:
        return "BOOST"
    elif Dist < 8000:
        return thrust * 2
    else:
        return thrust

def calculate_thrust(distance):
    thrust_levels = {
        5000: 100, 2000: 50, 1000: 25, 500: 10, 250: 5, 100: 1, 0: 0
    }
    for threshold, thrust in thrust_levels.items():
        if distance > threshold:
            return thrust
    return 0

def main():
    boosted = False
    while True:
        x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
        opponent_x, opponent_y = [int(i) for i in input().split()]

        next_checkpoint_thrust = calculate_thrust(next_checkpoint_dist)
        boosted_thrust = boost(next_checkpoint_thrust, next_checkpoint_angle, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist,boosted)
        if boosted_thrust == "BOOST":
            boosted = True
        if (x - opponent_x) ** 2 + (y - opponent_y) ** 2 < 202500:
            boosted_thrust = "SHIELD"

        print(f"{next_checkpoint_x} {next_checkpoint_y} {boosted_thrust} {boosted_thrust}")

if __name__ == "__main__":
    main()
