 ![image](https://github.com/sidpatondikar/Capstone-Cardiovascular-Risk-Prediction/assets/83869822/46d95566-7e76-454e-95d5-86ed83b87d53) 
 # Capstone-Cardiovascular-Risk-Prediction
----------------------------------------------------------------
 Project Completion Certificate : https://certificates.almabetter.com/en/verify/42254995213647
 
----------------------------------------------------------------

## Project Summary:
------------------------------------------------------------
The project aimed to predict the 10-year risk of future coronary heart disease (CHD) in patients using a dataset from an ongoing cardiovascular study in Framingham, Massachusetts. With over 4,000 records and 15 attributes, five classification machine learning models were constructed for this task.


### Variables:
- **Demographic**:

   - Sex: male or female ("M" or "F")
   - Age: Age of the patient (Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
   - Education: The level of education of the patient (categorical values - 1,2,3,4)

- **Behavioral**:

  - is_smoking: whether or not the patient is a current smoker ("YES" or "NO")
  - Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)

- **Medical (history)**:

  - BP Meds: whether or not the patient was on blood pressure medication (Nominal)
  - Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)
  - Prevalent Hyp: whether or not the patient was hypertensive (Nominal)
  - Diabetes: whether or not the patient had diabetes (Nominal)

- **Medical (current)**:

  - Tot Chol: total cholesterol level (Continuous)
  - Sys BP: systolic blood pressure (Continuous)
  - Dia BP: diastolic blood pressure (Continuous)
  - BMI: Body Mass Index (Continuous)
  - Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
  - Glucose: glucose level (Continuous)

 ----------------------------------------------------
 ### Exploratory Data Analysis:

 #### Key Insights:
 
- Categorical Features:
  - There is a class imbalance in target variable 'TenYearCHD' which needs to be dealt with before building the models.
  - Mostly level 1 education patients are prone to coronary heart diseases (CHD).
  - There are more female patients in the dataset. However, the number of male patient at risk of getting CHD is higher than the female patients.
  - There are equal proportion of smokers and non-smokers in dataset, the proption of smokers and non-smokers at risk are also very similar.
  - Very few patients are on blood pressure medications, and the number of risky patients taking BP meds are negligible.
  - Most risky patients do not have diabetes.

- Continuos Features:
  - Most of the continuos variable columns are positively skewed. We will have to deal with skewness in data transformation.
  - Most number of risky patient are between the age of 51 and 63.
  - Most of the patients who are also smokers have less than 5 cigarettes per day.
  - For risky patients: Systolic BP is between 120 and 150, whereas, Diastolic BP is between 75 and 85.
  - Mostly risky patients have BMI between 24-26.
  - Mostly risky patients have heart rate between 70 and 80.
  - Mostly risky patient have glucose between 50 and 100.

--------------------------------------------------------------

### Feature Engineering:

#### Key Insights and Changes:

- There are few independent variables which have high correlation with each other. To deal with multicollinearity,
  - 'is_smoking' column is dropped and only cigsPerDay is kept.
  - To deal with 'Systolic BP' and 'Diastolic BP' column, a new feature called 'pulse_pressure' is created.

    [ Pulse Pressure = Systolic BP - Diastolic BP ]  [Reference Link](https://my.clevelandclinic.org/health/symptoms/21629-pulse-pressure)

  - Skewness in continuos variables is dealt with taking log transform (np.log1p)
  - To deal with outliers, only outliers in the range of +- 3 S.D. are kept and rest are removed.
  - The target variable TenYearCHD is imbalanced. As true values are less, to handle imbalance we will need to perform oversampling. Hence, oversampling technique SMOTE is used.
  - Data is then split into train and test followed by scaling using Normalization (MinMaxScaler).

--------------------------------------------------------------------

### ML Model Implementation:

- 5 Classifcation ML Models to predict risk of coronary heart disease amongst patients. These include:
  - Logistic Regression
  - SVM
  - Decision Tree
  - Random Forest
  - XGBoost

- K-fold cross validation and hyperparmeter tuning is done using GridSearchCV, to reduce overfitting and improve model performance.
- Recall was chosen as the best evaluation metric as we are working with medical data, where false negatives are of high concern. When we fail to detect people at risk of getting a disease, that can lead to loss in life and is thus highly dangerous.
  ![image](https://github.com/sidpatondikar/Capstone-Cardiovascular-Risk-Prediction/assets/83869822/d8054cf5-4583-4bfa-b143-6ea007d013b5)

- Here are the result comparision of all 5 models:
 ![image](https://github.com/sidpatondikar/Capstone-Cardiovascular-Risk-Prediction/assets/83869822/80354f79-c940-4df6-8b2d-d69119952b1f)

Hyperparmeter tuned Random Forest model gives the best recall score on test data, hence, this model is chosen as final predition model.

Confusion Matrix for final model:

![image](https://github.com/sidpatondikar/Capstone-Cardiovascular-Risk-Prediction/assets/83869822/3bf0d986-46e5-45ce-9db2-2f2d62b0691c)

### Feature Importance:

![image](https://github.com/sidpatondikar/Capstone-Cardiovascular-Risk-Prediction/assets/83869822/85a95dbb-16ba-4b85-86d9-43df2711c62f)

Age came out to be the most important feature in our model followed by pulse pressure and heart rate. On the other hand, BPMeds and had_stroke were the least import features.

------------------------------------------------------------

### Conclusion:

- In this project we built 5 Classifcation ML Models to predict risk of coronary heart disease amongst patients.
- To build these models:
   - Missing values were handled by imputing mode values for categorical column and median/KNN Imputer values for continuous columns.
   - Feature engineering and feature selection was performed that included handling multicollinearity, reducing skewness, handling outliers and class imbalance in data was handled using SMOTE.
   - Recall was chosen as the best evaluation metric as we are working with medical data, where false negatives are of high concern. When we fail to detect people at risk of getting a disease, that can lead to loss in life and is thus highly dangerous.

- Initially simple models like Logistic Regression and SVM were used and later on more complex tree based and ensemble models were used.

- Final model chosen was hyperparamter tuned random forest model, which gave a recall of 1 on test data. This means that out of 100 possible high risk patients, we were able to classify all 100 succesfully. This high accuracy is beneficial in saving lives in critical conditions.

- Age came out to be the most important feature in our model followed by pulse pressure and heart rate. On the other hand, BPMeds and had_stroke were the least import features in predicting CHD risk.

