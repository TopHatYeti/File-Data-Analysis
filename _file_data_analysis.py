'''Spencer Schill, SDEV300
This project uses pandas to read a set of data from an excel sheet
and uses matplotlib to graph the data from the excel sheets and print a graph of the data'''

import pandas as pd
import matplotlib.pyplot as plt

def popChange(sub_option):                          #PopChange method
    df = pd.read_csv('PopChange.csv')               #reads PopChange.csv in project folder

    if sub_option == 'a':                           #menu options for PopChange
        print("You selected Pop Apr 1")
        column = df['Pop Apr 1']
    elif sub_option == 'b':
        print("You selected Pop Jul 1")
        column = df['Pop Jul 1']
    else:
        print("You selected Change pop")
        column = df['Change Pop']


    #prints the statistics for PopChange

    print(f'''Count = {column.count():.1f} \nMean = {column.mean():.1f} \nStandard Deviation = {column.std():.1f}
    \nMin = {column.min():.1f}\nMax = {column.max():.1f}''')
    print('The Histogram of this column is now displayed.')

                        #make histogram
    n, bins, patches = plt.hist(column, 40, density=True, facecolor='b',alpha=0.75)

    plt.grid(True)
                    #Assign to a grid
    fig=plt
                    #Save figure in folder where program is
    fig.savefig(f'popchange-{sub_option}.png')

def Housing(sub_option):                    #Housing method
    df = pd.read_csv('Housing.csv')         #read Housing.csv in project folder

    if sub_option == 'a':                   #menu options for Housing
        print('You selected Age')
        column = df['AGE']
    elif sub_option == 'b':
        print('You selected BEDRMS')
        column = df['BEDRMS']
    elif sub_option == 'c':
        print('You selected BUILT')
        column = df['BUILT']
    elif sub_option == 'd':
        print('You selected ROOMS')
        column = df['ROOMS']
    else:
        print('You selected UTILITY')
        column = df['UTILITY']

        #Print the statistics for Housing

    print(
        f'''Count = {column.count():.1f} \nMean = {column.mean():.1f} \nStandard Deviation = {column.std():.1f}
        \nMin = {column.min():.1f}\nMax = {column.max():.1f}''')
    print('The Histogram of this column is now displayed.')

                    #make histogram
    n, bins, patches = plt.hist(column, 10, density=True, facecolor='b', alpha=0.75)
    plt.grid(True)
                    #assign hist to grid
    fig = plt
                    #save figure in folder where program is
    fig.savefig(f'housing-{sub_option}.png')



#Main program
if __name__ == "__main__":
    print("------- Welcome to the Python Data Analysis App --------")
    while (True):                                               #while loop menu
        print("1. Population data")
        print("2. Housing Data")
        print("3. Exit the program")
        main_option = int(input("Select the file you want to analyze: "))            #user input option
        if main_option == 3:
            print("Thank you for using the python analysis program")                    #break if user wants to exit
            break
        if main_option == 1:                            #PopChange menu
            while (True):
                print("a. Pop Apr 1")
                print("b. Pop Jul 1")
                print("c. Change Pop")
                print("d. Exit Column")
                sub_option = input("Select the column you want to analyze: ")
                if sub_option.lower() == 'd':
                    print('You selected to exit the column menu')
                    break
                if sub_option.lower() in ['a', 'b', 'c']:
                    popChange(sub_option)
                else:
                    print('Please select from one of the menu items')
        if main_option == 2:                                            #Housing menu
            while (True):
                print("a. AGE")
                print("b. BEDRMS")
                print("c. BUILT")
                print("d. ROOMS")
                print("e. UTILITY")
                print("f. Exit Column")
                sub_option = input("Select the Column you want to analyze: ")
                if sub_option.lower() == 'f':
                    print('You selected to exit the column menu')
                    break
                if sub_option.lower() in ['a', 'b', 'c', 'd', 'e']:
                    Housing(sub_option)
                else:                                                       #if user inputs option not on menu
                    print('Please select from one of the menu items')

        else:                                                               #if user inputs option not on menu
            print('Please select from one of the menu items ')
