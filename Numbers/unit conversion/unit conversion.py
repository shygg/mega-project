
print("-" * 20)
print("type number + space + unit", "type: 'kg' to convert to lbs","'lbs' to kg", "feet/meter")
raw_user = input()


def make_sense_of(raw_user):
    try:
        raw = raw_user.split()
        if len(raw) != 2:
            print("you goofed 1")
        number = float(raw[0])
        from_unit = str(raw[1])
    except:
        print("you goofed")

    result = False

    if "kg" in from_unit:
        result = 2.205 * number
    elif "lbs" in from_unit:
        result = number / 2.205
    elif "feet" in from_unit:
        result = 0.3048 * number
    elif "meter" in from_unit:
        result = number / 0.3048
    return result


print(make_sense_of(raw_user))

input()