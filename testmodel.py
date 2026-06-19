import csv


def estimatePrice(kilometer, theta0, theta1):
    return theta0 + (theta1 * kilometer)


theta0 = 0
theta1 = 0
dataset_min = 0
dataset_max = 0

# 1. Load trained parameters
with open("theta.csv", mode="r") as f:
    reader = csv.reader(f)
    for row in reader:
        theta0, theta1 = float(row[0]), float(row[1])
        dataset_min, dataset_max = float(row[2]), float(row[3])

# 2. Load dataset
mileages = []
prices = []
with open("Daten.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))

# 3. Calculate and print percentage errors
total_percentage_error = 0.0
m = len(prices)

print(
    f"{'Mileage (km)':<14} | {'Real Price':<12} | {'Predicted':<12} | {'Difference':<10} | {'% Off'}"
)
print("-" * 65)

for i in range(m):
    # Scale mileage
    scaled_m = (mileages[i] - dataset_min) / (dataset_max - dataset_min)

    # Predict price
    predicted = estimatePrice(scaled_m, theta0, theta1)
    real = prices[i]

    # Calculate absolute difference and percentage error
    diff = abs(real - predicted)
    pct_off = (diff / real) * 100
    total_percentage_error += pct_off

    # Print individual row report
    print(
        f"{mileages[i]:<14,.0f} | ${real:<11,.2f} | ${predicted:<11,.2f} | ${diff:<10,.2f} | {pct_off:.1f}%"
    )

# 4. Final Score
average_error = total_percentage_error / m
overall_accuracy = 100 - average_error

print("-" * 65)
print(f"Overall Model Accuracy: {overall_accuracy:.2f}%")
print(f"Mean Absolute Percentage Error (MAPE): {average_error:.2f}% off")
