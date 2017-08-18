
# coding: utf-8

# ### World Development Indicators

# In[1]:


from collections import OrderedDict
import contextlib
import os
import pandas as pd
import requests
import zipfile


# In[2]:


# 
# http://data.worldbank.org/data-catalog/world-development-indicators
#
# The World Development Indicators are the primary World Bank collection
# of development indicators, compiled from officially-recognized
# international sources.
#
# The World Development Indicators present the most current and accurate
# global development data available, and includes national, regional and
# global estimates.
#


# In[3]:


# Download and extract the WDI files
zfilename = 'WDI_csv.zip'
if not os.path.exists(zfilename):
    wdi_url = 'http://databank.worldbank.org/data/download/' + zfilename
    response = requests.get(wdi_url, timeout=3.333)
    response.raise_for_status()
    with open(zfilename, 'wb') as f:
        # Save the zip file to disk.
        f.write(response.content)
        # Extract all files from the archive
        with zipfile.ZipFile(zfilename) as z:
            z.extractall()


# In[4]:


# Read the full data file into a data frame, dropping empty columns
df = pd.read_csv('WDIData.csv')
df.dropna(how='all', axis=1, inplace=True)


# In[5]:


print(df.columns)


# In[6]:


# Tidy up: Melt all year columns into year and value columns
id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
df = pd.melt(frame=df, id_vars=id_vars, var_name='Year')
df.dropna(inplace=True)


# In[7]:


# Let's peek at what we've got
print(df.head())


# In[8]:


# Split each indicator into a separate data frame and save to CSV
with contextlib.suppress(FileExistsError):
    os.mkdir('output')

filelist = []
os.chdir('output')
for indicator, frame in df.groupby(['Indicator Name', 'Indicator Code']):
    # Replace 'value' with indicator name in header
    frame = frame.rename(columns={'value': indicator[0]})
    frame = frame.drop(labels=['Indicator Name', 'Indicator Code'], axis=1)
    # Use indicator code for file name
    fname = indicator[1] + '.csv'
    # Save to CSV
    frame.to_csv(fname, index=False)
    # Record indicator name and file name for file-list output file
    record = OrderedDict([('Indicator', indicator[0]), ('File', fname)])
    filelist.append(record)

# Save indicator file list to CSV
pd.DataFrame(filelist).to_csv('FileList.csv', index=False)

