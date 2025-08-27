import operator  
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod
}
def evaluate(numbers, operators):
    for op in operators:
        if op not in ops:
            raise ValueError("Invalid operator: " + op)
    
    result = numbers[0]
    
    for i in range(1, len(numbers)):
        op_index = (i-1) % len(operators)
        # fetch the actual function from the ops dict
        func = ops[operators[op_index]]
        result = func(result, numbers[i])    
    return result
