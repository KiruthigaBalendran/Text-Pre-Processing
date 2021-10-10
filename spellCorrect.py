from textblob import TextBlob
import argparse
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

# Calling TextBlob function
blob_data = TextBlob(text)   

# Correcting the data
corrected_data = blob_data.correct()   

# Printing the corrected data
print(corrected_data)