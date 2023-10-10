"""
Author: Jacob Kolster
Date: 10/10/2023
Class Encore Week 3, CS 210
"""

#Note that the provided data are below the comments so that you can reference them

def list_is_large(li:list[int])->bool:
    """Check whether the list has 10 or more elements
    
    list_is_large([1, 2, 3])
    >>>False
    list_is_large([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    >>>True
    list_is_large([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11])
    >>>True
    """

    return

def doubleOdd(numbers:list[int])->list[int]:
    """Return numbers after having doubled its odd numbers.
    DO NOT MAKE A COPY OF THIS LIST! INSTEAD MAKE CHANGES TO
    THE LIST IT AND THEN RETURN THAT SAME LIST (make an effect)
    
    doubleOdd(prime_numbers)
    >>>[2, 2, 6, 10, 14]
    
    doubleOdd(even_numbers)
    >>>[2, 4, 6, 8, 10]

    """
    prime_numbers = [1, 2, 3, 5, 7]
    even_numbers = [2, 4, 6, 8, 10]

    return



def removeGroceries(groceries:list[str], removed:list[str])->list[str]:
    """Groceries contains a list of groceries, removed contains
    a list of items that need to be removed from groceries. Return
    a list containing only the groceries that do not need to be removed so that...
    

    removeGroceries(safeway_list, no_vegetables)
    >>>[apples, bananas, yogurt, oranges]

    remove Groceries(safeway_list, [])
    >>>[apples, bananas, yogurt, oranges, kale, zucchini]

    remove Groceries(safeway_list, safeway_list)
    >>>[]
    
    """
    safeway_list = ["apples", "bananas", "yogurt", "oranges", "kale", "zucchini"]
    no_vegetables = ["kale", "zucchini"]
    
    
    return 

def highscore(scores:dict[str:int])->str:
    """Given a list of names and a dictionary 
    that maps names to scores. Use both these elements to
    return the name of the person with the highest score.

    highscore(names, playerscores)
    >>>"Lily"

    """
    names = ["Amanda", "Lily", "Kailee", "John", "Joe", "Billy"]
    playerscores = {"Lily" : 2500, 
                    "Kailee" : 1300,
                    "Billy" : 250,
                    "John" : 500,
                    "Joe" : "1000",
                    "Amanda" : 1100}
    
    
    return
