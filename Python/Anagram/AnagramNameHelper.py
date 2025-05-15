from math import perm
from optparse import Values
import PySimpleGUI as sg
from sympy import false, true
import bisect
from itertools import permutations
import random
from random import randint

default_theme="DarkBlue"

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

def convert(s):
    #Introduce spaces into the string
    str1=" " 

    return(str1.join(s))

def find_index(elements, value):
    index = bisect.bisect_left(elements, value)
    if index < len(elements) and elements[index] == value:
        return index

def anagram_check():
    str1=values[0].lower()
    str2=values[1].lower()
    if len(str1)==0:
        window['-OUT-'].update("Word 1 is empty")

    elif len(str2)==0:
        window['-OUT-'].update("Word 2 is empty")

    elif(len(str1) == len(str2)):
    
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
    
        if(sorted_str1 == sorted_str2):
            window['-OUT-'].update(values[0]+ " and "+values[1] +" are an anagram")

        else:
            window['-OUT-'].update(values[0]+ " and "+values[1] +" are not an anagram")

    else:
        window['-OUT-'].update(values[0]+ " and "+values[1] +" are not same length -> not an anagram")

def letter_check():


        str1=values[0].lower()
        str2=values[1].lower()  
        i=0
        error=0
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

        if len(sorted_str1) == len(sorted_str2) or len(sorted_str1) > len(sorted_str2):
            for i in range(len(sorted_str2)):
                index=find_index(sorted_str1, sorted_str2[i])
                if index != None:
                    del(sorted_str1[index])     
                else: 
                    error=1
                    break                    

            s=convert(sorted_str1)

            if error==1:
                window['-OUT-'].update(values[0]+ " and "+values[1] +" are not same length -> not an anagram")
                window['-LET-'].update("1 letter used too much: "  + sorted_str2[i])  
            elif error==0:
                if len(s)==0:
                    window['-LET-'].update("All letters used")
                    anagram_check()
                else:
                    window['-OUT-'].update(values[0]+ " and "+values[1] +" are not same length -> not an anagram")
                    window['-LET-'].update("Still available characters: " + s)

        else:
            window['-OUT-'].update(values[0]+ " and "+values[1] +" are not same length -> not an anagram")
            window['-LET-'].update("Too many characters in 2nd word")

def random_perms():
    str1=values[0].lower()
    global perms
    if len(str1)<7:
        window['-PERM-'].update(sorted(perms))
    else:
        k=200
        permsl=random.sample(perms,k)
        permssort=quicksort(permsl)
        window['-PERM-'].update(permssort)
    
def run_once(f):
    def wrapper(*args, **kwargs):
        if wrapper.has_run != values[0].lower():
            wrapper.has_run = values[0].lower()
            ##print("1")
            return f(*args, **kwargs)

        else:
            random_perms()
    wrapper.has_run = ""
    
    return wrapper

@run_once
def create_perm():
    str1=values[0].lower()
    global perms
    perms=set([''.join(s) for s in permutations(str1)])
    ##print(len(perms))
    random_perms()

   


sg.theme(default_theme)  
#How the window should looke like.
layout = [  [sg.Text('Please enter 2 Words')],
            [sg.Text('Word 1'), sg.InputText()],
            [sg.Text('Word 2'), sg.InputText()],
            [sg.Text(auto_size_text=true, key='-OUT-')],
            [sg.Text(auto_size_text=true, key='-LET-')],
            #[sg.Listbox(values="",auto_size_text=true,expand_x=true, size=(100,20), key='-PERM-')],
            [sg.Multiline(key="-PERM-", size=(70,10))],
            [sg.Button('Anagram'), sg.Button('Letters'),sg.Button('Create Permutation',tooltip='Creates permutations of Word 1'), sg.Button('Exit')]
                ]



#Create the Window
window = sg.Window('Anagram Name Helper', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'Anagram':
        anagram_check()
        
    elif event == 'Letters':    
        letter_check()

    elif event == 'Create Permutation':
        create_perm()

window.close()




