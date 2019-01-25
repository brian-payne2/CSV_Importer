# CSV_Importer
Python utility to parse all values in a CSV file into a dictionary, then filter out purchases that contained multiple items.

### Requirements
Python 3.6 installed and configured in your path

### Use
1. Navigate your CLI to the directory where this script is cloned.

2. Run the script, passing in the name of the CSV file

```
python CSV_Importer csv_file_name.csv
```

This will output a dictionary of all values in the configured CSV file that have more than one product_id for each purchase_id.

For example, the default CSV file configured will display:
{'HYGENKPUFQ1589': ['CHD023', 'VRA361']}

## Built With
* Python 3.6

## Author
Brian Payne - [brian.payne2@gmail.com](mailto:brian.payne2@gmail.com)
