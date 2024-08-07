def my_test_function():
	print("I'm working as exptected")

def scaling_data(data):
	from sklearn.preprocessing import StandardScaler
	scaler = StandardScaler()
	scaled_data = scaler.fit_transform(data)

	return scaled_data


