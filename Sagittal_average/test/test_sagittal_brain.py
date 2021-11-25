import numpy as np

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

expected_data_output = np.zeros(20)
expected_data_output[-1] = 1

output_data = np.loadtxt("brain_average.csv",dtype= np.float, delimiter=',' )

print(np.array_equal(output_data,expected_data_output))
