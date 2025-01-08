import joblib
import pandas as pd
import argparse

# Load your encoder and model
loaded_model = joblib.load('C:/salman/ML/Calories Burnt Prediction/model.joblib')

def preprocess_input(data):
    # Assuming 'Item_Fat_Content' needs replacement, as per your previous code
    data_encoded=data.replace({"Gender":{'male':0,'female':1}})

    return pd.DataFrame(data_encoded)

def predict_price(args):
    # Create a DataFrame from the input data
    input_data = pd.DataFrame([(args.Gender, args.Age, args.Height, args.Weight, args.Duration, args.Heart_Rate, args.Body_Temp)],
                               columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])

    # Preprocess the input data
    preprocessed_input = preprocess_input(input_data)

    # Make predictions
    pred = loaded_model.predict(preprocessed_input)[0]
    return pred

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='burn predicition')
    parser.add_argument('--Gender', type=str, required=True, help='Gender')
    parser.add_argument('--Age', type=float, required=True, help='Age')
    parser.add_argument('--Height', type=float, required=True, help='Height')
    parser.add_argument('--Weight', type=float, required=True, help='Weight')
    parser.add_argument('--Duration', type=float, required=True, help='Duration')
    parser.add_argument('--Heart_Rate', type=float, required=True, help='Heart Rate')
    parser.add_argument('--Body_Temp', type=float, required=True, help='Body Temperature')

    args = parser.parse_args()

    # Call the predict_price function with the parsed arguments
    prediction = predict_price(args)
    print(f"Predicted value: {prediction}")
