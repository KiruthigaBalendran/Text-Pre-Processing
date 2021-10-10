import argparse
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import data


# Set up CLI Arguments
parser = argparse.ArgumentParser()

# Arguments
required = parser.add_argument_group('required arguments')
required.add_argument("-d", "--data", required=True, help="student/twitter/research.")

args = parser.parse_args()

if args.data == 'student':
    text = data.student_course_feedback
elif args.data == 'twitter':
    text = data.twitter
elif args.data == 'research':
    text = data.research_paper

# Tokenize the data
token_data = word_tokenize(text)

stemmer = PorterStemmer()

# Printing the stem word
for word in token_data:
	rootWord=stemmer.stem(word)
	print("Stem word for {} is {}".format(word,rootWord))