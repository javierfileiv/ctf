import re


def part2(touple_local_turns):
    cross_0 = 0
    cursor = 50
    total_dial = 100

    for turn in touple_local_turns:
        turn_int = 0
        direction = turn[0]
        steps = turn[1]
        print(f"Direction: {direction}, Steps: {steps}, Cursor before mod: {cursor}")
        rotations, steps = divmod(steps, total_dial)
        cross_0 += rotations

        if steps % total_dial != 0:
            if direction == "L":
                if (cursor - steps) < 0 :
                    if cursor != 0:
                        cross_0 += 1
                    cursor = total_dial - (steps - cursor)
                else:
                    if (cursor - steps) == 0:
                        cross_0 += 1
                    cursor = cursor - steps
            elif direction == "R":
                if (cursor + steps) >= 100:
                    cross_0 += 1
                cursor = (cursor + steps) % total_dial

        # if(turn == ('R', 20)):
        #     # breakpoint()
        #     pass
        # #calculate cross by 0
        # cross_0 += abs(turn_int) // total_clicks
        # turn_int = turn_int % total_clicks

        print(f"Cursor at: {cursor}, Crossed 0: {cross_0}")

    print(f"Final Cursor Position: {cursor}, Total Crossed 0: {cross_0}")

    return cross_0, cursor


if __name__ == "__main__":
    regex = "([LR])(\d+)"
    touple_turns = ()
    rg = re.compile(regex)

    # first parse file to fill in map
    with open("/home/fixp/sourceCode/AOC/day1/rotations.txt", "r") as file:
        for line in file:
            # skip commented lines
            if line.startswith("#"):
                continue
            if line != "\n":
                match = rg.match(line)
                groups = match.groups()
                direction = groups[0]
                steps = int(groups[1])
                touple_turns += ((direction, steps),)
    part2(touple_turns)
