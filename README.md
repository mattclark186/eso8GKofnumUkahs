# Customer Survey Analysis

This project aimed to use machine learning to create a model that can accurately predict whether a customer was happy overall based on their response to several survey questions.

The final model was an XGBoost classifier, achieving 81% accuracy using just 2 of the 6 available features.

This was all completed using Python.

## The Brief

The client was a growing logistics and delivery start-up that was trying to understand more about their customers' experiences. They wanted to be able to predict customer happiness from survey responses and specifically wanted to know which questions made the most difference to overall happiness. This would help them identify which areas to focus on to improve their service for their customers.

## The Data

The data came from a customer survey that contained responses from 126 customers who answered 7 questions - 6 specific questions about their experience, rated 1-5 (to be used as the features) and whether they were happy overall, yes or no (to be used as the target).

| Question | Description | Scoring | Type |
|:---:|---|:---:|:---:|
| X1 | My order was delivered on time | 1 - 5 | Feature |
| X2 | Contents of my order was as I expected | 1 - 5 | Feature |
| X3 | I ordered everything I wanted to order | 1 - 5 | Feature |
| X4 | I paid a good price for my order | 1 - 5 | Feature |
| X5 | I am satisfied with my courier | 1 - 5 | Feature |
| X6 | The app makes ordering easy for me | 1 - 5 | Feature |
| Y | I was happy overall | Yes/No | Target |

## Analysis and Modelling

**Exploratory Data Analysis**

[EDA Notebook](/notebooks/exploration/EDA.ipynb)
- Checked and found no bad data points (e.g. a non-integer survey response, a response greater than 5 or less than 1 etc.)
- Checked and found no null values
- Every feature and the target had the same number of values
- No features were highly correlated with each other or the target
- Created histograms displaying the frequency of each response to each feature question

**Modelling**
- Used LazyPredict to establish which models may be effective
- Went forward with KNeighbors, BernoulliNB, RandomForest and XGBoost
    - [LazyPredict](/notebooks/modelling/lazy_predict.ipynb)
    - [KNeighbors](/notebooks/modelling/knn.ipynb)
    - [BernoulliNB](/notebooks/modelling/bnb.ipynb)
    - [RandomForest](/notebooks/modelling/random_forest.ipynb)
    - [XGBoost](/notebooks/modelling/xgb_model.ipynb)
- Used GridSearchCV to tune the hyperparameters of each model
- XGBoost performed better than the others, but still only achieved a moderate accuracy
- Evaluated each model using each possible combination of features to see if a smaller feature set could improve performance
- Managed to achieve 81% accuracy with XGBoost using just 2 features

**Model Performance**

| Model Type | Features Used | Accuracy | F1 | Precision | Recall |
| :---: | :---: | :---: | :---: | :---: | :---: |
| KNeighbors | All | 62% | 55% | 67% | 59 |
| BernoulliNB | All | 69% | 68% | 69% | 68% |
| RandomForest | All | 77% | 77% | 77% | 77% |
| XGBoost | All | 73% | 71% | 77% | 71% |
| RandomForest | X1, X5 | 81% | 81% | 81% | 80% |
| XGBoost | X1, X5 | 81% | 81% | 81% | 81% |

## Conclusion

The final model used was XGBoost and achieved the following metrics:

- 0.81 Accuracy
- 0.80 Recall
- 0.81 Precision
- 0.81 F1

And did so using just 2 features of the available 6:

- X1: My order was delivered on time
- X5: I am satisfied with my courier

With the available data, this was the best feature combination. It's worth noting that X1 was nearly twice as important as X5 (62% and 38% respectively). Therefore, the recommendation to the client was that the survey could be reduced to just these 2 questions, simplifying the data collection process without impacting the predictive power of the data.