from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

url = "2021 Notifiable Diseases.csv"
names = ['Period', 'Giardiasis', 'Invasive pneumococcal', 'Measles', 'Mumps','Pertussis','Salmonellosis','Tuberculosis']
dataset = read_csv(url, names=names)


# shape
print(dataset.shape)
# head
print(dataset.head(20))
# descriptions
print(dataset.describe())
# class distribution
print(dataset.groupby('Period').size())

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()
# histograms
dataset.hist()
pyplot.show()
# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()
