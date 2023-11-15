# Library monopoly_functions
# Description: 
#   functions for a simple Monopoly game simulation
#   Assignment 2 edition
# Functions Included in Library: 
#   setup_player()
#   display()
#   move_player()
# Author: Carl Gregory
# Date: 8 April 2023
# Revised: 
#    9 April 2023

# import library modules here
import random

# Define global constants (name in ALL_CAPS)
PLAYER1 = 1
PLAYER2 = 2

START_MONEY = 1500
GO_MONEY = 200
NOT_OWNED = "none"

HIGHEST_SQUARE = 3
NUM_TURNS = 5
DIE_SIDES = 6

# These are index values to self-document the lists:
# player[NAME] and property[OWNER] are more meaningful than
# player[0] and property[4], for example

NAME = 0    # these work for both players and property
SQUARE = 1  # used to be "location"

MONEY = 2   # the only other player attribute

PRICE = 2   # property has more features
RENT = 3
OWNER = 4

# Function setup_player()
# Description:
#   creates and returns an initialized player list
#   the player list contains a name, a position, and money
#
#   initial position is 0 and initial money is START_MONEY
#   the name is received as a parameter
# Calls:
#   none
# Parameters:
#   name            str
# Returns:
#   values          list

def setup_player ( name ):

    # Declare Local Variable types (NOT parameters)
    values = list()

    values = []
    values = [ name, 0, START_MONEY ]
        
    # Return the return variable, if any
    return values

#} Function setup_player()

# Function display()
# Description:
#   displays a status line
#       if display_type is "header",
#       print a "column header" line with each player's name and position
#
#       if display_type is "status",
#       print a line with each player's money and position
#       lined up beneath the column headers
# Calls:
#   none
# Parameters:
#   display_type    str
#   player1         list
#   player2         list
# Returns:
#   none

def display ( display_type, player1, player2 ):

    # Declare Local Variable types (NOT parameters)

    if ( display_type == "header" ):
        print( f' {player1[NAME]:<5} square  {player2[NAME]:<5} square' )
    elif ( display_type == "status" ):
        print( f' ${player1[MONEY]:4}{player1[SQUARE]:7}  ${player2[MONEY]}{player2[SQUARE]:7}' )
    else:
        print( "*****  LOGIC ERROR 1  *****" )
    #if

    # Return the return variable, if any

#} Function display()

# Function move_player()
# Description:
#   revises a player's square by adding a random number
#   between 1 and DIE_SIDES (i.e., "roll a die")
#
#   the resulting square "wraps around" the board
#   using the formula
#       square = (square + move) % (HIGHEST_SQUARE + 1)
#   so moving 1 from square 3 will end up in square 0, etc.
# Calls:
#   none
# Parameters:
#   player      list
# Returns:
#   player      list

def move_player ( player ):

    # Declare Local Variable types (NOT parameters)
    player_move = int()

    player_move = random.randint( 1, DIE_SIDES )
    player[SQUARE] = (player[SQUARE] + player_move) % (HIGHEST_SQUARE + 1)

    # Return the return variable, if any
    return player

#} Function move_player()


# End Module monopoly_functions 

if ( __name__ == "__main__" ):
    p1 = setup( "player", "cat" )
    p2 = setup( "player", "dog" )
    prop1 = setup( "property", "Mediterranean Ave." )
    prop2 = setup( "property", "Baltic Ave." )
    prop3 = setup( "property", "Reading Railroad" )
    print( prop1, prop2, prop3 )
    display( "header", p1, p2 )
    display( "status", p1, p2 )
    p1 = buy( p1, prop1 )
    p2 = buy( p1, prop3 )
    display( "header", p1, p2 )
    display( "status", p1, p2 )
    p1 = buy( p1, prop2 )
    display( "header", p1, p2 )
    display( "status", p1, p2 )
##    pay_rent( p1, p2, prop3 )
##    pay_rent( p1, p2, prop3 )
##    pay_rent( p1, p2, prop3 )
# if running standalone


#****************************************************************
#   blank layout for adding more functions                      *
#****************************************************************

# Function stub()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def stub ():

    # Declare Local Variable types (NOT parameters)

    print ( "stub" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function stub()



