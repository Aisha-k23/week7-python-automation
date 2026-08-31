import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("titanic.txt")

# Calculate total passengers
total_passengers = len(df)

# Calculate average fare
average_fare = df["Fare"].mean()

# Calculate female survival rate
female_rate = df[df["Sex"] == "female"]["Survived"].mean() * 100

# Calculate male survival rate
male_rate = df[df["Sex"] == "male"]["Survived"].mean() * 100

# Print the dataset summary
print("\nTitanic Dataset Summary")
print("=" * 30)
print(f"Total Passengers: {total_passengers}")
print(f"Average Fare: £{average_fare:.2f}")
print(f"Female Survival Rate: {female_rate:.1f}%")
print(f"Male Survival Rate: {male_rate:.1f}%")