def tribonacci_sequence(start_sequence, length):
    sequence = start_sequence[:]
    if length==0:
        return []
    elif length==1:
        return start_sequence[:1]
    elif length==2:
        return start_sequence[:2]
    elif length==3:
        return start_sequence
    else:
        while len(sequence)<length:
            total = sum(sequence[-3:])
            sequence.append(total)
    return sequence

tribonacci_sequence([0, 0, 1], 20)


