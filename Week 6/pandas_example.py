import pandas as pd

cars = {
    "Name":["toyota" ,"BMW", "Ford"],
    "Model":["corolla", "civic", "Mustang"],
    "Year":["2020", "2019", "2021"]
}

df =pd.DataFrame(cars)
print(df)

# more example
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

df  = pd.DataFrame(data)
# print("DataFrame:\n", df)

# print("Names:", df['Age'])
# print(df[df['Score'] >= 90])