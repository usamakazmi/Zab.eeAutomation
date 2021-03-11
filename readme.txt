1)TO run individual files use the following command
pytest -q FILENAME.py

ie.
pytest -q test_example2.py

2)TO RUN ALL TEST CASES WITH at the same time
#This command runs all test_XYZ.py files but only 2 at the same time,
by changing -n=? you can increase number of testcases at a time,
however increasing this value too much can result in failed test cases,
reason for this is net performance or pc performance.

pytest -s -v -n=2

3)config.json file contains name of browser and wait duration
