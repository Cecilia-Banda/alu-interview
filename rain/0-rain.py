 #!/usr/bin/python3
    """This code calculate how many square units of water will be retained after it rains"""
def rain(walls):
    if not walls:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water += right_max - walls[right]
            right -= 1

    return water
