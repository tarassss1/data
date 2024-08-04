import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("StudentsPerformance.csv")

# гістограма 
df['назва_стовпця'].plot(kind = 'hist')
df[df['назва_стовпця'] == 'значення_стовпця']['стовпець'].plot(kind = 'hist')


# діаграма розміювання
df.plot(x = 'Стовпець1', y = 'Стовпець2', kind = 'scatter')

# кругова діаграма
df['назва_стовпця'].value_counts().plot(kind = 'pie')

# стовпчаста діаграма
df['назва_стовпця'].value_counts().plot(kind = 'bar')
df['назва_стовпця'].value_counts().plot(kind = 'barh', figsize = (8, 5), grid = True)


d1 = df[df['назва_стовпця'] == 'значення_стовпця'].groupby('назва_стовпця')['назва_стовпця'].mean()
d2 = df[df['назва_стовпця'] == 'значення_стовпця'].groupby('назва_стовпця')['назва_стовпця'].mean()
d1.plot(kind = 'barh')
d2.plot(kind = 'barh')


# ящик з вусами
df[df['назва_стовпця'] == 'значення_стовпця']['назва_стовпця'].plot(kind = 'box')

plt.show()
