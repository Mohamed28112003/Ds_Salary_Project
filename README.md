# Data Science Salary Estimator: Project Overview
- Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
- Scraped over 1000 job descriptions from glassdoor using python and selenium
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
- Optimized Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
# Model performance
- Random Forest : MAE = 11.22
- Ridge Regression: MAE = 19.67
