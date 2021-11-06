class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, degree = 0, 0, 0
        for letter in instructions:
            if letter == "L":
                degree -= 90
            elif letter == "R":
                degree += 90
            elif letter == "G":
                if degree % 360 == 0:
                    x += 1
                elif degree % 360 == 90:
                    y -= 1
                elif degree % 360 == 180:
                    x -= 1
                elif degree % 360 == 270:
                    y += 1

        return (x == 0 and y == 0) or (degree % 360 != 0)
