# google-ngram-analytics
Get the actual probabilities of an ngram from the Google Ngram Viewer

You can pass any text corpus full of sentences and obtain probability of each sentence as used in code.

You can also modify the input, by providing any query
We use the JSON data provided and take the CASE INSENSITIVE version of probabilities. (Check the URL itself in your browser to know more)

# INSTALL
Will require nltk, json, urllib

Use Python 3, if you want to use python 2, [check this](https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script) 

# command to use
python scrapengram.py text-file

expects a text file with newline separated sentences
