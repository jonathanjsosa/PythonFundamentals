import sys
import math

def calcSquareArea():
    print('##### SQUARE AREA #####')
    side = float(input('Please enter the size of the square side: '))
    squareArea = side ** 2
    print(f'\nSquare area is {squareArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Exit.')
    functionState = 'square'
    nextAction(functionState)

def calcRentangleArea():
    print('##### RECTANGLE AREA #####')
    length = float(input('Please enter the length of the rectangle: '))
    width = float(input('Please enter the width of the rectangle: '))
    rectangleArea = length * width
    print(f'\nRectangle area is {rectangleArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Exit.')
    functionState = 'rectangle'
    nextAction(functionState)

def calcTriangleArea():
    print('##### TRIANGLE AREA #####')
    length = float(input('Please enter the length of the rectangle: '))
    base = float(input('Please enter the width of the rectangle: '))
    triangleArea = (length * base) / 2
    print(f'\nTriangle area is {triangleArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Exit.')
    functionState = 'triangle'
    nextAction(functionState)

def calcCircleArea():
    print('##### CIRCLE AREA #####')
    radius = float(input('Please enter the circle radius: '))
    circleArea = math.pi * (math.pow(radius, 2))
    print(f'\nCircle area is {circleArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Exit.')
    functionState = 'circle'
    nextAction(functionState)

def nextAction(functionState):
    userSelection = int(input('Please choose an option: '))
    afterCalcArea(userSelection, functionState)

def afterCalcArea(userSelection,functionState):
    if userSelection == 1:
        if functionState == 'square':
            calcSquareArea()
        elif functionState == 'rectangle':
            calcRentangleArea()
        elif functionState == 'triangle':
            calcTriangleArea()
        elif functionState == 'circle':
            calcCircleArea()
    elif userSelection == 2:
        initApp()
    elif userSelection == 3:
        print("Bye")
        sys.exit()
    else:
        while True:
            userSelection = int(input('Non-valid option. Please choose a valid option: '))
            afterCalcArea(userSelection, functionState)

def menuApp(userSelection):
    if userSelection == 1:
        calcSquareArea()
    elif userSelection == 2:
        calcRentangleArea()
    elif userSelection == 3:
        calcTriangleArea()
    elif userSelection == 4:
        calcCircleArea()
    elif userSelection == 5:
        print('Bye')
        sys.exit()
    else:
        return

def initApp():
    while True:
        print('Which figure would you like to calculate its area from?')
        print('\t1) Square\n\t2) Rectangle\n\t3) Triangle\n\t4) Circle\n\t5) None (Exit).\n')
        userSelection = int(input('Please choose an option: '))
        menuApp(userSelection)
        while True:
            userSelection = int(input('Non-valid option. Please choose a valid option: '))
            menuApp(userSelection)

initApp()
