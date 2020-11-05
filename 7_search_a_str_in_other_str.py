'''
Problem Statement:-
You are given few sentences as a list (Python list of sentences). 
Take a query string as an input from the user. 
You have to pull out the sentences matching this query inputted by the user in 
decreasing order of relevance after converting every word in the query and the sentence to lowercase. 
Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

-> Python is not python snake
-> Python is good
-> Python is cool
'''
def matching(sentence1, sentence2):
    word1 = sentence1.strip().split(" ")
    word2 = sentence2.strip().split(" ")
    score = 0
    # query_str 
    for word1 in word1:
        # sntences 
        for word2 in word2:
            # query_str first word was picked and came into sentences and was checked in it by the statement below.
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":

    sentences = ["This is good", "Python is good",
                 "python is not python snake", "My name is vaibhav"]
    query_str = input("Enter a string you want to search:\n")

    # All the scores will be put in this list which are getting returned by the method matching.
    scores = [matching(query_str, sentence) for sentence in sentences]
    # print (scores)
    # sortedSentScore is storing sentScore and sentScore is a sorted zipped list which includes,
    # score of the particular sentence together, we reversed irt as it was asked in question,
    # if condition will help us further print only those results which particullarly have those words.
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] != 0]

    # print(sortedSentScore)
    # output o fsortedSentScore:
    # Enter a string you want to search:
    # python
    # [(1, 'Python is good'), (2, 'python is not python snake')]

    print(f"{len(sortedSentScore)} results found.")
    for score, item in sortedSentScore:
        print(f"\"{item}\" : with a score of {score}")
