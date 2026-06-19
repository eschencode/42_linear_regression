Evaluation Sheet
Introduction
We ask you:

To remain courteous, polite, respectful, constructive.
To clearly highlight with the examined person the possible errors.
To accept that there may sometimes be differences of interpretation on the requests of the subject or the extent of the functionalities.
Guidelines
REMEMBER THAT YOU MUST ONLY CORRECT WHAT IS IN THE STUDENT'S REPOSITORY.

It's a matter of making a "git clone" of the repository, and correcting what's there. If the corrector has not yet done this project, it is mandatory to read the entire subject before starting this defense.

Attachments
Subject Data

Preliminaries
First check the following elements:

There is indeed a project in the git repository
No cheating, the student must be able to explain his code.
There are indeed two programs, one for prediction and one for learning.
Also check that the project is not using a library which itself manages linear regression. If it does, mark the project with Cheat flag.

Yes No

Mandatory part
Prediction before learning
Start the prediction program. The latter should ask you for a mileage: enter any non-zero value. The program displays the result of its prediction which should be 0 since it has not gone through the learning phase.

Check that the equation is of the format: theta0 + (theta1 * x)

Yes No

Learning phase
Ask the team to show you their implementation of linear regression. Check that the equation present in the subject is well implemented, and that the program saves the coefficients theta0 and theta1 at the end of its execution.

Keep in mind that if you don't see the equation but instead a function like numpy.polyfit was used, it's a cheat case and therefore select the Cheat flag.

Yes No

Reading the csv file
The training program reads the csv file and uses it as a reference for training.

Yes No

Simultaneous assignment
This one is a little more complex: check that the two parameters theta0 and theta1 are assigned simultaneously throughout the learning phase.

To do this, check that the result of the two equations of the learning phase are indeed stored in temporary variables, and that at the end of each loop turn theta0 and theta1 are assigned their respective temporary value.

Yes No

Prediction after learning
Run the prediction program one more time, the latter asks you again for a mileage. This time enter a mileage for which you know the price of the car (take an example in the csv file).

The program should show you a price. Is this price consistent with that of the csv? Note that the imprecision between the actual price and the predicted price is completely normal, it is a prediction and not an exact value. It would be suspicious to come across the exact value, it could indicate that we are in a case of over-fitting (a bonus point if correcting it can explain what an over-fitting case is).

Yes No

Bonus part
You can count up to five different bonuses:

a graph which shows the distribution of the data
a graph which shows the results of the training
a program to calculate the precision of the algorithm
Rate it from 0 (failed) through 5 (excellent)

Ratings
Don't forget to check the flag corresponding to the defense
Okay Outstanding project Empty work Incomplete work No author file Invalid compilation Norme Cheat Crash Forbidden function

Pages 1
Find a page or section…
Home
Evaluation Sheet
Introduction
Guidelines
Attachments
Preliminaries
Mandatory part
Prediction before learning
Learning phase
Reading the csv file
Simultaneous assignment
Prediction after learning
Bonus part
Ratings
Don't forget to check the flag corresponding to the defense
Clone this wiki locally
https://github.com/k-off/ft_linear_regression.wiki.git
Footer
