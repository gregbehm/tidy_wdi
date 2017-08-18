# Tidy the World Development Indicators data file

The World Development Indicators are the primary World Bank collection
of development indicators, compiled from officially-recognized
international sources. These data sets present the most current and accurate
global development data available, and includes national, regional and
global estimates.

More information about the WDI is available at:  
http://data.worldbank.org/data-catalog/world-development-indicators

## Messy dataset

The World Development Indicators (WDI) data file available for download is
a zipped archive in Excel and CSV format. The CSV archive contains several
meta-data files and the full data file, WDIData.csv. The Excel archive
contains one file, WDIEXCEL.xlsx, with sheets corresponding to the same
meta-data and data tables mentioned above.

*The WDI data table is messy, containing data for all 1500+ indicators,
as well as data spanning multiple observations (years) in each row.* 

## Tidy the data

The purpose of this project is to tidy WDI, splitting each observation
(country + year + measure) into a separate data row, and then saving
each indicator data set to its own CSV output file for further analysis.



