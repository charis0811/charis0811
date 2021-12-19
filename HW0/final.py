has_mark = None

def get_head_number(in_str, no_sign=False):
    if not len(in_str):
        return None, in_str 
    if no_sign and in_str[0] in ["+", "-"]:
        return None, in_str
    number = 1
    if in_str[0] == "+":
        in_str = in_str[1:] 
    if in_str[0] == "-":
        number = -1 
        if not in_str[1].isnumeric(): 
            in_str = in_str[1:] 
    if in_str[0].isnumeric():
        index = 1
        while(index < len(in_str) and in_str[:index+1].isnumeric()):
            index += 1
        number *= int(in_str[:index])
        in_str = in_str[index:]
    return number, in_str


def trim_head_mark(in_str):
    if not len(in_str):
        return in_str
    return in_str[1:] if in_str[0] in ["*", "^"] else in_str


def add_times(in_str, times):
    if times == -1:
        return "-" + in_str
    if times != 1:
        return str(times) + ("*" if has_mark else "") + in_str
    return in_str


def to_string(variables, times=None):
    output = "".join(
        [f"""{v}{'' if variables[v] == 1 else f'{"^" if has_mark else ""}{variables[v]}'}""" for v in sorted(
            variables.keys())]
    )
    if times is not None:
        return add_times(output, times)
    return output


def extrate(in_str):
    output = {}
    while True:
        times, in_str = get_head_number(in_str)
        in_str = trim_head_mark(in_str)
        variables = {}
        while True:
            variable, in_str = in_str[0], in_str[1:]
            in_str = trim_head_mark(in_str)
            power, in_str = get_head_number(in_str, no_sign=True)
            if power is None:
                variables[variable] = 1
                break
            variables[variable] = power
            if not len(in_str) or in_str[0] in ["+", "-"]:
                break
        output[to_string(variables)] = {"times": times, "variables": variables}
        if not len(in_str):
            break
    return output


def multiply(a, b):
    if not a:
        return b
    output = {}
    for p1 in a.values(): 
        for p2 in b.values(): 
            buffer = {**p1["variables"]}
            for v, n in p2["variables"].items():
                if v in buffer.keys():
                    buffer[v] += n 
                else: 
                    buffer[v] = n
            key = to_string(buffer) 
            if key in output: 
                output[key]["times"] += p1["times"] * p2["times"] 
            else:
                output[key] = {
                    "times": p1["times"] * p2["times"],
                    "variables": buffer
                }
    return output


def multiplicative_polynomails(in_str):
    result = {}
    while in_str.find(")") != -1:
        index = in_str.find(")")
        result = multiply(result, extrate(in_str[1:index]))
        in_str = in_str[index+1:]
    output = ""
    for k in result.keys():
        if output:
            output += ("+" if result[k]["times"] >
                       0 else "") + add_times(k, result[k]["times"])
        else:
            output = add_times(k, result[k]["times"])
    return output


q = input("Input the polynomials: ")
has_mark = "*" in q or "^" in q 

print("Output Result:", multiplicative_polynomails(q))