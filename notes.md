Part 1 — The vocabulary

These are the words you'll hear over and over. Get comfortable with them.

**Dataset**
Your raw data. Here it's a file of cars: each row has a *mileage* and a *price*. Each row is one *example*.

**Feature (a.k.a. input / variable)**
The thing you use to make a prediction. Here you have a *single feature*: mileage. (More complex models use many features — square footage, age, etc. You have one, which keeps the math clean.)

**Target (a.k.a. label / output)**
The thing you're trying to predict: price.

**Model / Hypothesis**
A function that maps a feature to a predicted target. The subject hands you the model:

```
estimatePrice(mileage) = θ0 + (θ1 × mileage)
```

That's just the equation of a straight line, `y = b + a·x`. Nothing more.

**Parameters (θ0 and θ1 — "theta")**
The two numbers that *define* which line you have.
- `θ1` is the **slope** — how much price changes per unit of mileage (you'd expect it to be negative: more miles, lower price).
- `θ0` is the **intercept** — the predicted price at mileage 0.

These start at `0` and the whole point of "training" is to *find good values* for them.

**Training / Learning**
The process of adjusting θ0 and θ1 so the line fits the data well. This is what makes it "machine learning" — you don't set the line by hand; the algorithm discovers it from the data.

**Cost function (a.k.a. loss / error function)**
A single number that measures *how wrong* your current line is across the whole dataset. Big number = bad line. Small number = good line. Training = making this number as small as possible.

**Gradient descent**
The specific *algorithm* you'll use to minimize the cost function. It's an iterative "walk downhill toward the lowest error" procedure. This is the heart of the project.

**Learning rate**
A small number that controls *how big a step* you take each time you walk downhill. Too big and you overshoot; too small and you take forever. You'll tune this.

θ0 = slide the whole line up/down. Driven by *average* error.
θ1 = rotate the line. Driven by error *weighted by position on the x-axis*
