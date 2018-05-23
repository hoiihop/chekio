def sun_angle(time):
    a = time.split(':')
    degree = 180 / 720
    start = 6 * 60
    end = 18 * 60
    check_time = int(a[0]) * 60 + int(a[1])   
    if start <= check_time <= end:
        return (check_time - start) * degree
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")