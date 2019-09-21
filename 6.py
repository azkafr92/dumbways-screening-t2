from functools import reduce


def mrBruno(operation, N, arraydigit):
    num_array = ''.join([str(i) for i in range(1, N+1)])
    num_array_digit = [int(num_array[i-1]) for i in arraydigit]
    if operation == 'SUM':
        result = reduce((lambda x, y: x + y), num_array_digit)
        return result
    elif operation == 'MUL':
        result = reduce((lambda x, y: x * y), num_array_digit)
        return result
    elif operation == 'SUB':
        result = reduce((lambda x, y: x - y), num_array_digit)
        return result
    elif operation == 'DIV':
        result = reduce((lambda x, y: x / y), num_array_digit)
        return result
    else:
        return('Please check your operation')


if __name__ == '__main__':
    print(mrBruno('SUM', 20, [11, 13, 15]))

    print(mrBruno('MUL', 20, [12, 15, 17]))

    print(mrBruno('SUB', 20, [12, 15, 17]))

    print(mrBruno('DIV', 20, [12, 15, 17]))
