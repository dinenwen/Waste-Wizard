def main():
    global city
    city = input ('Choose your city: San Francisco, Oakland, Portland')
    city = city.upper()
    print ('Okay you are in ', city, '!')
    item = input ('The program will tell you how to sort your trash based on your city. Inspect your trash and type the material that it most resembles. Type one of the following: Paper, Cardboard, Plastic, Food, Aluminium, TetraPak, Juice Box, Other Metal, Battery, Electronic Waste, Automotive Fluids, Cooking Oil, Grey Water, Cork, Textile, Durable')
    item = item.upper()
    items(item)
    nextItem(item)
    
def items(item):
    if item == 'PAPER' or item == 'CARDBOARD':
        qu = input('Is the paper clean? Enter yes or no') 
        if qu == "yes" or qu == "y" and item == 'CARDBOARD':
            print('RECYCLE  your ' , item , ' in the blue bin!')
            nextItem(item)
        elif qu =='no' or qu =='n' and item == 'CARDBOARD':
            print ('COMPOST your ',item,'in the green bin!')
            nextItem(item)
        elif qu =='yes' or qu =='y':
            qu = input('Can you rip the paper?')
            if qu == "yes" or qu == "y":
                print ('RECYCLE  your ' , item , ' in the blue bin!')
                nextItem(item)
            elif qu == "no" or qu == "n":
                print('Oh no your ', item , ' is LANDFILL. Put it in the black bin.')
                nextItem(item)
        elif qu == "no" or qu == "n":
            print('COMPOST  your ' , item , ' in the green bin!')
            nextItem(item)

    elif item == 'GLASS':
        print ('RECYCLE  your ' , item , ' in the blue bin!')
        nextItem(item)

    elif item == 'TETRAPAK' or item == 'JUICE BOX':
        print ('Oh no, your',item,'is LANDFILL in',city,'.')
        nextItem(item)
               
    elif item == 'PLASTIC':
        qu = input ('Is this a hard plastic? Enter yes or no')
        if qu == "yes" or qu == "y":
            qu = input('Does your plastic item say the word COMPOSTABLE anywhere on it? Check the sides and the bottom!')
            if qu == 'yes' and city!='PORTLAND' or qu == 'y' and city != 'PORTLAND':
                print ('Your item is made from a COMPOSTABLE BIOPLASTIC. Put it in the green bin!')
                nextItem(item)
            elif qu == 'no' or qu == 'n':    
                resinCode = input ('Enter the number 1-7 printed on the bottom. This is called a Resin Code')
                if city == 'OAKLAND' or city == 'SAN FRANCISCO':
                    print ('RECYCLE your #',resinCode,' ',item,' in the blue bin!')
                    nextItem(item)
                elif city == 'PORTLAND' and resinCode != '6' and resinCode !='7':
                    print ('RECYCLE your #',resinCode,' ',item,' in the blue bin!')
                    nextItem(item)
                elif city == 'PORTLAND' and resinCode == '6' or city == 'PORTLAND' and resinCode == '7':
                    print ('Oh no, #',resinCode,item,' is LANDFILL in ',city,'. Put it in the black bin.')
                    nextItem(item)
        elif qu == "no" or qu == "n":
            print('Oh no your SOFT', item, ' is LANDFILL. Put it in the black bin!')
            qu = input('Alternatively would you like to see some alternate diversion suggestions for soft plastics?')
            if qu == "yes" or qu == "y":
                print ('List of RECYCLE options for SOFT PLASTIC')
                nextItem(item)
            elif qu == "no" or qu == "n":
                print ('LANDFILL or take to your preferred RECYCLE center')
                nextItem(item)
                
    elif item == 'FOOD':
        qu = input('Is the food Still edible. Choose yes or no')
        if qu == "yes" or qu == "y":
            qu = input('We recommend donating to a local organization. Would you like to see a list of organizations in your area accepting donations?')
            if qu == "yes" or qu == "y":
                print('List of organizations accepting donations')
                nextItem(item)
            elif qu == "no" or qu == "n":
                print ('COMPOST  your ' , item , ' in the green bin!')
                nextItem(item)
        elif qu == "no" or qu == "n":
            print ('COMPOST  your ' , item , ' in the green bin!')
            nextItem(item)

    elif item == 'ALUMINIUM' or item == 'ALUMINIUM CAN' or item == 'ALUMINIUM FOIL' or item == 'FOIL':
        print ('RECYCLE  your ' , item , ' in the blue bin!')
        nextItem(item)

    elif item == 'OTHER METAL':
        print ('RECYCLE  your ' , item , ' in the blue bin!')
        nextItem(item)

    elif item == 'BATTERY':
        qu = input('Your battery cannot be disposed of at this station. It is considered toxic waste. Would you like to see a list of nearby facilities that will accept used batteries?')
        if qu == "yes" or qu == "y":
            print ('List of nearby facilities that RECYCLE batteries')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please take to your preffered battery RECYCLE center')
            nextItem(item)

    elif item == 'ELECTRONIC WASTE' or item == 'E-WASTE':
        qu = input('Your electronic waste cannot be disposed of at this station. It is considered toxic waste. Would you like to see a list of nearby facilities that will RECYCLE e-waste?')
        if qu == "yes" or qu == "y":
            print ('List of nearby facilities that RECYCLE electronic waste')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please take to your preffered electronic waste RECYCLE center')
            nextItem(item)

    elif item == 'PAINT':
        qu = input('Your paint cannot be disposed of at this station. It is considered toxic waste. Would you like to see a list of nearby facilities that will accept used batteries?')
        if qu == "yes" or qu == "y":
            print ('List of nearby facilities that RECYCLE paint')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please take to your preffered paint RECYCLE or disposal center')
            nextItem(item)
            
    elif item == 'AUTOMOTIVE FLUIDS' or item == 'MOTOR OIL':
        qu = input('Would you like to see a list of nearby places that accept automotive fluids')
        if qu == "yes" or qu == "y":
            print ('List of nearby places that accept automotive fluids')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please take to your prefered automotive fluid disposal center')
            nextItem(item)
            
    elif item == 'COOKING OIL':
        qu = input('Did you know that cooking oil can be repurposed to make biodiesel? Would you like to see a list of nearby organizations that will accept or collect your used cooking oil?')
        if qu == "yes" or qu == "y":
            print ('List of nearby places that RECYCLE cooking oil')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please dispose of at your preferred oil collection facility')
            nextItem(item)
            
    elif item == 'GREY WATER':
        qu = input('Your water is contaminated and must be disposed of at a proper facility. Would you like to see a list of nearby facilities that accept grey water?')
        if qu == "yes" or qu == "y":
            print ('List of nearby facilties that accept grey water')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please dispose of at your preferred grey water disposal center')
            nextItem(item)
            
    elif item == 'CORK':
        qu = input('Does the cork appear to contain plastic?')
        if qu == "yes" or qu == "y":
            print ('Oh no, your',item, 'is LANDFILL. Please dispose of in black bin.')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print('COMPOST  your' ,item,'in the green bin! or return to a cork RECYCLE program.')
            qu = input('Would you like to see a list of cork RECYCLE programs in your location?')
            if qu == "yes" or qu == "y":
                print ('List of nearby facilities with cork recycling')
                nextItem(item)
            elif qu == "no" or qu == "n":
                print ('COMPOST your',item,' in the green bin!')
                nextItem(item)

    elif item == 'TEXTILE' or item == 'FABRIC':
        qu = input('Can the item be re-used or repurposed?')
        if qu == "yes" or qu == "y":
            qu = input('Would you like to see a list of nearby facilities that accept textiles?')
            if qu == "yes" or qu == "y":
                print ('List of nearby facilities that accept textiles')
                nextItem(item)
            elif qu == "no" or qu == "n":
                print ('Please take to your prefered thrift store or other textile recycling facility')
                nextItem(item)
        elif qu == "no" or qu == "n":                                    
            qu = input('Is the item 100% natural fibers such as cotton or hemp?')
            if qu == "yes" or qu == "y":
                print ('COMPOST your',item,'in the green bin!')
                nextItem(item)
            elif qu == "no" or qu == "n":
                print ('Oh no, your',item,'is LANDFILL. Please dispose of in black bin.')
                nextItem(item)

    elif item == 'DURABLE':
        qu = input('Your item can still be used. Hang on to it. or would you like to see a list of nearby facilties that accept durable items?')
        if qu == "yes" or qu == "y":
            print ('List of nearby facilities that accept durable items')
            nextItem(item)
        elif qu == "no" or qu == "n":
            print ('Please return at your preferred thrift store or other durable item donation center')
            nextItem(item)

    else:
        print ('Sorry we did not understand your selection.')
        nextItem(item)
            
def nextItem(item):
    qu = input('Would you like to check another item?')
    if qu == "yes" or qu == "y":
        item = input ('Enter your next item')
        item = item.upper()
        items(item)
    elif qu == "no" or qu == "n": 
        qu = input('Thank you for using Waste Wizard. Sorting your trash reduces your ecological foott dont forget to choose durable items whenever possible. Would you like to see more tips on reducing your waste impact?')
        if qu == "yes" or qu == "y":
            print ('More tips')
    elif qu == "no" or qu == "n":
        print ('Thanks have a nice day. The program will end now')
main()
