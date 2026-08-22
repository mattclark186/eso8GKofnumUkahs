# Customer Survey Analysis

This project aimed to use machine learning to create a model that can accurately predict whether a customer was happy overall based on their response to several survey questions.

The final outcome was an XGBoost model that can predict happiness with 81% accuracy.

This was all completed using Python.

## The Brief

The client was a growing logistics and delivery start-up that was trying to understand more about their customers' experiences. They wanted to be able to predict what makes customers happy in order to take necessary actions to improve. They also wanted to know which questions made the most difference to overall happiness so that they could identify which areas of the experience to focus on.

## The Data

The data came from a customer survey that contained responses from 126 customers who answered 7 questions - 6 specific questions about their experience, rated 1-5 (to be used as the features) and whether they were happy overall, yes or no (to be used as the target).

| Question | Description | Scoring |
|---|---|---|
| X1 | My order was delivered on time | 1 - 5 |
| X2 | Contents of my order was as I expected | 1 - 5 |
| X3 | I ordered everything I wanted to order | 1 - 5 |
| X4 | I paid a good price for my order | 1 - 5 |
| X5 | I am satisfied with my courier | 1 - 5 |
| X6 | The app makes ordering easy for me | 1 - 5 |
| Y | I was happy overall | Yes/No |

## Project Process

**Exploratory Data Analysis**
- Checked and found no bad data points (e.g. a non-integer survey response, a response greater than 5 or less than 1 etc.)
- Checked and found no null values
- Every feature and the target had the same number of values
- No features were highly correlated with each other or the target
- Created histograms displaying the frequency of each response to each feature question

[EDA Notebook](/notebooks/exploration/EDA.ipynb)

**Modelling**
- Used lazy predict to establish which models may be effective
- Went forward with KNeighbors, BernoulliNB, RandomForest and XGBoost
- Used GridSearchCV to tune the hyperparameters of each model
- XGBoost performed better than the others, but still only achieved a moderate accuracy
- Tried each subset of features
- Managed to achieve 81% accuracy with XGBoost using just 2 features

[Modelling Notebooks](/notebooks/modelling)

## Conclusion

The final model used was XGBoost and achieved the following metrics:

- Accuracy: 0.81
- Recall: 0.80
- Precision: 0.81
- F1: 0.81

And did so using just 2 features of the available 6:

- X1: My order was delivered on time
- X5: I am satisfied with my courier

This data is sufficient to predict whether a customer is happy overall with 81% accuracy. It's worth noting that X1 is nearly twice as important as X5 (62% and 38% respectively). Therefore, the recommendation to the client was to reduce the customer survey to just these 2 questions, simplifying the data collection process.
