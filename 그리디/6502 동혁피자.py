i = 1

while True:
    length = input()
    if length == '0':
        break
    else:
        r, w, l = map(int, length.split())

        table = r*2  #지름의 길이
        pizza = (w**2 + l**2) ** 0.5  #대각선 길이

        if table >= pizza:
            print(f"pizza {i} fits on the table.")
        else:
            print(f"pizza {i} does not fit on the table.")
        i += 1