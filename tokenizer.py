from nltk.tokenize import word_tokenize,TweetTokenizer,sent_tokenize
import argparse
import data

# Set up CLI Arguments
parser = argparse.ArgumentParser()

# Arguments
required = parser.add_argument_group('required arguments')
required.add_argument("-d", "--data", required=True, help="student/twitter/research.")

args = parser.parse_args()

if args.data == 'student':
    # Calling word tokenizer
    print("\nStudent Course Feedback \n")
    print("\nWord Tokenizer \n")
    print(word_tokenize(data.student_course_feedback))
    print("\nSentence Tokenizer \n")
    print(sent_tokenize(data.student_course_feedback))
    print("\n")
elif args.data == 'twitter':
    # Calling Tweet tokenizer
    tweet_tokenizer = TweetTokenizer()
    print("\nTwitter Data \n")
    print(tweet_tokenizer.tokenize(data.twitter))
    print("\n")
elif args.data == 'research':
    # Calling word tokenizer
    print("\nResearch Paper \n")
    print(word_tokenize(data.research_paper))
    print("\n")



