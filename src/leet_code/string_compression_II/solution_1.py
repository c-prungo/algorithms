def runtime_compression(text: str) -> str:

    res_list = []
    curr = text[0]
    count = 0

    def add_value(char: str, n: int):
        temp = char + (str(n) if n > 1 else "")
        res_list.append(temp)

    for c in text:

        if curr != c:
            add_value(curr, count)
            count = 0
            curr = c

        count += 1

    add_value(curr, count)

    return "".join(res_list)
