def timeConversion(s):
    # Write your code here
    new_clock = 0
    if s.__contains__("PM"):
        b = s.split(":")
        new_clock = int(b[0]) + 12
        if new_clock == 24:
            new_clock = 12
        return str(new_clock) + ":" + b[1] + ":" + str(b[2][0:2])
    elif s.__contains__("AM"):
        b = s.split(":")
        if 0 < int(b[0]) < 12:
            new_clock = int(b[0])
        if new_clock == 12:
            new_clock = new_clock - 12
        return str(0) + str(new_clock) + ":" + b[1] + ":" + str(b[2][0:2])
    return 0
