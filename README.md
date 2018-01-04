# CSV_Importer
Python utility to parse all values in a CSV file into a dictionary, then filter out purchases that contained multiple items.

### Requirements
Python 3.6 installed and configured in your path

### Use
1. Navigate your CLI to the directory where this script is cloned.

2. Configure the script to point to the CSV file desired (line 11)

3. Run the script

```
python CSV_Importer
```

This will output a dictionary of all values in the configured CSV file that have more than one product_id for each purchase_id.

For example, the default CSV file configured will display:
{'HYGENKPUFQ1589': ['CHD023', 'VRA361']}

## Built With
* Python 3.6

## Author
Brian Payne - [brian.payne2@gmail.com](mailto:brian.payne2@gmail.com)
