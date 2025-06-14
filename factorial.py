def calculate_factorial(n: int) -> int: 
    if n < 0:
        raise ValueError("Від'ємні числа не мають факторіалу")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    try:
        number = int(input("Введіть ціле число: "))
        result = calculate_factorial(number)
        print(f"Факторіал числа {number} = {result}")
    except ValueError as error:
        print(f"Помилка: {error}")
