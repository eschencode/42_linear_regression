# Linear Regression Car Price Predictor

A simple yet effective linear regression model that predicts car prices based on mileage. This project implements gradient descent optimization from scratch to train the model.

## Features

- **Data Scaling**: Normalizes input features to [0, 1] range for better training
- **Gradient Descent**: Trains the model using batch gradient descent
- **Visualization**: Plots both scaled and non-scaled regression lines
- **CSV Storage**: Saves trained parameters for later use
- **CLI Flags**: Easy control over training and visualization modes

## Setup

```bash
# Clone/navigate to the project directory
cd ft_linear_regression

# Install dependencies
pip install matplotlib numpy

# Prepare your data
# Ensure you have a Daten.csv file with format:
# mileage,price
# 10000,15000
# 20000,12000
# ...
```

## Usage

### Train the model
```bash
python train.py
```

### Train and visualize scaled data
```bash
python train.py --drawscaled
```

### Train and visualize non-scaled data
```bash
python train.py --draw
```

### Make predictions
```bash
python predict.py <mileage>
```

## How It Works

1. **Data Loading**: Reads mileage and price data from `Daten.csv`
2. **Scaling**: Normalizes mileage values to [0, 1] range
3. **Training**: Applies gradient descent to minimize prediction error
4. **Visualization**: Plots actual data points and the fitted regression line
5. **Storage**: Saves `theta0` and `theta1` parameters to `theta.csv`

## Parameters

- **Learning Rate**: 0.1 (controls step size during training)
- **Iterations**: 1000 (number of gradient descent steps)

## Output

- `theta.csv`: Stores trained parameters (theta0, theta1, dataset_min, dataset_max)
- Visualization plots: Show regression fit on your data

## Project Structure

```
ft_linear_regression/
├── train.py              # Training script
├── predict.py            # Prediction script
├── Daten.csv            # Input data
├── theta.csv            # Trained parameters
└── README.md            # This file
```
