
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Loading and Structuring the DataSet
df = pd.read_csv("Datasets\Pandas_Dataset.csv")

# Data Shape
print("*******************************DATA SHAPE*******************************")
print(f"Rows: {df.shape[0]} \nColumns: {df.shape[1]}")


print("\n")


# Data Types and Info
print(print("*******************************DATA TYPES AND INFO*******************************"))
print(df.info())


print("\n")


# Data Summary
print("*******************************DATA SUMMARY*******************************")
print(df.describe())


print("\n")


# Checking for Duplicates and removing them
print("*******************************DATA CLEANING - CHECKING FOR DUPLICATE*******************************")

duplicate_count = df.duplicated().sum()
print(f"Duplicated Rows: {duplicate_count}")

if (duplicate_count > 0):

    df = df.drop_duplicates().reset_index(drop=True)

# duplicate_count = df.duplicated().sum()
# print(f"Duplicated Rows: {duplicate_count}")


print("\n")


# Checking for NULL Values
print("*******************************DATA CLEANING - CHECKING FOR NULL VALUES*******************************")
print(df.isnull().sum())

# Option - 1: Remove the Null Rows
if df["Gen"].isnull().any():

    df = df.dropna(subset=["Gen"])


if df["Age"].isnull().any():

    df = df.dropna(subset=["Age"])


if df["AnnualIncome"].isnull().any():

    df = df.dropna(subset=["AnnualIncome"])


if df["Spending Score"].isnull().any():

    df = df.dropna(subset=["Spending Score"])


# Option - 2: Fill the NULL Rows with median
if df["CustomerID"].isnull().any():

    df["CustomerID"] = df["CustomerID"].fillna(df["CustomerID"].median())

# print(df.isnull().sum())


print("\n")


# Filtering and Outlier Detection
print("*******************************DATA CLEANING - CHECKING FOR NULL VALUES*******************************")

print("Outliers has been Generated")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(data=df, y="AnnualIncome", color="skyblue")
plt.title("Annual Income Outliers")

plt.subplot(1, 2, 2)
sns.boxplot(data=df, y="Spending Score", color="limegreen")
plt.title("Spending Score Outliers")
plt.tight_layout()
plt.show()


print("\n")


# Filtering out the extreme outliers using the InterQuartile Range (IQR) Method
print("*******************************DATA FILTERING*******************************")
Q1 = df["AnnualIncome"].quantile(0.25)
Q3 = df["AnnualIncome"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtering the Dataframe
df_filtered = df[(df["AnnualIncome"] >= lower_bound) & (df["AnnualIncome"] <= upper_bound)]
print(f"\nFiltered out {df.shape[0] - df_filtered.shape[0]} outlier rows based on Annual Income")


print("\n")


# Visual EDA
print("*******************************VISUAL EDA*******************************")

print("Correlation Matrix Generated")

# Correlation Heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(df_filtered.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

print("Scatter Plot Generated")

# Scatter Plot
plt.figure(figsize=(7, 7))
sns.scatterplot(data=df_filtered, x="AnnualIncome", y="Spending Score")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Scatter Plot")
plt.show()


print("\n")


# Model Training and Evaluation
print("*******************************MODEL TRAINING AND EVALUATION*******************************")

# Seperating features and Target
X = df_filtered[["AnnualIncome"]]
Y = df_filtered["Spending Score"]

# Splitting the Data (80% Training, 20% Testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Training the Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict
Y_pred = model.predict(X_test)


print("\n")


# Metrics
print("*******************************FINAL MODEL PERFORMANCE*******************************")
print(f"R-squared Score (R²): {r2_score(Y_test, Y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(Y_test, Y_pred)):.2f}")


print("\n")


# Metrics
print("*******************************PLOTTING THE BEST FIT LINE*******************************")

print("Best fit line plot generated")

plt.figure(figsize=(12, 6))

# Scatter Plot of the Actual Data (Annual Income Vs Actual Spending Score)
sns.scatterplot(x=X_test["AnnualIncome"], y=Y_test, color="green", alpha=0.7 )

# Line Plot of the Prediction (Annual Income Vs Predicted Spending Score)

# Sorting the axis points
sorted_axis = X_test["AnnualIncome"].argsort()

plt.plot(X_test["AnnualIncome"].iloc[sorted_axis], Y_pred[sorted_axis], color="red", linewidth=3, label="Best-Fit Line")

plt.title("Linear Regression")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()