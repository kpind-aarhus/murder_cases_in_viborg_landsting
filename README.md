# murder_cases_in_viborg_landsting
A Python based scraper that handles HTML files of Nørgaard-Pedersen's summaries in Viborg Landsting 1569-1666, converts them to JSON and then extracts possible murder cases.\
The HTML documents can be found at the website http://www.dragtilminde.dk/SLHISTORIE.html. \
##HTML to JSON
The HTML to JSON script is specialised in handling the summaries of "Dombøger" from Viborg Landsting and should not be used for other purposes.\
It iterates through each HTML document for dates, the special case numbers based on Nørgaard-Pedersen's system, and the summaries of each case description and creates a dictionary that is then converted to JSON.\
After downloading the HTML files, they have been manipulated to avoid too many exceptions in an already fairly unstructured document. This ensures that there will always be some sort of date that the case numbers can relate to, and that these dates are unique to each protocol.\
The JSON files also needed some manipulation to avoid empty case numbers in the first case after each date change. The uploaded JSON files are not the raw output from the HTML to JSON script.

##Case extractor
The keywords to extract are found in the CSV-file.
