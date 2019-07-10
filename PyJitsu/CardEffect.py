from enum import Enum
class CardEffect(Enum):
    NONE = 0
    
    NOFIRE # When scored, fire cannot be played in the next round.
    NOWATER # When scored, water cannot be played in the next round.
    NOSNOW # When scored, snow cannot be played in the next round.
    
    ADDTWO # When scored, your card gets +2 for the next round.
    MINUSTWO # When scored, your opponent's card gets -2 for the next round.
    REVERSE # When scored, cards' numbers are reversed for the next round.
    
    DISCARDFIRE # When scored, one of your opponent's fire cards is discarded.
    DISCARDWATER # When scored, one of your opponent's water cards is discarded.
    DISCARDSNOW # When scored, one of your opponent's snow cards is discarded.
    
    DISCARDRED # When scored, one of your opponent's red cards is discarded.
    DISCARDBLUE # When scored, one of your opponent's blue cards is discarded.
    DISCARDYELLOW # When scored, one of your opponent's yellow cards is discarded.
    DISCARDGREEN # When scored, one of your opponent's green cards is discarded.
    DISCARDORANGE # When scored, one of your opponent's orange cards is discarded.
    DISCARDPURPLE # When scored, one of your opponent's purple cards is discarded.

    DISCARDALLRED # When scored, all of your opponent's red cards are discarded.
    DISCARDALLBLUE # When scored, all of your opponent's blue cards are discarded.
    DISCARDALLYELLOW # When scored, all of your opponent's yellow cards are discarded.
    DISCARDALLGREEN # When scored, all of your opponent's green cards are discarded.
    DISCARDALLORANGE # When scored, all of your opponent's orange cards are discarded.
    DISCARDALLPURPLE # When scored, all of your opponent's purple cards are discarded.

    FIRETOSNOW # When played, all fire cards become snow for the current round.
    WATERTOFIRE # When played, all water cards become fire for the current round.
    SNOWTOWATER # When played, all snow cards become water for the current round.
