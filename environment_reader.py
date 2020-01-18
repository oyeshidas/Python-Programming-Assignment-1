import matplotlib.pyplot as plt
import csv
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    # Lines here happen before any data is processed
    environment = []
    for row in reader:
        rowlist = []
        # Lines here happen before each row is processed
        for value in row:
            rowlist.append(value)
            # do something with values.
        # Lines here happen before after row is processed
        environment.append(rowlist)
    # Lines here happen after all the data is processed

plt.imshow(environment)
plt.show()    





