import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def load_data(filepath):
    df = pd.read_csv(filepath, sep=';')

    # Convert target
    df['y'] = df['y'].map({'yes': 1, 'no': 0})

    return df


def create_preprocessor(df):

    X = df.drop("y", axis=1)

    categorical_cols = X.select_dtypes(include=['object']).columns
    numerical_cols = X.select_dtypes(exclude=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
        ]
    )

    return preprocessor

# Load dataset
df = load_data("../../data/bank_marketing.csv")

X = df.drop("y", axis=1)
y = df["y"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create preprocessor
preprocessor = create_preprocessor(df)

# 🔥 Professional ML Pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(
        class_weight='balanced',
        max_iter=1000
    ))
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
preds = pipeline.predict(X_test)
print(classification_report(y_test, preds))

# Save full pipeline (IMPORTANT)
joblib.dump(pipeline, "../models/lead_model.pkl")

print("Professional ML pipeline trained and saved.")
