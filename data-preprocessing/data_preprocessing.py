# Data Processing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

working_dir = "./data/"
data_file   = "Data.csv"
data_file_path = f"{working_dir}{data_file}"
data_set = pd.read_csv('./data/Data.csv')
x = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 3].values

# from sklearn.impute import SimpleImputer as Imputer
# imputer = Imputer(missing_values = np.nan, strategy = 'mean')
# imputer = imputer.fit(x[:, 1:3])
# x[:, 1:3] = imputer.transform(x[:, 1:3])

# from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
# label_encoder_x = LabelEncoder()
# x[:, 0] = label_encoder_x.fit_transform(x[:, 0])
#
# one_hot_encoder = OneHotEncoder(categorical_features = [0])
# x = one_hot_encoder.fit_transform(x).toarray()
#
# label_encoder_y = LabelEncoder()
# y = label_encoder_y.fit_transform(y)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


# sc_x = StandardScaler()
# x_train = sc_x.fit_transform(x_train)
# x_test = sc_x.transform(x_test)