import csv


def estimatePrice(kilometer, theta0, theta1):
    return theta0 + (theta1 * kilometer)


theta00 = 0
theta01 = 0
dataset_min = 0
dataset_max = 0
try:
    with open("theta.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                print("theta.csv row is incomplete, using defaults (0)")
                continue
            theta00 = float(row[0])
            theta01 = float(row[1])
            dataset_min = float(row[2])
            dataset_max = float(row[3])
            print("row ", row)
except FileNotFoundError:
    print("theta.csv not found, using defaults (0). Run train.py first.")
except ValueError:
    print("theta.csv contains invalid values, using defaults (0)")

print("input your cars mileage and i give you the estmated price :)")
while True:
    try:
        mileage = float(input("Enter Millage: "))
        if mileage < 0:
            print("Mileage must be positive")
            continue
        break
    except ValueError:
        print("Enter Millage a mileage in numerical format pls ")
if dataset_max == dataset_min:
    print("no valid training data (dataset range is 0), estimate defaults to 0")
    scaledmilage = 0
else:
    scaledmilage = (mileage - dataset_min) / (
        dataset_max - dataset_min
    )  # need to scale here to so my theata valuesmatch
estimate = estimatePrice(scaledmilage, theta00, theta01)
print("the estimated price for your car based on the mileage is: ", estimate)
