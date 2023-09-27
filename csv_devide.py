import pandas as pd
from sklearn.model_selection import train_test_split

# Read the CSV file
df = pd.read_csv('/home/suger01/Desktop/CDCN_suger/train_files.csv')

# Shuffle the data and split it into training and testing parts (80% training, 20% testing)
train_df, test_df = train_test_split(df, test_size=0.2, shuffle=True)

# Save the training part to a new CSV file
train_df.to_csv('./train.csv', index=False)

# Save the testing part to a new CSV file
test_df.to_csv('./test.csv', index=False)

#Epoch: 97, iter: 419384, loss: 404.0394177614532, acc: 0.793443600490967
