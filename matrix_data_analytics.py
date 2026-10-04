import math

def calculate_statistics(data):
    """Calculates Mean and Standard Deviation for Statistical Data Analysis"""
    if not data:
        return 0, 0
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_deviation = math.sqrt(variance)
    return mean, std_deviation

def multiply_matrices(matrix_a, matrix_b):
    """Executes Matrix Multiplication - The Foundation of Machine Learning Algorithms"""
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

# --- Execution of the Computational Diagnostic Test ---
if __name__ == "__main__":
    sample_dataset = [12, 15, 29, 34, 45, 52, 60]
    avg, steps = calculate_statistics(sample_dataset)
    print(f"[DATA ANALYTICS] Dataset Mean: {avg:.2f}, Standard Deviation: {steps:.2f}")

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(f"[ALGORITHM] Matrix Multiplication Result: {multiply_matrices(mat1, mat2)}")
