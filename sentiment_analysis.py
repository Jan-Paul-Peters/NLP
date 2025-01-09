import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_most_liked_disliked(data, threshold = 10):

    '''
    most_liked: List of stocks with the highest relative positive sentiment
    most_disliked: List of stocks with the highest relative negative sentiment
    max_relative_positive: Maximum relative positive sentiment
    max_relative_negative: Maximum relative negative sentiment

    the scores are calculated as follows:
        relative_positive = positive_sentiments / total_sentiments
        relative_negative = negative_sentiments / total_sentiments

    '''
    most_liked = []
    most_disliked = []
    max_relative_positive = float('-inf')
    max_relative_negative = float('-inf')

    for stock, sentiment in data.items():
        total_sentiments = sentiment['positive'] +  sentiment['negative'] + sentiment['neutral']
        if total_sentiments < threshold:
            continue

        relative_positive = sentiment['positive']/total_sentiments
        relative_negative = sentiment['negative']/total_sentiments

        print(stock, total_sentiments, relative_positive, relative_negative)
        
        if relative_positive > max_relative_positive:
            max_relative_positive = relative_positive
            most_liked = [stock]
        if relative_positive == max_relative_positive:
            most_liked.append(stock)
        
        if relative_negative > max_relative_negative:
            max_relative_negative = relative_negative
            most_disliked = [stock]
        if relative_negative == max_relative_negative:
            most_disliked.append(stock)

    return most_liked, most_disliked, max_relative_positive, max_relative_negative

def find_most_controversial(data, threshold = 10):

    '''
    
    Controversy score is calculated as follows:
        Controversy score = 4 * relative_negative * relative_positive

        where relative_negative = negative_sentiments / total_sentiments
        and relative_positive = positive_sentiments / total_sentiments

        This score has a maximum of 1 when both relative_negative and relative_positive are 0.5
        This score has a minimum of 0 when either relative_negative or relative_positive is 0
    '''

    most_controversial = []
    max_controversy_score = float('-inf')

    for stock, sentiment in data.items():
        total_sentiments = sentiment['positive'] +  sentiment['negative'] + sentiment['neutral']
        if total_sentiments < threshold:
            continue

        relative_positive = sentiment['positive']/total_sentiments
        relative_negative = sentiment['negative']/total_sentiments

        controversy_score = 4 * relative_negative * relative_positive

        if controversy_score > max_controversy_score:
            max_controversy_score = controversy_score
            most_controversial = [stock]
        if controversy_score == max_controversy_score:
            most_controversial.append(stock)

    return most_controversial, max_controversy_score

if __name__ == "__main__":
    threshold = 10

    file_path = 'sentiment/stocks_sentiment.json'  # Replace with your JSON file path
    data = load_data(file_path)
    most_liked, most_disliked, max_relative_positive, max_relative_negative = find_most_liked_disliked(data, threshold= threshold)

    find_most_controversial, max_controversy_score = find_most_controversial(data, threshold= threshold)

    print('-----------------------------------')
    print(f"Most liked: {most_liked}, {max_relative_positive}")
    print('-----------------------------------')
    print(f"Most disliked: {most_disliked}, {max_relative_negative}")
    print('-----------------------------------')
    print(f"Most controversial: {find_most_controversial}, {max_controversy_score}")