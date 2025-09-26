Here is an exploration on the CORD data sample containing details about COVID research.

First, a data sample is obtained from the whole file by running extract_sample.py to get the number of rows required.
  // python extract_sample.py

After running this file, a new dataset called cord_sample is created. It contains a contracted sample of the larger dataset.

Next, run stlfriendly.py to run and visualize statistics.
The script loads the dataset as a datafram using pandas, then uses matplotlib, seaborn and streamlit to display findings.
    The information shown includes:
        a. Basic statistics about the columns.
        b. Column data types
        c. Top 10 rows of the dataset
        d. Total number of empty cells per column 
        e. Total number of duplicated records in the dataframe.
    
    To clean the data, :
        a. Date columns are converted to the datetime datatype
        b. Totally empty columns are dropped.
        c. Duplicated records are dropped.
        Records lacking crucial credentials like the id(cord_uid), password hash(sha) and publishing dates(publish_time) are dropped as they may lack authenticity.

    Further filtering and exploratory analysis is performed. Such include:
        a. Counting the number of lines in a file.
            Here, values of the url column are extracted, one by one. The requests library is used to access the webfiles and a for loop run through to count the lines. The findings are stored in a new column named "line_count".
        b. Arranging journals by the amount of lines, from top to bottom.
        c. Getting the number of publications per year
        d. Finding journals producing the most research.
        e. Finding the most used word in titles
        f. Finding the number of papers produced per source.

    Visualization of the data extracted above.