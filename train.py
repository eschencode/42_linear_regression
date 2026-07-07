import argparse
import csv


def estimatePrice(kilometer, theta0, theta1):
    return theta0 + (theta1 * kilometer)


# need to scale dataset to combat imbalance between the two parameters gradients
def scaleDataset(milleages, dataset_min, dataset_max):
    scaledDataset = []
    totalelements = len(milleages)
    for i in range(totalelements):
        scaledDataset.append((mileages[i] - dataset_min) / (dataset_max - dataset_min))
    return scaledDataset


def training(theta0, theta1, scaled_milleages, learningRate, iterations):
    sum0 = 0.0
    sum1 = 0.0
    m = len(scaled_milleages)
    for j in range(iterations):
        sum0 = 0
        sum1 = 0
        for i in range(m):
            estimatedPrice = estimatePrice(scaled_milleages[i], theta0, theta1)
            error = estimatedPrice - prices[i]
            sum0 += error
            sum1 += error * scaled_milleages[i]
            # scaled the millage becuse if not sum1 very imbalenced for example error times 250 k kilometers is in millions but still same learning rate as sum0
        # adjust values after each batch
        temp0 = theta0 - (learningRate / m) * sum0
        temp1 = theta1 - (learningRate / m) * sum1
        theta0 = temp0
        theta1 = temp1
    return (theta0, theta1)


def draw_nonscaled(mileages, theta0, theta1, dataset_min, dataset_max):
    import matplotlib.pyplot as plt

    plt.scatter(mileages, prices, color="blue", label="Actual Data")

    line_x = [min(mileages), max(mileages)]

    raw_theta1 = theta1 / (dataset_max - dataset_min)
    raw_theta0 = theta0 - (theta1 * dataset_min) / (dataset_max - dataset_min)

    line_y = [estimatePrice(x, raw_theta0, raw_theta1) for x in line_x]

    plt.plot(line_x, line_y, color="red", linewidth=2, label="Line of Best Fit")
    plt.xlabel("Mileages")
    plt.ylabel("Prices")
    plt.title("Car Prices vs. Mileage")
    plt.legend()
    plt.show()


def draw_scaled(scaled_milleages, theta0, theta1):
    import matplotlib.pyplot as plt

    # 1. Draw the raw data points (Scatter plot)
    plt.scatter(scaled_milleages, prices, color="blue", label="Actual Data")

    # 2. Calculate the points for your regression line
    # We take the minimum and maximum scaled mileages to draw a straight line across the plot
    line_x = [min(scaled_milleages), max(scaled_milleages)]
    line_y = [estimatePrice(x, theta0, theta1) for x in line_x]

    # 3. Draw the regression line on top of the scatter plot
    plt.plot(line_x, line_y, color="red", linewidth=2, label="Line of Best Fit")

    # 4. Add labels, a title, and a legend so it looks clean
    plt.xlabel("Scaled Mileages (0 to 1)")
    plt.ylabel("Prices")
    plt.title("Car Prices vs. Scaled Mileage")
    plt.legend()  # Displays the "Actual Data" and "Line of Best Fit" labels

    # 5. Render the graph window
    plt.show()


def read_dataset(filename):
    mileages = []
    prices = []
    # read data
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            mileages.append(float(row[0]))
            prices.append(float(row[1]))
    return mileages, prices


def validate_dataset(mileages):
    # validate dataset before training
    if len(mileages) == 0:
        print("Daten.csv has no data, cannot train")
        exit(1)
    # find min and max value --> save in to theta csv too
    dataset_min = min(mileages)
    dataset_max = max(mileages)
    if dataset_max == dataset_min:
        print("all mileages are identical (range is 0), cannot scale/train")
        exit(1)
    return dataset_min, dataset_max


theta0 = 0.0
theta1 = 0.0
learningRate = 0.1
iterations = 1000
print("starting thetas: ", theta0, theta1)

mileages, prices = read_dataset("data.csv")

dataset_min, dataset_max = validate_dataset(mileages)

scaled_milleages = scaleDataset(mileages, dataset_min, dataset_max)

theta0, theta1 = training(theta0, theta1, scaled_milleages, learningRate, iterations)

print("Training complete!")
print("Final theta0:", theta0)
print("Final theta1:", theta1)

# write result to theta.csv
with open("theta.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([theta0, theta1, dataset_min, dataset_max])

parser = argparse.ArgumentParser()
parser.add_argument("--draw", action="store_true")
parser.add_argument("--drawscaled", action="store_true")
args = parser.parse_args()

if args.draw:
    draw_nonscaled(mileages, theta0, theta1, dataset_min, dataset_max)
if args.drawscaled:
    draw_scaled(scaled_milleages, theta0, theta1)
