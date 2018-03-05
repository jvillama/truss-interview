# Build and run instructions
Install python3 onto your machine if neccessary.

Instructions to install python3 here:
http://docs.python-guide.org/en/latest/starting/install3/osx/

With python3 installed, install pytz from pip:

```pip install pytz```

or from requirements.txt:

```pip install requirements.txt```


Then run:

```python3 csv_cleaner.py <filename>```

For example:

```python3 csv_cleaner.py sample.csv```

Clean CSVs generated are named ```cleaned-<filename>``` and should be cleaned according to specifications.