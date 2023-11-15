# Program monopoly
# Description: 
#   Simulates playing the board game Monopoly
#   Assignment 3 edition
# Author: <your name>
# Date: <creation date>
# Revised: 
#   <revision date>

# import library modules here
import monopoly_functions, random

# Define global constants (name in ALL_CAPS)
PROPERTIES_FILE = "properties.txt"          # file of property records
PLAYER_PIECES_FILE = "playing_pieces.txt"   # file of possible playing pieces
PROPERTY_ITEMS = 3                          # size of a property record

PLAYER1 = 1
PLAYER2 = 2

START_MONEY = 1500
GO_MONEY = 200
NOT_OWNED = "not_owned"

HIGHEST_SQUARE = 6
NUM_TURNS = 5

# These are index values to self-document the lists:
# player[NAME] and property[OWNER] are more meaningful than
# player[0] and property[4], for example

NAME = 0    # these work for both players and property
SQUARE = 1  # used to be "location"
MONEY = 2   # the only other player attribute

PRICE = 1   # property has more features (name is still [0])
RENT = 2
OWNER = 3

def main():

    # Declare Variable types (EVERY variable used in this main program)
    player1 = list()
    player2 = list()
    board_items = list()
    piece_list = list()
    this_property = list()
    game_board = list()
    num_squares = int()
    index = int()
    name1 = str()
    name2 = str()

    # initialize all variables
    player1 = []
    player2 = []
    board_items = []
    piece_list = []
    this_property = []
    game_board = []
    num_squares = 0
    index = 0
    name1 = ''
    name2 = ''

################# MAKE UPDATES HERE ########################
    # initialize board items (the properties) and the piece list
    # by passing the names of the files that
    # hold the properties and player pieces
    
    # randomly choose a name from the piece list for player1
    
    # randomly choose a name from the piece list for player2
    # keep choosing a name as long as the player2 name
    # is the same as player1
    
#############################################################
    

    # set up the players with the chosen names
    player1 = monopoly_functions.setup_player( name1 )
    player2 = monopoly_functions.setup_player( name2 )
    

################# MAKE UPDATES HERE ########################
    # calculate the number of board squares by
    # dividing the board items by
    # the size of a property record

    # for each square,
    # set up the next property from the board items and
    # append the property to the game board
    
#############################################################

    # display header line and initial status line
    monopoly_functions.display( "header", player1, player2 )
    monopoly_functions.display( "status", player1, player2 )

    for turns in range( NUM_TURNS ):
        
        #   PLAYER1

        # move player 1 and print status line
        player1 = monopoly_functions.move_player( player1, HIGHEST_SQUARE )
        monopoly_functions.display( "status", player1, player2 )
        
        this_property = []
        this_property = game_board[player1[SQUARE]]
        
        # check which square the player is on:
        # 0:  it's Go, add $200
        if ( this_property[NAME] == "Go" ):
            player1[MONEY] += GO_MONEY
            print()
            print( player1[NAME], "<--", GO_MONEY )
            print()
        # 1 - 3: if unowned, buy the property; otherwise, pay the other player the property's rent value
        elif ( this_property[OWNER] == NOT_OWNED ):
            #buy it
            player1[MONEY] = player1[MONEY] - this_property[PRICE]
            this_property[OWNER] = player1[NAME]
            print()
            print( f' {player1[NAME]} <-- {this_property[NAME]}' )
            print()
        elif ( this_property[OWNER] == player2[NAME] ):
            #pay rent
            player1[MONEY] = player1[MONEY] - this_property[RENT]
            player2[MONEY] = player2[MONEY] + this_property[RENT]
            print()
            print( f' {player1[NAME]} \t\t${this_property[RENT]} -->  {player2[NAME]}' )
            print()
        else: # player1 must own it
            pass
        #if
        
        #   PLAYER2

        # move player 2 and print status line
        player2 = monopoly_functions.move_player( player2, HIGHEST_SQUARE )
        monopoly_functions.display( "status", player1, player2 )
        
        this_property = []
        this_property = game_board[player2[SQUARE]]
        
        # check which square the player is on:
        # 0:  it's Go, add $200
        if ( this_property[NAME] == "Go" ):
            player2[MONEY] += GO_MONEY
            print()
            print( player2[NAME], "<--", GO_MONEY )
            print()
        # 1 - 3: if unowned, buy the property; otherwise, pay the other player the property's rent value
        elif ( this_property[OWNER] == NOT_OWNED ):
            #buy it
            player2[MONEY] = player2[MONEY] - this_property[PRICE]
            this_property[OWNER] = player2[NAME]
            print()
            print( f' {player2[NAME]} <-- {this_property[NAME]}' )
            print()
        elif ( this_property[OWNER] == player1[NAME] ):
            #pay rent
            player2[MONEY] = player2[MONEY] - this_property[RENT]
            player1[MONEY] = player1[MONEY] + this_property[RENT]
            print()
            print( f' {player2[NAME]} \t\t${this_property[RENT]} -->  {player1[NAME]}' )
            print()
        else: # player1 must own it
            pass
        #if

            
    #for-in

    # print final status line
    print()
    monopoly_functions.display( "header", player1, player2 )
    monopoly_functions.display( "status", player1, player2 )

    # End Program

# Function firstFunction()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def firstFunction ():

    # Declare Local Variable types (NOT parameters)

    print ( "firstFunction" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function firstFunction()

if ( __name__ == "__main__" ):
    main()
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
