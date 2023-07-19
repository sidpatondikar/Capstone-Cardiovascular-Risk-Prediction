# Capstone-Cardiovascular-Risk-Prediction

Project Summary:

The project aimed to predict the 10-year risk of future coronary heart disease (CHD) in patients using a dataset from an ongoing cardiovascular study in Framingham, Massachusetts. With over 4,000 records and 15 attributes, five classification machine learning models were constructed for this task.

The data preprocessing stage involved handling missing values by imputing mode values for categorical columns and using median/KNN imputer values for continuous columns. Feature engineering and selection techniques were applied, addressing multicollinearity, skewness, outliers, and class imbalance using SMOTE.

Given the critical nature of medical data, where false negatives are of high concern, recall was chosen as the primary evaluation metric. Detecting individuals at risk is crucial, as it can lead to life-saving interventions.

The model building process started with simple models like Linear Regression and SVM. Later, more complex tree-based and ensemble models were employed. Ultimately, a hyperparameter-tuned random forest model was selected as the final model due to its exceptional performance on the test data, achieving a recall score of 1. This means that all 100 possible high-risk patients were successfully classified, highlighting the model's life-saving potential in critical conditions.

Upon analyzing feature importance, age emerged as the most crucial feature in the model, followed by pulse pressure and heart rate. Conversely, BPMeds and had_stroke turned out to be the least influential features in predicting CHD risk.

In conclusion, the project successfully developed a predictive model for identifying high-risk patients susceptible to coronary heart disease. By employing a well-tuned random forest model and focusing on essential features like age, pulse pressure, and heart rate, the model demonstrated a recall of 1, ensuring the identification of all at-risk individuals. This implementation holds the potential to save lives by enabling timely interventions and medical care for those in need.
