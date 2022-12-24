# University Admission Prediction

This project aims to predict the likelihood of a student being admitted to a university based on various factors. We used a sample dataset of 400 student records, and employs four different machine learning methods to make the predictions: linear regression, random forest, k-nearest neighbors (KNN), and a voting regressor that combines the predictions of the first three methods.

## Dataset

There are seven variables used in this project:

* GRE Scores ( out of 340 )
* TOEFL Scores ( out of 120 )
* University Rating ( out of 5 )
* Statement of Purpose (SOP) Strength ( out of 5 )
* Letter of Recommendation (LOR) Strength ( out of 5 )
* Undergraduate GPA ( out of 10 )
* Research Experience ( either 0 or 1 )
* Chance of Admit ( ranging from 0 to 1 ).

Dataset sources: [here](https://www.kaggle.com/datasets/akshaydattatraykhare/data-for-admission-in-the-university).

## Result

We trained a model for each machine learning methods and found that linear regression outperformed the other models. The results on the test set are shown below:

| Model | R-Squared |
| --- | --- |
| Linear Regression | 0.821 |
| KNN | 0.773 |
| Random Forest | 0.808 |
| Voting Regressor | 0.816 |

As you can see, linear regression achieved the highest R-Squared value of 0.821, indicating that it was able to accurately predict the target variable with a high degree of accuracy. In contrast, the other models had lower R-Squared values, indicating that they were less accurate in their predictions. Also, we have not yet performed hyperparameter tuning in this project, so the results of the models may still be improved through this process.

## Requirements

In order to run the python script, you will need to have the following packages installed:

* matplotlib
* pandas
* scikit-learn

## Disclaimer

This script is provided for educational purposes only, and is not intended to be used for making actual admissions decisions. The predictions made by the script should not be taken as definitive, and should always be considered in conjunction with other factors such as the student's personal statement, letters of recommendation, and the overall admissions criteria of the university.
