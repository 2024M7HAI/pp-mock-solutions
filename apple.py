import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# --- Task 1: Correctly load the apple dataset into a DataFrame
label_encoder = LabelEncoder()
file_path = 'data/apple_quality.csv'
apple_data = pd.read_csv(file_path)
# Quality is the target variable and it's categorical
apple_data['Quality'] = label_encoder.fit_transform(apple_data['Quality'].astype(str))

# --- Task 2: Preprocess the data
# Note: We restrict ourselves to dropping incomplete rows and duplicate rows here
# In particular, since we're building a Random Forest Feature Scaling is not necessary
apple_data_cleaned = apple_data.dropna()
apple_data_cleaned = apple_data_cleaned.drop_duplicates()

# --- Task 3: Generate summary statistics
# Calculating the mean, median, and standard deviation for only the numeric columns in the dataset
mean_values = apple_data.mean(numeric_only=True)
median_values = apple_data.median(numeric_only=True)
std_dev_values = apple_data.std(numeric_only=True)

# --- Task 4: Create a basic histogram for, e.g., the 'Sweetness' feature
plt.figure(figsize=(8, 6))
apple_data['Sweetness'].hist(bins=10)
plt.title('Distribution of Sweetness in Apples')
plt.xlabel('Sweetness')
plt.ylabel('Frequency')
plt.show()
# Saving to file so we can submit it to the exam upload
histogram_file_path = 'data/sweetness_distribution_histogram.png'
plt.savefig(histogram_file_path)


# --- Task 5: Split data into training and testing set with ratio 80-20
# Define the feature data X and the target variable y, where 'Quality' is the column to predict
X = apple_data.drop('Quality', axis=1)
y = apple_data['Quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X_train.drop('Acidity', axis=1)
X_test = X_test.drop('Acidity', axis=1)

# --- Task 6: Train ar Random Forest Classifier
# To make an informed choice about hyperparameters we use GridSearchCV;
# To get full score the detailed grid don't matter too much; We just want to see that you're aware of this
param_grid = {
    'n_estimators': [10, 20],           # Number of trees in the random forest
    'max_depth': [None, 10, 20],        # Maximum depth of the tree
    'min_samples_split': [2, 5],        # Minimum number of samples required to split a node
    'min_samples_leaf': [1, 2]          # Minimum number of samples required at each leaf node
}

# Create a base classifier
random_forest = RandomForestClassifier(random_state=42)
# Instantiate the grid search model
grid_search = GridSearchCV(estimator=random_forest, param_grid=param_grid, n_jobs=1)
# Fit the grid search to the data
grid_search.fit(X_train, y_train)
# The best parameters found by GridSearchCV
best_params = grid_search.best_params_

# Create a new RandomForestClassifier with the best parameters
# We use ** to unpack the dictionary into the classifier's parameters
optimized_random_forest = RandomForestClassifier(**best_params, random_state=42)
# Train the optimized model on the training data
optimized_random_forest.fit(X_train, y_train)

# --- Task 7: Calculating accuracy and generating confusion matrix
y_pred = optimized_random_forest.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print results
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)