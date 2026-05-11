import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']


# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Create a 'FamilySize' column
data['FamilySize'] = data['SibSp'] + data['Parch']

#Create an 'IsAlone' column
data['IsAlone'] = (data['FamilySize'] == 0).astype(int)

#Convert  the 'Sex' column to numeric values
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# One-hot encode the 'Embarked' column, dropping the firest category
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Get the mean age of passengers
mean_age = data['Age'].mean()

# Get the median fare of passengers
median_fare = data['Fare'].median()

# Get the number of passengers by class
passengers_by_class = data['Pclass'].value_counts()

# Get the number of passengers by gender
passengers_by_gender = data['Sex'].value_counts()

# Get the number of passengers by survival status
passengers_by_survival = data['Survived'].value_counts()

# Calculate the survival rate of passenegers
survival_rate = data['Survived'].mean()

# Calculate the survival rate by gender
survival_rate_by_gender = data.groupby('Sex')['Survived'].mean()

# Output the results
print(mean_age)
print(median_fare)
print(passengers_by_class)
print(passengers_by_gender)
print(passengers_by_survival)
print(survival_rate)
print(survival_rate_by_gender)