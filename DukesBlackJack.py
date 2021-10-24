#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
import random


class MainWindow:
    def __init__(self, master):
        self.master = master
        # self.master.geometry("500x500+400+50")
        self.master.title("Welcome to Duke's BlackJack Application, Enjoy! ")
        self.screenW = self.master.winfo_screenwidth()
        self.screenH = self.master.winfo_screenheight()
        sW = self.screenW * 0.65
        sH = self.screenH * 0.75

        pos = int(self.screenW / 2)-self.screenW * 0.3
        self.master.geometry("%dx%d+%d+50" % (sW, sH, pos))
        self.master.resizable(False, False)
        
        self.canvas = tk.Canvas(self.master, heigh= sH, width= sW, bg= 'green' )
        self.canvas.pack()
        
        self.deck = ImageTk.PhotoImage(Image.open('png/cardBack.png'))
        self.clubs2 = ImageTk.PhotoImage(Image.open('png/2_of_clubs.png'))
        self.clubs3 = ImageTk.PhotoImage(Image.open('png/3_of_clubs.png'))
        self.clubs4 = ImageTk.PhotoImage(Image.open('png/4_of_clubs.png'))
        self.clubs5 = ImageTk.PhotoImage(Image.open('png/5_of_clubs.png'))
        self.clubs6 = ImageTk.PhotoImage(Image.open('png/6_of_clubs.png'))
        self.clubs7 = ImageTk.PhotoImage(Image.open('png/7_of_clubs.png'))
        self.clubs8 = ImageTk.PhotoImage(Image.open('png/8_of_clubs.png'))
        self.clubs9 = ImageTk.PhotoImage(Image.open('png/9_of_clubs.png'))
        self.clubs10 = ImageTk.PhotoImage(Image.open('png/10_of_clubs.png'))
        self.clubsJ = ImageTk.PhotoImage(Image.open('png/jack_of_clubs.png'))
        self.clubsQ = ImageTk.PhotoImage(Image.open('png/queen_of_clubs.png'))
        self.clubsK = ImageTk.PhotoImage(Image.open('png/king_of_clubs.png'))
        self.clubsA = ImageTk.PhotoImage(Image.open('png/ace_of_clubs.png'))
        self.diamonds2 = ImageTk.PhotoImage(Image.open('png/2_of_diamonds.png'))
        self.diamonds3 = ImageTk.PhotoImage(Image.open('png/3_of_diamonds.png'))
        self.diamonds4 = ImageTk.PhotoImage(Image.open('png/4_of_diamonds.png'))
        self.diamonds5 = ImageTk.PhotoImage(Image.open('png/5_of_diamonds.png'))
        self.diamonds6 = ImageTk.PhotoImage(Image.open('png/6_of_diamonds.png'))
        self.diamonds7 = ImageTk.PhotoImage(Image.open('png/7_of_diamonds.png'))
        self.diamonds8 = ImageTk.PhotoImage(Image.open('png/8_of_diamonds.png'))
        self.diamonds9 = ImageTk.PhotoImage(Image.open('png/9_of_diamonds.png'))
        self.diamonds10 = ImageTk.PhotoImage(Image.open('png/10_of_diamonds.png'))
        self.diamondsJ = ImageTk.PhotoImage(Image.open('png/jack_of_diamonds.png'))
        self.diamondsQ = ImageTk.PhotoImage(Image.open('png/queen_of_diamonds.png'))
        self.diamondsK = ImageTk.PhotoImage(Image.open('png/king_of_diamonds.png'))
        self.diamondsA = ImageTk.PhotoImage(Image.open('png/ace_of_diamonds.png'))     
        self.hearts2 = ImageTk.PhotoImage(Image.open('png/2_of_hearts.png'))
        self.hearts3 = ImageTk.PhotoImage(Image.open('png/3_of_hearts.png'))
        self.hearts4 = ImageTk.PhotoImage(Image.open('png/4_of_hearts.png'))
        self.hearts5 = ImageTk.PhotoImage(Image.open('png/5_of_hearts.png'))
        self.hearts6 = ImageTk.PhotoImage(Image.open('png/6_of_hearts.png'))
        self.hearts7 = ImageTk.PhotoImage(Image.open('png/7_of_hearts.png'))
        self.hearts8 = ImageTk.PhotoImage(Image.open('png/8_of_hearts.png'))
        self.hearts9 = ImageTk.PhotoImage(Image.open('png/9_of_hearts.png'))
        self.hearts10 = ImageTk.PhotoImage(Image.open('png/10_of_hearts.png'))
        self.heartsJ = ImageTk.PhotoImage(Image.open('png/jack_of_hearts.png'))
        self.heartsQ = ImageTk.PhotoImage(Image.open('png/queen_of_hearts.png'))
        self.heartsK = ImageTk.PhotoImage(Image.open('png/king_of_hearts.png'))
        self.heartsA = ImageTk.PhotoImage(Image.open('png/ace_of_hearts.png'))
        self.spades2 = ImageTk.PhotoImage(Image.open('png/2_of_spades.png'))
        self.spades3 = ImageTk.PhotoImage(Image.open('png/3_of_spades.png'))
        self.spades4 = ImageTk.PhotoImage(Image.open('png/4_of_spades.png'))
        self.spades5 = ImageTk.PhotoImage(Image.open('png/5_of_spades.png'))
        self.spades6 = ImageTk.PhotoImage(Image.open('png/6_of_spades.png'))
        self.spades7 = ImageTk.PhotoImage(Image.open('png/7_of_spades.png'))
        self.spades8 = ImageTk.PhotoImage(Image.open('png/8_of_spades.png'))
        self.spades9 = ImageTk.PhotoImage(Image.open('png/9_of_spades.png'))
        self.spades10 = ImageTk.PhotoImage(Image.open('png/10_of_spades.png'))
        self.spadesJ = ImageTk.PhotoImage(Image.open('png/jack_of_spades.png'))
        self.spadesQ = ImageTk.PhotoImage(Image.open('png/queen_of_spades.png'))
        self.spadesK = ImageTk.PhotoImage(Image.open('png/king_of_spades.png'))
        self.spadesA = ImageTk.PhotoImage(Image.open('png/ace_of_spades.png'))
        
        self.chip5img = ImageTk.PhotoImage(Image.open('png/5.png'))
        self.chip10img = ImageTk.PhotoImage(Image.open('png/10.png'))
        self.chip25img = ImageTk.PhotoImage(Image.open('png/25.png'))
        self.chip50img = ImageTk.PhotoImage(Image.open('png/50.png'))
        self.chip100img = ImageTk.PhotoImage(Image.open('png/100.png'))
        self.chip250img = ImageTk.PhotoImage(Image.open('png/250.png'))

        self.myDeck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']

        self.card = ''
        self.dealers2ndcard = ''

        self.bust = False
        self.blackJack = False
        
        self.total = 0
        self.bet = 0
        
        self.playerHand = []
        self.dealerHand = []
        self.playerSum = 0
        self.dealerSum = 0
        self.playerDraw = ''
        self.dealerDraw = ''

        random.shuffle(self.myDeck)

    
        self.butDeck = tk.Button(self.canvas, image= self.deck, bg= 'green', activebackground= 'green', command= lambda: self.PlayerDrawCard(), state= 'disabled')
        self.butDeck.place(relx= 0.01, rely= 0.365, height= 120 , width= 70)     
        self.dealercard1 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard1.place(relx= 0.01, rely= 0.01, height= 120 , width= 70)
        self.dealercard2 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard2.place(relx= 0.109, rely= 0.01, height= 120 , width= 70)
        self.dealercard3 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard3.place(relx= 0.208, rely= 0.01, height= 120 , width= 70)
        self.dealercard4 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard4.place(relx= 0.307, rely= 0.01, height= 120 , width= 70)    
        self.dealercard5 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard5.place(relx= 0.406, rely= 0.01, height= 120 , width= 70)
        self.dealercard6 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard6.place(relx= 0.505, rely= 0.01, height= 120 , width= 70)
        self.dealercard7 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard7.place(relx= 0.604, rely= 0.01, height= 120 , width= 70)
        self.dealercard8 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard8.place(relx= 0.703, rely= 0.01, height= 120 , width= 70)
        self.dealercard9 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard9.place(relx= 0.802, rely= 0.01, height= 120 , width= 70)
        self.dealercard10 = tk.Label(self.canvas, bg= 'green') 
        self.dealercard10.place(relx= 0.901, rely= 0.01, height= 120 , width= 70)
        self.playercard1 = tk.Label(self.canvas, bg= 'green') 
        self.playercard1.place(relx= 0.01, rely= 0.75, height= 120 , width= 70)
        self.playercard2 = tk.Label(self.canvas, bg= 'green') 
        self.playercard2.place(relx= 0.109, rely= 0.75, height= 120 , width= 70)
        self.playercard3 = tk.Label(self.canvas, bg= 'green') 
        self.playercard3.place(relx= 0.208, rely= 0.75, height= 120 , width= 70)
        self.playercard4 = tk.Label(self.canvas, bg= 'green') 
        self.playercard4.place(relx= 0.307, rely= 0.75, height= 120 , width= 70)
        self.playercard5 = tk.Label(self.canvas, bg= 'green') 
        self.playercard5.place(relx= 0.406, rely= 0.75, height= 120 , width= 70)
        self.playercard6 = tk.Label(self.canvas, bg= 'green') 
        self.playercard6.place(relx= 0.505, rely= 0.75, height= 120 , width= 70)
        self.playercard7 = tk.Label(self.canvas, bg= 'green') 
        self.playercard7.place(relx= 0.604, rely= 0.75, height= 120 , width= 70)
        self.playercard8 = tk.Label(self.canvas, bg= 'green') 
        self.playercard8.place(relx= 0.703, rely= 0.75, height= 120 , width= 70)
        self.playercard9 = tk.Label(self.canvas, bg= 'green') 
        self.playercard9.place(relx= 0.802, rely= 0.75, height= 120 , width= 70)
        self.playercard10 = tk.Label(self.canvas, bg= 'green') 
        self.playercard10.place(relx= 0.901, rely= 0.75, height= 120 , width= 70)
        
        self.chip5 = tk.Button(self.canvas, bg= 'green', activebackground= 'green', relief='flat', highlightthickness=0, bd=0, image= self.chip5img, state= 'disabled', command=lambda: self.Betting(5)) 
        self.chip5.place(relx= 0.28, rely= 0.625, height= 55 , width= 55)
        self.chip10 = tk.Button(self.canvas, bg= 'green', activebackground= 'green', relief='flat', highlightthickness=0, bd=0, image= self.chip10img, state= 'disabled', command=lambda: self.Betting(10)) 
        self.chip10.place(relx= 0.36, rely= 0.625, height= 55 , width= 55)
        self.chip25 = tk.Button(self.canvas, bg= 'green', activebackground= 'green', relief='flat', highlightthickness=0, bd=0, image= self.chip25img, state= 'disabled', command=lambda: self.Betting(25)) 
        self.chip25.place(relx= 0.44, rely= 0.625, height= 55 , width= 55)
        self.chip50 = tk.Button(self.canvas, bg= 'green', activebackground= 'green', relief='flat', highlightthickness=0, bd=0, image= self.chip50img, state= 'disabled', command=lambda: self.Betting(50)) 
        self.chip50.place(relx= 0.52, rely= 0.625, height= 55 , width= 55)
        self.chip100 = tk.Button(self.canvas, bg= 'green', activebackground= 'green', relief='flat', highlightthickness=0, bd=0, image= self.chip100img, state= 'disabled', command=lambda: self.Betting(100)) 
        self.chip100.place(relx= 0.6, rely= 0.625, height= 55 , width= 55)
        self.chip250 = tk.Button(self.canvas, bg= 'green', activebackground= 'green', relief='flat', highlightthickness=0, bd=0, image= self.chip250img, state= 'disabled', command=lambda: self.Betting(250)) 
        self.chip250.place(relx= 0.68, rely= 0.625, height= 55 , width= 55)
        
        self.PlayAgainButton = tk.Button(self.canvas, text= 'Play Again', bg= '#347C17', font= ('Algerian', 11), state= 'disabled', activebackground= 'green', command=lambda: self.PlayAgain())
        self.PlayAgainButton.place(relx= 0.85, rely= 0.42, height= 40, width= 110)
        
        self.insertButton = tk.Button(self.canvas, text= 'Add \nMoney!', bg= '#347C17', font= ('Algerian', 11), activebackground= 'green', command=lambda: self.create_window())
        self.insertButton.place(relx= 0.85, rely= 0.51, height= 40, width= 110)
        
        self.placeBetButton = tk.Button(self.canvas, text= 'Place', bg= '#347C17', state= 'disabled', font= ('Algerian', 11), activebackground= 'green', command=lambda: self.placeBet())
        self.placeBetButton.place(relx= 0.51, rely= 0.53, height= 30, width= 80)
        
        self.undoButton = tk.Button(self.canvas, text= 'Undo', bg= '#347C17', font= ('Algerian', 11), state= 'disabled', activebackground= 'green', command=lambda: self.undoBet())
        self.undoButton.place(relx= 0.64, rely= 0.53, height= 30, width= 80)
        
        self.standButton = tk.Button(self.canvas, text= 'Stand', bg= '#347C17', font= ('Algerian', 11), state= 'disabled', activebackground= 'green', command=lambda: self.Stand())
        self.standButton.place(relx= 0.11, rely= 0.45, height= 30, width= 70)
        
        self.totalScreen = tk.Label(self.canvas, text= f'Total :  {self.total}', bg= 'green', font=('Bernard MT Condensed', 14), anchor= 'w')
        self.totalScreen.place(relx= 0.02, rely= 0.625, height= 50, width= 120)
        
        self.betScreen = tk.Label(self.canvas, text= f'Bet :  {self.bet}', bg= 'green', font= ('Bernard MT Condensed', 14), anchor= 'w')
        self.betScreen.place(relx= 0.32, rely= 0.512, height= 50, width= 130)
        
        self.messageScreen = tk.Label(self.canvas, text= "Welcome to Duke's \n BlackJack!", bg= 'green', font=('Old English Text MT',33))
        self.messageScreen.place(relx= 0.25, rely= 0.28, height= 100, width= 460)
                

    def CardMapping(self, draw):
        self.deckDict = {'2C' : self.clubs2,
                    '3C' : self.clubs3,
                    '4C' : self.clubs4,
                    '5C' : self.clubs5,
                    '6C' : self.clubs6, 
                    '7C' : self.clubs7,
                    '8C' : self.clubs8,
                    '9C' : self.clubs9,
                    '10C' : self.clubs10,
                    'JC' : self.clubsJ,
                    'QC' : self.clubsQ,
                    'KC' : self.clubsK,
                    'AC' : self.clubsA,
                    '2D' : self.diamonds2,
                    '3D' : self.diamonds3,
                    '4D' : self.diamonds4,
                    '5D' : self.diamonds5,
                    '6D' : self.diamonds6,
                    '7D' : self.diamonds7,
                    '8D' : self.diamonds8,
                    '9D' : self.diamonds9,
                    '10D' : self.diamonds10,
                    'JD' : self.diamondsJ,
                    'QD' : self.diamondsQ,
                    'KD' : self.diamondsK,
                    'AD' : self.diamondsA,
                    '2H' : self.hearts2,
                    '3H' : self.hearts3,
                    '4H' : self.hearts4,
                    '5H' : self.hearts5,
                    '6H' : self.hearts6,
                    '7H' : self.hearts7,
                    '8H' : self.hearts8,
                    '9H' : self.hearts9,
                    '10H' : self.hearts10,
                    'JH' : self.heartsJ,
                    'QH' : self.heartsQ,
                    'KH' : self.heartsK,
                    'AH' : self.heartsA,
                    '2S' : self.spades2,
                    '3S' : self.spades3,
                    '4S' : self.spades4,
                    '5S' : self.spades5,
                    '6S' : self.spades6,
                    '7S' : self.spades7,
                    '8S' : self.spades8,
                    '9S' : self.spades9,
                    '10S' : self.spades10,
                    'JS' : self.spadesJ,
                    'QS' : self.spadesQ,
                    'KS' : self.spadesK,
                    'AS' : self.spadesA}
        self.card = self.deckDict.get(draw) 
        return(self.card)
    
    def placePlayersCard(self):
        if self.playercard5['text'] == '':
            self.playercard5.config(text= '.', image= self.card)
        elif self.playercard6['text'] == '':
            self.playercard6.config(text= '.', image= self.card)
        elif self.playercard4['text'] == '':
            self.playercard4.config(text= '.', image= self.card)
        elif self.playercard7['text'] == '':
            self.playercard7.config(text= '.', image= self.card)
        elif self.playercard3['text'] == '':
            self.playercard3.config(text= '.', image= self.card)
        elif self.playercard8['text'] == '':
            self.playercard8.config(text= '.', image= self.card)
        elif self.playercard2['text'] == '':
            self.playercard2.config(text= '.', image= self.card)
        elif self.playercard9['text'] == '':
            self.playercard9.config(text= '.', image= self.card)
        elif self.playercard1['text'] == '':
            self.playercard1.config(text= '.', image= self.card)
        elif self.playercard10['text'] == '':
            self.playercard10.config(text= '.', image= self.card)
            
    def placeDealersCard(self):
        if self.dealercard5['text'] == '':
            self.dealercard5.config(text= '.', image= self.card)
        elif self.dealercard6['text'] == '':
            self.dealercard6.config(text= '.', image= self.card)
        elif self.dealercard4['text'] == '':
            self.dealercard4.config(text= '.', image= self.card)
        elif self.dealercard7['text'] == '':
            self.dealercard7.config(text= '.', image= self.card)
        elif self.dealercard3['text'] == '':
            self.dealercard3.config(text= '.', image= self.card)
        elif self.dealercard8['text'] == '':
            self.dealercard8.config(text= '.', image= self.card)
        elif self.dealercard2['text'] == '':
            self.dealercard2.config(text= '.', image= self.card)
        elif self.dealercard9['text'] == '':
            self.dealercard9.config(text= '.', image= self.card)
        elif self.dealercard1['text'] == '':
            self.dealercard1.config(text= '.', image= self.card)
        elif self.dealercard10['text'] == '':
            self.dealercard10.config(text= '.', image= self.card)
            
    def calculatePlayersHand(self):
        self.playerSum = 0
        valueDict = {'2C' : 2,
                    '3C' : 3,
                    '4C' : 4,
                    '5C' : 5,
                    '6C' : 6, 
                    '7C' : 7,
                    '8C' : 8,
                    '9C' : 9,
                    '10C' : 10,
                    'JC' : 10,
                    'QC' : 10,
                    'KC' : 10,
                    '2D' : 2,
                    '3D' : 3,
                    '4D' : 4,
                    '5D' : 5,
                    '6D' : 6,
                    '7D' : 7,
                    '8D' : 8,
                    '9D' : 9,
                    '10D' : 10,
                    'JD' : 10,
                    'QD' : 10,
                    'KD' : 10,
                    '2H' : 2,
                    '3H' : 3,
                    '4H' : 4,
                    '5H' : 5,
                    '6H' : 6,
                    '7H' : 7,
                    '8H' : 8,
                    '9H' : 9,
                    '10H' : 10,
                    'JH' : 10,
                    'QH' : 10,
                    'KH' : 10,
                    '2S' : 2,
                    '3S' : 3,
                    '4S' : 4,
                    '5S' : 5,
                    '6S' : 6,
                    '7S' : 7,
                    '8S' : 8,
                    '9S' : 9,
                    '10S' : 10,
                    'JS' : 10,
                    'QS' : 10,
                    'KS' : 10 }
        
        ace = False
        
        Aces = [a for a in self.playerHand if a == 'AC' or a == 'AD' or a == 'AH' or a == 'AS']
        noAces = [na for na in self.playerHand if na != 'AC' and na != 'AD' and na != 'AH' and na != 'AS']
       
        if len(Aces) > 0:
            ace = True
            
        if ace == False:
            for na in noAces:
                self.playerSum += valueDict.get(na)    
            return(self.playerSum)
        else:          
            for na in noAces:
                self.playerSum += valueDict.get(na)
                       
            if len(Aces) == 1:
                if self.playerSum < 11:
                    self.playerSum += 11
                    return(self.playerSum)
                else:
                    self.playerSum += 1
                    return(self.playerSum)
            elif len(Aces) > 1:
                self.playerSum += 10 + len(Aces)
                return(self.playerSum)
            
    def calculateDealersHand(self):
        self.dealerSum = 0
        valueDict = {'2C' : 2,
                    '3C' : 3,
                    '4C' : 4,
                    '5C' : 5,
                    '6C' : 6, 
                    '7C' : 7,
                    '8C' : 8,
                    '9C' : 9,
                    '10C' : 10,
                    'JC' : 10,
                    'QC' : 10,
                    'KC' : 10,
                    '2D' : 2,
                    '3D' : 3,
                    '4D' : 4,
                    '5D' : 5,
                    '6D' : 6,
                    '7D' : 7,
                    '8D' : 8,
                    '9D' : 9,
                    '10D' : 10,
                    'JD' : 10,
                    'QD' : 10,
                    'KD' : 10,
                    '2H' : 2,
                    '3H' : 3,
                    '4H' : 4,
                    '5H' : 5,
                    '6H' : 6,
                    '7H' : 7,
                    '8H' : 8,
                    '9H' : 9,
                    '10H' : 10,
                    'JH' : 10,
                    'QH' : 10,
                    'KH' : 10,
                    '2S' : 2,
                    '3S' : 3,
                    '4S' : 4,
                    '5S' : 5,
                    '6S' : 6,
                    '7S' : 7,
                    '8S' : 8,
                    '9S' : 9,
                    '10S' : 10,
                    'JS' : 10,
                    'QS' : 10,
                    'KS' : 10 }
        
        ace = False
        
        Aces = [a for a in self.dealerHand if a == 'AC' or a == 'AD' or a == 'AH' or a == 'AS']
        noAces = [na for na in self.dealerHand if na != 'AC' and na != 'AD' and na != 'AH' and na != 'AS']
       
        if len(Aces) > 0:
            ace = True
            
        if ace == False:
            for na in noAces:
                self.dealerSum += valueDict.get(na)    
            return(self.dealerSum)
        else:          
            for na in noAces:
                self.dealerSum += valueDict.get(na)
                       
            if len(Aces) == 1:
                if self.dealerSum < 11:
                    self.dealerSum += 11
                    return(self.dealerSum)
                else:
                    self.dealerSum += 1
                    return(self.dealerSum)
            elif len(Aces) > 1:
                self.dealerSum += 10 + len(Aces)
                return(self.dealerSum)        
    
    def checkBlackJack(self):
        if self.playerSum == 21 and len(self.playerHand) == 2:
            self.blackJack = True
        return(self.blackJack)
    
    def checkBust(self, who):
        if who == 'player':
            if self.playerSum > 21:
                self.bust = True
        else:
            if self.dealerSum > 21:
                self.bust = True
        return(self.bust)
    
    def doubleBlackJack(self):
        if self.blackJack == True:
            if self.dealerSum == 21 and len(self.dealerHand) == 2:
                self.total += self.bet * 1.5
                self.totalScreen.config(text= f'Total :  {round(self.total,1)}€')
                self.messageScreen.config(text= f'Both have BLACKJACK! \n You won {round(self.bet*0.5,1)}€ ! \nClick Play Again')
                self.PlayAgainButton.config(state= 'normal')
                self.totalScreen.config(fg= '#6CC417')
                return(self.total)
            else:
                self.total += self.bet * 2
                self.totalScreen.config(text= f'Total :  {self.total}€')
                self.messageScreen.config(text= f'You won with BLACKJACK {self.bet}€ ! \nClick Play Again')
                self.PlayAgainButton.config(state= 'normal')
                self.totalScreen.config(fg= '#6CC417')
                return(self.total)        
                
    def moneyLost(self):
        self.totalScreen.config(text= f'Total :  {self.total}€')
        self.messageScreen.config(text= f'Dealer won! \nYou lost {self.bet}€ \nClick Play Again')
        self.PlayAgainButton.config(state= 'normal')
        self.totalScreen.config(fg= 'red')
        return(self.total)
                
    def moneyEarn(self):
        self.total += self.bet * 2
        self.totalScreen.config(text= f'Total :  {self.total}€')
        self.messageScreen.config(text= f'You won {self.bet}€ ! \nClick Play Again')
        self.PlayAgainButton.config(state= 'normal')
        self.totalScreen.config(fg= '#6CC417')
        return(self.total)       
        
    def PlayerDrawCard(self):
        self.playerDraw = self.myDeck.pop()
        self.playerHand.append(self.playerDraw)
        self.calculatePlayersHand()
        self.CardMapping(self.playerDraw)
        self.placePlayersCard()  
        self.checkBust('player')
        if self.bust == True:
            self.moneyLost()
            self.butDeck.config(state= 'disabled')
            self.standButton.config(state= 'disabled')
            if self.total == 0:
                self.PlayAgainButton.config(state= 'disabled')
                self.insertButton.config(state= 'normal')
            else:
                self.PlayAgainButton.config(state= 'normal')
        
    def DealerDrawCard(self):
        self.dealerDraw = self.myDeck.pop()
        self.dealerHand.append(self.dealerDraw)
        self.calculateDealersHand()
        self.CardMapping(self.dealerDraw)
        self.placeDealersCard()
        
    def Betting(self, bet):
        if self.total >= bet:
            self.undoButton.config(state= 'normal')
            self.messageScreen.config(text= 'Place your bet \nClick Chips', font= ('Monotype Corsiva',20, 'bold italic'))
            self.totalScreen.config(fg= 'black')
            self.total -= bet
            self.bet += bet
            self.betScreen.config(text= f'Bet :  {self.bet}€')
            self.totalScreen.config(text= f'Total :  {self.total}€')
        elif self.total == 0:
            self.messageScreen.config(text= "You don't have any money!", font= ('Monotype Corsiva',20, 'bold italic'))
            self.totalScreen.config(fg= 'red')
        else:
            self.messageScreen.config(text= "You don't have much money\n place smaller bet", font= ('Monotype Corsiva',20, 'bold italic'))
            self.totalScreen.config(fg= 'red')
    
    def placeBet(self):
        if self.bet > 0:
            self.chip5.config(state= 'disabled')
            self.chip10.config(state= 'disabled')
            self.chip25.config(state= 'disabled')
            self.chip50.config(state= 'disabled')
            self.chip100.config(state= 'disabled')
            self.chip250.config(state= 'disabled')
            self.placeBetButton.config(state= 'disabled')
            self.standButton.config(state= 'normal')
            self.butDeck.config(state= 'normal')
            self.PlayerDrawCard()
            self.DealerDrawCard()
            self.PlayerDrawCard()
            self.dealerDraw = self.myDeck.pop()
            self.dealerHand.append(self.dealerDraw)
            self.calculateDealersHand()
            self.CardMapping(self.dealerDraw)
            self.dealercard6.config(image= self.deck)
            self.dealers2ndcard = self.card   
            self.messageScreen.config(text= 'Click Deck\nor\nClick Stand')
            self.undoButton.config(state= 'disabled')
            return(self.dealers2ndcard)
        else:
            self.messageScreen.config(text= 'You have to bet first! \nClick Chips')
            
    def Stand(self):
        self.standButton.config(state= 'disabled')
        self.messageScreen.config(text= '')
        self.butDeck.config(state= 'disabled')
        self.dealercard6.config(image= self.dealers2ndcard, text= '.')
        self.checkBlackJack()
        self.doubleBlackJack()
        if self.blackJack == False:
            while self.dealerSum <= self.playerSum and self.bust == False:
                self.DealerDrawCard()
                self.checkBust('dealer')
            if self.dealerSum >= self.playerSum and self.bust == False:
                self.moneyLost()
            elif self.bust == True:
                self.moneyEarn()
        self.noMoney()
            
    def PlayAgain(self):
        self.myDeck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
            '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
            '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
    
        self.card = ''
        self.dealers2ndcard = ''
        
        self.bust = False
        self.blackJack = False
        self.bet = 0
        
        self.playerHand = []
        self.dealerHand = []
        self.playerSum = 0
        self.dealerSum = 0
        self.playerDraw = ''
        self.dealerDraw = ''
        
        random.shuffle(self.myDeck)
        
        self.messageScreen.config(text= 'Place your bet \nClick Chips', font= ('Monotype Corsiva', 20, 'bold italic'))
        self.betScreen.config(text= f'Bet :  {self.bet}€')
        self.chip5.config(state= 'normal')
        self.chip10.config(state= 'normal')
        self.chip25.config(state= 'normal')
        self.chip50.config(state= 'normal')
        self.chip100.config(state= 'normal')
        self.chip250.config(state= 'normal')
        self.placeBetButton.config(state= 'normal')
        self.PlayAgainButton.config(state= 'disabled')
        self.totalScreen.config(fg= 'black')
    
        self.playercard5.config(text= '', image= '')
        self.playercard6.config(text= '', image= '')
        self.playercard4.config(text= '', image= '')
        self.playercard7.config(text= '', image= '')
        self.playercard3.config(text= '', image= '')
        self.playercard8.config(text= '', image= '')
        self.playercard2.config(text= '', image= '')
        self.playercard9.config(text= '', image= '')
        self.playercard1.config(text= '', image= '')
        self.playercard10.config(text= '', image= '')
        
        self.dealercard5.config(text= '', image= '')
        self.dealercard6.config(text= '', image= '')
        self.dealercard4.config(text= '', image= '')
        self.dealercard7.config(text= '', image= '')
        self.dealercard3.config(text= '', image= '')
        self.dealercard8.config(text= '', image= '')
        self.dealercard2.config(text= '', image= '')
        self.dealercard9.config(text= '', image= '')
        self.dealercard1.config(text= '', image= '')
        self.dealercard10.config(text= '', image= '')
        
    def undoBet(self):
        self.total += self.bet
        self.bet = 0
        self.betScreen.config(text= f'Bet :  {self.bet}€')
        self.totalScreen.config(text= f'Total :  {self.total}€')
        
    def create_window(self):
        x = self.master.winfo_x()
        y = self.master.winfo_y()  
        self.window = tk.Toplevel(self.master, bg= 'green', heigh= 200, width= 300)
        self.window.title('Add Money Here!')
        self.window.geometry("+%d+%d" % (x + 280, y + 110))
        
        self.insert_money = tk.Label(self.window, bg= 'green', text= 'Add money:', font= ('Monotype Corsiva',14, 'bold italic'))
        self.insert_money.place(relx= 0.15, rely= 0.1)
        
        self.errorwin = tk.Label(self.window, bg= 'green', text= '', fg= 'red', font= ('Monotype Corsiva',11, 'bold italic'))
        self.errorwin.place(relx= 0.23, rely= 0.25)
        
        self.poso = tk.Label(self.window, bg= 'green', text= 'EUR (€): ', font= ('Arial Greek',12))
        self.poso.place(relx= 0.12, rely= 0.42)
        
        self.entry = tk.Entry(self.window, font= ('Arial Greek',12), justify='center')
        self.entry.place(relx= 0.4, rely= 0.42, height= 30, width= 135)
        self.entry.focus_set()
        
        self.okButton = tk.Button(self.window, text= 'OK!', bg= '#347C17', font= ('Algerian', 12), activebackground= 'green', command=lambda: self.insertMoney())
        self.okButton.place(relx= 0.42, rely= 0.67, height= 30, width= 70)
        
        if self.total == 0:
            self.okButton.config(state= 'normal')
    
    def insertMoney(self):
        x = self.entry.get()
        if x != '':
            try:
                x = int(x)
                self.okButton.config(state= 'normal') 
                if x >= 5 and x <= 1000000:
                    self.total = int(x)
                    self.totalScreen.config(text= f'Total :  {self.total}€', fg= 'black')
                    self.PlayAgainButton.config(state= 'normal')               
                    self.insertButton.config(state= 'disabled')
                    self.window.destroy()
                    return(self.total)
                else:
                    self.errorwin.config(text= '5€ up to 1000000€')
            except:
                self.errorwin.config(text= 'Insert the right amount.')
                        
    def noMoney(self):
        if self.total == 0:
           self.insertButton.config(state= 'normal') 
           self.placeBetButton.config(state= 'disabled')
           self.undoButton.config(state= 'disabled')
           self.PlayAgainButton.config(state= 'disabled')
           self.butDeck.config(state= 'disabled')
           self.chip5.config(state= 'disabled')
           self.chip10.config(state= 'disabled')
           self.chip25.config(state= 'disabled')
           self.chip50.config(state= 'disabled')
           self.chip100.config(state= 'disabled')
           self.chip250.config(state= 'disabled')
           
        

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
    