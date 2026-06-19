import csv


def estimatePrice(kilometer, theta0, theta1):
    return theta0 + (theta1 * kilometer)


theta00 = 0
theta01 = 0
dataset_min = 0
dataset_max = 0
with open("theta.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        theta00 = float(row[0])
        theta01 = float(row[1])
        dataset_min = float(row[2])
        dataset_max = float(row[3])
        print("row ", row)

print("input your cars mileage and i give you the estmated price :)")
while True:
    try:
        mileage = float(input("Enter Millage: "))
        if mileage < 0:
            print("Mileage must be positive")
            continue
        # if mileage > 100000000:
        #    print("no car runs 100 millon kilometers ;)")
        #    continue
        break
    except ValueError:
        print("Enter Millage a mileage in numerical format pls ")
scaledmilage = (mileage - dataset_min) / (dataset_max - dataset_min)
estimate = estimatePrice(scaledmilage, theta00, theta01)
print("the estimated price for your car based on the mileage is: ", estimate)
