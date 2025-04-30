import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ================================================
# 1. Data Collection
# ================================================
df = pd.read_excel("dataset.xlsx")

print("\n--- Data Sample ---")
print(df.head())

print("\nColumns available:", df.columns.tolist())

# ================================================
# 2. Data Cleaning
# ================================================
print("\n--- Missing Values ---")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
df.columns = df.columns.str.strip().str.title()
df.dropna(subset=["Bedrooms", "Bathrooms", "Floors", "Garage", "Condition", "Price"], inplace=True)
df.reset_index(drop=True, inplace=True)

# ================================================
# 3. Exploratory Data Analysis (EDA)
# ================================================
print("\n--- Summary Statistics ---")
print(df[["Bedrooms", "Bathrooms", "Floors"]].describe())

# Plotting histograms and correlation
plt.hist(df['Bedrooms'], bins=10, color='lightgreen')
plt.title('Distribution of Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Frequency')
plt.show()

sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

# ================================================
# 4. Feature Engineering
# ================================================
df["TotalRooms"] = df["Bedrooms"] + df["Bathrooms"]
print("\n--- New Feature (TotalRooms) ---")
print(df[["Bedrooms", "Bathrooms", "TotalRooms"]].head())

# ================================================
# 5. Model Building (Linear Regression)
# ================================================
# Define features and target variable
features = ["Bedrooms", "Bathrooms", "Floors", "Garage", "Condition", "TotalRooms"]
X = pd.get_dummies(df[features], drop_first=True)  # One-hot encoding for categorical variables
y = df["Price"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# ================================================
# 6. Model Evaluation
# ================================================
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared: {r2}")

# ================================================
# 7. User Input and Price Prediction
# ================================================
try:
    bedrooms = int(input("Enter number of bedrooms: "))
    bathrooms = int(input("Enter number of bathrooms: "))
    floors = int(input("Enter number of floors: "))
    garage = int(input("Enter number of garages: "))
    condition = input("Enter house condition (e.g., Excellent, Good, Fair): ").strip().title()

    input_data = pd.DataFrame({
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Floors": [floors],
        "Garage": [garage],
        "Condition": [condition],
        "TotalRooms": [bedrooms + bathrooms]
    })

    # Preprocessing input data
    input_data = pd.get_dummies(input_data, drop_first=True)
    # Align input data columns with model training data
    input_data = input_data.reindex(columns=X.columns, fill_value=0)

    predicted_price = model.predict(input_data)
    print(f"Predicted House Price: ${predicted_price[0]:,.2f}")

except ValueError:
    print("⚠️ Please enter valid numeric values.")
