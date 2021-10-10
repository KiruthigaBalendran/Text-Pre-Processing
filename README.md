# Text-Pre-Processing

The repository describes four text pre-processing techniques.
1. Tokenizer
2. Spell Corrector
3. Stemmer
4. Lemmatization

## Installation
1. Install the below Python packages
	* pip install nltk
	* pip install textblob
  
2. Open the Python shell and enter the below commands
	* import nltk
	* nltk.download('punkt')
	* nltk.download('wordnet')

## Execution Steps
1. To run tokenizer.py 
    * for Student Course Feedback data,
	  * python tokenizer.py -d "student"
    * for Twitter data,
	  * python tokenizer.py -d "twitter"
    * for Research Paper data,
	  * python tokenizer.py -d "research"
	
2. To run spellCorrect.py
    * for Student Course Feedback data,
	  * python spellCorrect.py -d "student"
    * for Twitter data,
	  * python spellCorrect.py -d "twitter"
    * for Research Paper data,
	  * python spellCorrect.py -d "research"
	
3. To run stemmer.py 
    * for Student Course Feedback data,
	  * python stemmer.py -d "student"
    * for Twitter data,
	  * python stemmer.py -d "twitter"
    * for Research Paper data,
	  * python stemmer.py -d "research"

4. To run lemmatizer.py 
    * for Student Course Feedback data,
	  * python lemmatizer.py -d "student"
    * for Twitter data,
	  * python lemmatizer.py -d "twitter"
    * for Research Paper data,
	  * python lemmatizer.py -d "research"
