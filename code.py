 import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ================================
# 1. Data Collection
# ================================
# Load dataset (make sure the file path is correct)
df = pd.read_excel("dataset.xlsx")

# Quick preview of data
print("\n--- Data Sample ---")
print(df.head())

# Check columns available
print("\nColumns available:", df.columns.tolist())

# ================================
# 2. Data Cleaning
# ================================
# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing values in important columns
df.dropna(subset=["Bedrooms", "Bathrooms", "Floors", "Price"], inplace=True)

# Clean column names (standardize)
df.columns = df.columns.str.strip().str.title()

# Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# ================================
# 3. Exploratory Data Analysis (EDA)
# ================================
# Summary statistics for important columns
print("\n--- Summary Statistics ---")
print(df[["Bedrooms", "Bathrooms", "Floors", "Price"]].describe())

# Visualize distribution of house prices
import matplotlib.pyplot as plt
plt.hist(df['Price'], bins=30, color='skyblue')
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Visualize correlation between features
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

# ================================
# 4. Feature Engineering
# ================================
# Create a new feature: TotalRooms = Bedrooms + Bathrooms
df["TotalRooms"] = df["Bedrooms"] + df["Bathrooms"]

# Check the first few rows to verify new feature
print("\n--- New Feature (TotalRooms) ---")
print(df[['Bedrooms', 'Bathrooms', 'TotalRooms']].head())

# ================================
# 5. Model Building
# ================================
# Features and target variable
X = df[["Bedrooms", "Bathrooms", "Floors", "TotalRooms"]]
y = df["Price"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# ================================
# 6. Model Evaluation
# ================================
# Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"\n--- Model Evaluation ---\nMean Squared Error: {mse:.2f}")

# Additional evaluation metrics can be added here if necessary

# ================================
# 7. User Input and Prediction
# ================================
try:
    # Get user input for house features
    bedrooms = int(input("Enter number of bedrooms: "))
    bathrooms = int(input("Enter number of bathrooms: "))
    floors = int(input("Enter number of floors: "))
    total_rooms = bedrooms + bathrooms  # Calculate TotalRooms

    # Prepare input data for prediction
    input_data = pd.DataFrame([[bedrooms, bathrooms, floors, total_rooms]],
                              columns=["Bedrooms", "Bathrooms", "Floors", "TotalRooms"])

    # Make the prediction
    predicted_price = model.predict(input_data)[0]
    print(f"\n💰 Predicted House Price: ₹{predicted_price:,.2f}")

except ValueError:
    print("⚠️ Please enter valid numbers.")

# ================================
# 8. Deployment (optional)
# ================================
# Optionally deploy this as a Streamlit app:
# 1. Install Streamlit with: pip install streamlit
# 2. Use: st.number_input, st.write, etc., to create interactive inputs
# 3. Run with: streamlit run your_script.py
