import re

def answer(question):
    exp = re.compile(r'^What is (-?\d+)(.+)?\?$')
    m = re.match(exp, question)
    if m:
        result = int(m[1])
        if m[2]:
            ops = re.compile(r'([^-]+?)(-?\d+)')
            match = re.findall(ops, m[2])
            if not match:
                raise ValueError("that question doesn't make sense to me")
            for operation in match:
                operator, number = operation
                operator = operator.strip()
                if operator == "plus":
                    result += int(number)
                elif operator == "minus":
                    result -= int(number)
                elif operator == "multiplied by":
                    result *= int(number)
                elif operator == "divided by":
                    if number == 0:
                        raise ValueError('cannot divide by 0')
                    result /= int(number)
                else:
                    raise ValueError('operation not understood')
        return result
    else:
        raise ValueError("that question doesn't make sense to me")

