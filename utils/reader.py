def read_numbers(file_path):
    f = [float(x) for x in open(file_path)]
    return f

def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")