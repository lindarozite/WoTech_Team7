#Task 1: Create a bar chart that shows the count of transactions for each unique value in the 'Gender' column (including NaN values). easy

#version1
df5 = dataset["Gender"].value_counts(dropna = False).reset_index()
df5["Gender"] = df5["Gender"].astype(str)
plt.bar(df5["Gender"], df5["count"], color="blue")
plt.title("Transactions by Gender")
plt.xlabel("Gender")
plt.ylabel("Transasctions")

#version2
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/content/transaction_dataset.csv')

gender_counts = data['Gender'].value_counts(dropna=False)

gender_counts.index = gender_counts.index.fillna('NaN')

plt.bar(gender_counts.index, gender_counts.values, color='skyblue')
plt.xlabel('Gender')
plt.ylabel('Transactions')
plt.title('Count of transactions by gender')
plt.show()

#Task 2: Create a horizontal bar chart that shows the top 5 most frequent names in the DataFrame, based on the 'name' column. (First, create a grouped DataFrame (name_df), then filter it using iloc, and finally create the visualization.) -medium

#version1
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('/content/transaction_dataset.csv')
df6 = dataset["Name"].value_counts().head().reset_index()
plt.barh(df6['Name'], df6['count'], color='orange')
plt.title("Most frequent names")
plt.xlabel('Count')
plt.ylabel('Name')

#version2
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/transaction_dataset.csv')

name_df = df['Name'].value_counts()
name_top5 = name_df.head(5)

plt.barh(name_top5.index, name_top5.values, color='skyblue')

plt.xlabel('Count')
plt.ylabel('Name')
plt.title('Top 5 Names by Count')

plt.show()

#Task 3: Create a filtered DataFrame that includes Category == 'Clothing' and Gender == 'M'. How many rows are there in this filtered DataFrame? Format the result as follows: The filtered DataFrame has XXXX rows. - hard 
#version1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/transaction_dataset.csv')
filtered_df = df[(df['Gender'] == 'M') & (df['Category'] == "Clothing")]
num_rows = filtered_df.shape[0]
print(f"The filtered DataFrame has {num_rows} rows")

#version2
import pandas as pd

df = pd.read_csv('/content/transaction_dataset.csv')

filtered_df = df[(df['Gender'] == 'M') & (df['Category'] == 'Clothing')]

num_rows_filtered = len(filtered_df)
print(f"The filtered data frame has {num_rows_filtered} rows.")
