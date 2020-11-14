# %%
# setting SparkContext for pyspark
from pyspark import SparkContext
sc = SparkContext("local", "Simple App")

# %% 
# Read in README.md
lines = sc.textFile("README.md")

# %%
# Return First Line
lines.first()

# %%
# Return first 5 lines
lines.take(5)

# %%
