import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv(r"C:\Users\mohamed22\Downloads\glassdoor_jobs.csv")



# salary



df=df[df['Salary Estimate']!='-1'] # reomve -1 salaries
salary=df['Salary Estimate'].apply(lambda x:x.split('(')[0]) # reomve text from salary
salary=salary.apply(lambda x:x.replace("$",'').replace('K','')) # replace k and $
df['Salary_Per_Hour'] = salary.apply(lambda x: 1 if "per hour" in x.lower() else 0)
df['Employer Provdid '] = salary.apply(lambda x: 1 if "employer provided salary" in x.lower() else 0)

salary=salary.apply(lambda x:x.replace('Employer Provided Salary:','').replace('Per Hour',''))
df['Min_Salary']=salary.apply(lambda x:x.split('-')[0])
df['Max_Salary']=salary.apply(lambda x:x.split('-')[1])
df['Avg_Salary']=(df['Max_Salary'].astype(int)+df['Min_Salary'].astype(int))/2


#company name
df["Company_name_txt"] = df['Company Name'].apply(lambda x:x.split('\n')[0])

#jop_estate
df["Jop_Estate"]=df['Location'].apply(lambda x:x.split(',')[1])


# see if location of the headquarters in the same location
df['Same_Location'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#company age
df['Company_Age']=df['Founded'].apply(lambda x : x if x<0 else 2023-x)
#jop_des

#python
df['Python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0 )

#r studio
df['R_studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#spark
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['Aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)



df_out = df.drop(['Unnamed: 0'], axis =1)

df_out.to_csv('data_cleaned.csv',index = False)
df2= pd.read_csv('data_cleaned.csv')
