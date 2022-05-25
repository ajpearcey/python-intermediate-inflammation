import numpy as np

def attach_names(data, names):
    """Create datastructure containing patient records."""
    output = []

    for i in range(len(data)):
        output.append({'name': names[i],
                       'data': data[i]})

    return output

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

output = attach_names(data, ['Alice', 'Bob'])
print(output)