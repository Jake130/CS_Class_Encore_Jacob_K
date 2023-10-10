def list_is_large(li:list[int])->bool:
    if len(li) >= 10:
        return True
    else:
        return False

print("\n____Number_1____\n")
print(list_is_large([1, 2, 3]))
print(list_is_large([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(list_is_large([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))




prime_numbers = [1, 2, 3, 5, 7]
even_numbers = [2, 4, 6, 8, 10]
def doubleOdd(numbers:list[int])->list[int]:
    other_list = []
    for number in numbers:
        if number % 2 == 1:
            number = number * 2
        other_list.append(number)
    return other_list

print("\n____Number_2____\n")
print(doubleOdd(prime_numbers))
print(doubleOdd(even_numbers))





safeway_list = ["apples", "bananas", "yogurt", "oranges", "kale", "zucchini"]
no_vegetables = ["kale", "zucchini"]
def removeGroceries(groceries:list[str], removed:list[str])->list[str]:
    new_list = []
    for item in groceries:
        if item not in removed:
            new_list.append(item)
    return new_list

print("\n____Number_3____\n")
print(removeGroceries(safeway_list, no_vegetables))
print(removeGroceries(safeway_list, []))
print(removeGroceries(safeway_list, safeway_list))




names = ["Amanda", "Lily", "Kailee", "John", "Joe", "Billy"]
playerscores = {"Lily" : 2500, 
                "Kailee" : 1300,
                "Billy" : 250,
                "John" : 500,
                "Joe" : 1000,
                "Amanda" : 1100}

def highscore(players:list[str], scores:dict[str:int])->str:
    max_score = 0
    for name in players:
        if name in scores:
            if scores[name] > max_score:
                max_score = scores[name]
    for name in players:
        if scores[name] == max_score:
            return name

print("\n____Number_4____\n")
print(highscore(names, playerscores))
