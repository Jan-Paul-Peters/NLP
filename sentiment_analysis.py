import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_most_liked_disliked(data, threshold = 10):
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

if __name__ == "__main__":
    threshold = 10

    file_path = 'sentiment/stocks_sentiment.json'  # Replace with your JSON file path
    data = load_data(file_path)
    most_liked, most_disliked, max_relative_positive, max_relative_negative = find_most_liked_disliked(data, threshold= threshold)
    print('-----------------------------------')
    print(f"Most liked: {most_liked}, {max_relative_positive}")
    print('-----------------------------------')
    print(f"Most disliked: {most_disliked}, {max_relative_negative}")