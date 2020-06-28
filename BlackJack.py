import simplegui
import random
card_size=[73,98]
card_center=[36.5,49]
card_images=simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
card_back_size=[71,96]
card_back_center=[35.5,48]
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    
playing=False
outcome=""
score=0
Suits = ('C', 'S', 'H', 'D')
Ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
Values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
class card:
    def __init__(self,suit,rank):
        if (suit in Suits) and (rank in Ranks):
            self.suit=suit
            self.rank=rank
        else:
            self.suit=None
            self.rank=None
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def str(self):
        return self.suit + self.rank
    def draw(self,canvas,pos):
        card_loc = (card_center[0] + card_size[0] * Ranks.index(self.rank), 
                    card_center[1] + card_size[1] * Suits.index(self.suit))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_center[0], pos[1] + card_center[1]], card_size)   
class Deck:
    def __init__(self):
        self.cards = []
        for s in Suits:
            for r in Ranks:
                self.cards.append(card(s,r))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        return str(len(self.cards)) + " Cards, " + str([str(self.cards[i]) for i in range(0,5)])    
class Hand:
    def __init__(self):
        self.cards = []
        self.hasAces = False

    def __str__(self):
        return str([str(c) for c in self.cards]) + "(" + str(self.get_value()) + " pt)"

    def add_card(self, card):
        self.cards.append(card)
        if card.get_rank() == 'A':
            self.hasAces = True   

    def get_value(self):
        sum_value = sum([Values[c.get_rank()] for c in self.cards])
        if self.hasAces and sum_value+10 <= 21:
            sum_value += 10
        return sum_value

    def draw(self, canvas, pos):
        OFFSET = 100
        if len(self.cards) > 6:
            OFFSET = 30
        elif len(self.cards) > 5:
            OFFSET = 80
        added_offset = 0
        for c in self.cards:
            c.draw(canvas, [pos[0]+added_offset, pos[1]]) 
            added_offset += OFFSET
def deal():
    global outcome, playing,deck, player, dealer, score
    if playing:
        score -= 1
    playing = True
    outcome = ""
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
def hit():
    global player, deck, outcome, score, playing
    if not playing:
        return
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())        
    if player.get_value() > 21:
        outcome = "You went bust and lose."
        score -= 1
        playing = False
        print "Player busting " + str(player), score   
def stand():
    global dealer, outcome, playing, score
    if not playing:
        return
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
    if dealer.get_value() > 21:
        outcome = "Dealer went bust and you win."
        score += 1
    elif dealer.get_value() < player.get_value():
        outcome = "You win."
        score += 1
    else:
        outcome = "You lose."
        score -= 1
   
    print "D" + str(dealer), "P" + str(player), score    
    playing = False
def draw(canvas):
    canvas.draw_text("Blackjack", (100,100), 48,"Cyan", 'sans-serif')
    canvas.draw_text("Score "+str(score), (350, 100), 36, "Black", 'sans-serif' )
    canvas.draw_text("Dealer", (50, 200), 36, "Black", 'sans-serif')
    canvas.draw_text(outcome, (200, 200), 28, "Black", 'sans-serif')
    canvas.draw_text("Player", (50, 400), 36, "Black", 'sans-serif')
    if playing:
        canvas.draw_text("Hit or Stand?", (220, 400), 30, "Black", 'sans-serif')
    else:
        canvas.draw_text("New Deal?", (220, 400), 30, "Black", 'sans-serif')
    dealer.draw(canvas, (50,220))
    if playing:
        canvas.draw_image(card_back, card_back_center, card_back_size, 
                          (51+card_back_center[0], 221+card_back_center[1]) , card_size)
    player.draw(canvas, (50,420))
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
deal()
frame.start()