import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None
pd.options.display.max_rows = None

#file_path = "D:/Trainity/application_data.csv"
file_path = "C:/Users/Agam Computer/OneDrive/Desktop/Bank Loan Case Study/application_data.csv"
app_data = pd.read_csv(file_path)
#print("1")
#pre_app_data = pd.read_csv("D:/Trainity/previous_application.csv")

'''
app_data.shape
print(app_data.shape)
print(pre_app_data.shape)
print(app_data.head())
print(pre_app_data.head())
print(app_data.columns)
print(pre_app_data.columns)
'''


# Application data: Data Cleaning and Replacing

null_data1 = app_data.isnull().sum()/49999*100
#print(null_data1)

threshold = 40
drop_col1 = null_data1[null_data1 > threshold].index

print(drop_col1.size)
app_data_filtered = app_data.drop(columns=drop_col1)
print(app_data.shape)
print(app_data_filtered.shape)
print(app_data_filtered.head())
columns_drop = ['FLAG_MOBIL', 'FLAG_EMP_PHONE', 'FLAG_WORK_PHONE', 'FLAG_CONT_MOBILE', 'FLAG_PHONE',
                   'FLAG_EMAIL', 'FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_3', 'FLAG_DOCUMENT_4', 'FLAG_DOCUMENT_5',
                   'FLAG_DOCUMENT_6', 'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_8', 'FLAG_DOCUMENT_9', 'FLAG_DOCUMENT_10',
                   'FLAG_DOCUMENT_11', 'FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_13', 'FLAG_DOCUMENT_14', 'FLAG_DOCUMENT_15',
                   'FLAG_DOCUMENT_16', 'FLAG_DOCUMENT_17', 'FLAG_DOCUMENT_18', 'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_20',
                   'FLAG_DOCUMENT_21', 'EXT_SOURCE_2', 'EXT_SOURCE_3']

app_data_filtered = app_data_filtered.drop(columns=columns_drop)
print(app_data_filtered.shape)
print(app_data_filtered.head())

columns_convert = ['DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'DAYS_LAST_PHONE_CHANGE']

app_data_filtered[columns_convert] = app_data_filtered[columns_convert].abs()

print(app_data_filtered[columns_convert].describe())

print(app_data_filtered.isnull().sum().sort_values(ascending=True))

print(app_data_filtered['DAYS_LAST_PHONE_CHANGE'].describe())

app_data_filtered['DAYS_LAST_PHONE_CHANGE'].fillna(964, inplace=True)

print(app_data_filtered.isnull().sum().sort_values(ascending=True))


app_data_filtered['CNT_FAM_MEMBERS'].head()

print(app_data_filtered['CNT_FAM_MEMBERS'].describe())

print(app_data_filtered.groupby('CNT_FAM_MEMBERS').size())

app_data_filtered['CNT_FAM_MEMBERS'].fillna(2, inplace=True)

print(app_data_filtered.isnull().sum().sort_values(ascending=True))

print(app_data_filtered['AMT_ANNUITY'].describe())
app_data_filtered['AMT_ANNUITY'].fillna(27107.3, inplace=True)

print(app_data_filtered['AMT_ANNUITY'].isnull().sum())

print(app_data_filtered['AMT_GOODS_PRICE'].describe())

print(app_data_filtered['AMT_GOODS_PRICE'].median())

print(app_data_filtered['AMT_GOODS_PRICE'].mean())

app_data_filtered['AMT_GOODS_PRICE'].fillna(450000.0, inplace=True)

print(app_data_filtered['AMT_GOODS_PRICE'].isnull().sum())


app_data_filtered[['DEF_60_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE', 'OBS_60_CNT_SOCIAL_CIRCLE', 'OBS_30_CNT_SOCIAL_CIRCLE']].describe()

print(app_data_filtered[['DEF_60_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE', 'OBS_60_CNT_SOCIAL_CIRCLE', 'OBS_30_CNT_SOCIAL_CIRCLE']].head())

print(app_data_filtered[['DEF_60_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE', 'OBS_60_CNT_SOCIAL_CIRCLE', 'OBS_30_CNT_SOCIAL_CIRCLE']].median())


app_data_filtered['DEF_60_CNT_SOCIAL_CIRCLE'].fillna(0, inplace=True)
app_data_filtered['DEF_30_CNT_SOCIAL_CIRCLE'].fillna(0, inplace=True)
app_data_filtered['OBS_60_CNT_SOCIAL_CIRCLE'].fillna(1, inplace=True)
app_data_filtered['OBS_30_CNT_SOCIAL_CIRCLE'].fillna(1, inplace=True)


print(app_data_filtered.isnull().sum().sort_values(ascending=True))



print(app_data_filtered['DAYS_LAST_PHONE_CHANGE'].describe())

print(app_data_filtered['CNT_FAM_MEMBERS'].describe())

app_data_filtered['DAYS_LAST_PHONE_CHANGE'].fillna(964, inplace=True)

app_data_filtered['CNT_FAM_MEMBERS'].fillna(2, inplace=True)



print(app_data_filtered.isnull().sum().sort_values(ascending=True))


print(app_data_filtered['NAME_TYPE_SUITE'].head())


print(app_data_filtered.groupby('NAME_TYPE_SUITE').size())

print(app_data_filtered['NAME_TYPE_SUITE'].describe())

app_data_filtered['NAME_TYPE_SUITE'].fillna('Unaccompanied', inplace=True)

print(app_data_filtered['NAME_TYPE_SUITE'].isnull().sum())



app_data_filtered[['AMT_REQ_CREDIT_BUREAU_QRT',
'AMT_REQ_CREDIT_BUREAU_HOUR',
'AMT_REQ_CREDIT_BUREAU_DAY',
'AMT_REQ_CREDIT_BUREAU_WEEK',
'AMT_REQ_CREDIT_BUREAU_MON',
'AMT_REQ_CREDIT_BUREAU_YEAR']].describe()



print(app_data_filtered[['AMT_REQ_CREDIT_BUREAU_QRT',
'AMT_REQ_CREDIT_BUREAU_HOUR',
'AMT_REQ_CREDIT_BUREAU_DAY',
'AMT_REQ_CREDIT_BUREAU_WEEK',
'AMT_REQ_CREDIT_BUREAU_MON',
'AMT_REQ_CREDIT_BUREAU_YEAR']].mode())


print(app_data_filtered[['AMT_REQ_CREDIT_BUREAU_QRT',
'AMT_REQ_CREDIT_BUREAU_HOUR',
'AMT_REQ_CREDIT_BUREAU_DAY',
'AMT_REQ_CREDIT_BUREAU_WEEK',
'AMT_REQ_CREDIT_BUREAU_MON',
'AMT_REQ_CREDIT_BUREAU_YEAR']].head())

app_data_filtered['AMT_REQ_CREDIT_BUREAU_QRT'].fillna(0, inplace=True)
app_data_filtered['AMT_REQ_CREDIT_BUREAU_HOUR'].fillna(0, inplace=True)
app_data_filtered['AMT_REQ_CREDIT_BUREAU_DAY'].fillna(0, inplace=True)
app_data_filtered['AMT_REQ_CREDIT_BUREAU_WEEK'].fillna(0, inplace=True)
app_data_filtered['AMT_REQ_CREDIT_BUREAU_MON'].fillna(0, inplace=True)
app_data_filtered['AMT_REQ_CREDIT_BUREAU_YEAR'].fillna(0, inplace=True)


print(app_data_filtered[['AMT_REQ_CREDIT_BUREAU_QRT',
'AMT_REQ_CREDIT_BUREAU_HOUR',
'AMT_REQ_CREDIT_BUREAU_DAY',
'AMT_REQ_CREDIT_BUREAU_WEEK',
'AMT_REQ_CREDIT_BUREAU_MON',
'AMT_REQ_CREDIT_BUREAU_YEAR']].isnull().sum())


print(app_data_filtered.isnull().sum().sort_values(ascending=True))

(app_data_filtered['OCCUPATION_TYPE'].describe())

print(app_data_filtered.groupby('OCCUPATION_TYPE').size())

app_data_filtered['OCCUPATION_TYPE'].fillna('Laborers', inplace=True)

print(app_data_filtered.isnull().sum().sort_values(ascending=True))


print(app_data_filtered.head(10))
print(app_data_filtered.nunique().sort_values())
print(app_data_filtered.dtypes)

app_data_filtered.to_csv('C:/Users/Agam Computer/OneDrive/Desktop/Bank Loan Case Study/app_data_filtered.csv', index=False)










# Previous Application Data: Data Cleaning and Replacing Missing Values

'''
pre_app_data = pd.read_csv("C:/Users/Agam Computer/OneDrive/Desktop/Bank Loan Case Study/previous_application.csv")

print(pre_app_data.shape)

pre_app_data.head()
print(pre_app_data_filtered.isnull().sum().sort_values(ascending=True))
'''
pre_app_data_filtered = "C:/Users/Agam Computer/OneDrive/Desktop/Bank Loan Case Study/pre_app_data_filtered.csv"


print(app_data_filtered.dtypes)

print("\n\n\n")
'''
print(app_data_filtered.select_dtypes(include=['object']).columns)

print(app_data_filtered.select_dtypes(exclude=['object']).columns)

print(pre_app_data_filtered.select_dtypes(include=['object']).columns)

print(pre_app_data_filtered.select_dtypes(exclude=['object']).columns)


merged_final_data = pd.merge(app_data_filtered,pre_app_data_filtered,how='inner',on='SK_ID_CURR')
merged_final_data.head()

merged_final_data.to_csv('C:/Users/Agam Computer/OneDrive/Desktop/Bank Loan Case Study/merged_final_data.csv', index=False)

'''





class_counts = app_data_filtered['TARGET'].value_counts()
imbalance_ratio = class_counts[0] / class_counts[1]

print("Imbalance Ratio:", imbalance_ratio)



app_data_fil = app_data_filtered['TARGET'].value_counts()
class_counts = app_data_fil
imbalance_ratio = class_counts[0] / class_counts[1]

print("Imbalance Ratio: 1:{:.0f}".format(imbalance_ratio))


app_data_fil = app_data_filtered['TARGET'].value_counts()

total_instances = app_data_fil.sum()

for target, count in app_data_fil.items():
    percentage = (count / total_instances)*100
    print("{} = {:.2f}%".format(target, percentage))


print(app_data_filtered.dtypes.value_counts())



numerical_variables = app_data_filtered.select_dtypes(include = ['float64', 'int64']).columns
numerical_columns = app_data_filtered[numerical_variables]
payment_difficulty = numerical_columns[numerical_columns['TARGET']==1]
all_other = numerical_columns[numerical_columns['TARGET']==0]


print(payment_difficulty.head(10))


correlations_with_target_1 = payment_difficulty.corr()
top_10_correlations_with_target_1 = correlations_with_target_1.unstack().sort_values(ascending=False)
top_10_correlations_with_target_1 = top_10_correlations_with_target_1[top_10_correlations_with_target_1.index.get_level_values(0) != top_10_correlations_with_target_1.index.get_level_values(1)]
top_10_correlations_with_target_1 = top_10_correlations_with_target_1.head(20)


print(top_10_correlations_with_target_1)



correlations_with_target_0 = all_other.corr()
top_10_correlations_with_target_0 = correlations_with_target_0.unstack().sort_values(ascending=False)
top_10_correlations_with_target_0 = top_10_correlations_with_target_0[top_10_correlations_with_target_0.index.get_level_values(0) != top_10_correlations_with_target_0.index.get_level_values(1)]
top_10_correlations_with_target_0 = top_10_correlations_with_target_0.head(20)

print(top_10_correlations_with_target_0)

columns = ['OBS_30_CNT_SOCIAL_CIRCLE',
'OBS_60_CNT_SOCIAL_CIRCLE',
'AMT_CREDIT',
'AMT_GOODS_PRICE',
'REGION_RATING_CLIENT_W_CITY',
'REGION_RATING_CLIENT',
'CNT_CHILDREN',
'CNT_FAM_MEMBERS',
'LIVE_REGION_NOT_WORK_REGION',
'REG_REGION_NOT_WORK_REGION',
'DEF_30_CNT_SOCIAL_CIRCLE',
'DEF_60_CNT_SOCIAL_CIRCLE',
'LIVE_CITY_NOT_WORK_CITY',
'REG_CITY_NOT_WORK_CITY',
'AMT_ANNUITY',
'DAYS_EMPLOYED',
'DAYS_BIRTH']

selected_columns = payment_difficulty[columns]
correlation_matrix = selected_columns.corr()

plt.figure(figsize=(100, 100))
sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', fmt='.3f', linewidths=0.5)
plt.title("Correlation for 'TARGET = 1'")
plt.show()


columns = ['OBS_30_CNT_SOCIAL_CIRCLE',
'OBS_60_CNT_SOCIAL_CIRCLE',
'AMT_CREDIT',
'AMT_GOODS_PRICE',
'REGION_RATING_CLIENT_W_CITY',
'REGION_RATING_CLIENT',
'CNT_CHILDREN',
'CNT_FAM_MEMBERS',
'LIVE_REGION_NOT_WORK_REGION',
'REG_REGION_NOT_WORK_REGION',
'DEF_30_CNT_SOCIAL_CIRCLE',
'DEF_60_CNT_SOCIAL_CIRCLE',
'LIVE_CITY_NOT_WORK_CITY',
'REG_CITY_NOT_WORK_CITY',
'AMT_ANNUITY',
'DAYS_EMPLOYED',
'DAYS_BIRTH']

selected_columns = all_other[columns]
correlation_matrix = selected_columns.corr()

plt.figure(figsize=(100, 100))
sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', fmt='.3f', linewidths=0.5)
sns.set(font_scale=20)
plt.title("Correlation for 'TARGET = 0'")
plt.show()















