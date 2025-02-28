def card_sorter(cards):
    # Define the order of ranks

    rank_order = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7,'10':8, 'J':9, 'Q':10, 'K':11, 'A':12}

    # Sort the cards based on rank order

    sorted_cards = sorted(cards, key=lambda card: rank_order[card])
    
    return sorted_cards


print(card_sorter(['2','4','6','8','A', 'K']))