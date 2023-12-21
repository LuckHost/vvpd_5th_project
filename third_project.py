"""The third project
by Ходыкин Александр"""
def selection_sort(arr):
    """ sorts by choise 
    
    the simplest sort method
    Iterates through the elements of each array, comparing them and swapping them
    
    Args:
    --------
    arr : list 
        the array to be sorted
        
    Returns:
    --------
    arr : list
        sorted array
        
    Raises:
    --------
    None
    
    Examples:
    --------
    >> selection_sort([1, 3, 2])
    [1, 2, 3]
     
    """
    arr_lenght = len(arr)
    for i in range(arr_lenght):
        min_index = i
        for j in range(i+1, arr_lenght):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def menu_function():
    """ visual component 
    
    accepts the action number from the user
    
    Args:
    --------
    None
        
    Returns:
    --------
    inp : int
        
    Raises:
    --------
    ValueError
    
    Examples:
    --------
    >> menu_function()
    1
    """
    str_menu = "Введите номер действия:\n\
        0 - ввести массив и отсортировать его\n\
        1 - выйти из программы"
    inp = input(str_menu)
    try:
        return int(inp)
    except ValueError:
        return None


def main():
    """ the main function 
    
    The main function of the program.
    Loops the program, starts working again if the input is incorrect.
    
    Args:
    --------
    None
        
    Returns:
    --------
    None
        
    Raises:
    --------
    ValueError
    
    Examples:
    --------
    >> main()
    Здравствуйте!
    Эта программа -сортировщик массивов
    Введите номер действия:
        0 - ввести массив и отсортировать его
        1 - выйти из программы1
    Работа завершена
    
    """
    print("Здравствуйте!\n",
              "Эта программа -сортировщик массивов")
    while True:
        task = menu_function()
        if task == 1:
            print("Работа завершена")
            break
        if task == 0:
            try:
                arr = list(map(int,
                               input("Введите массив через пробел ").split()))
            except ValueError:
                print("Ввод инкорректен")
                continue
            result = selection_sort(arr)
            print("Отсортированный массив: ", result)
            continue
        print("Попробуйте еще раз..")

if __name__ == "__main__":
    main()
