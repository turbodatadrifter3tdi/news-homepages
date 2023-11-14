import pandas as pd
import sys
sys.path.append('/Users/svetlin.ivanov/Documents/ftrepos/news-homepages/newshomepages')
from screenshot import screenshot
from .. import utils
# Read the CSV file
df = pd.read_csv('/Users/svetlin.ivanov/Documents/ftrepos/news-homepages/newshomepages/sources/sites.csv')

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Call the screenshot function for each handle
    screenshot.cli([row['twitter']])
