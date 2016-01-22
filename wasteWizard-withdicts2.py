def main():
    global city
    city = input ('Welcome to Waste Wizard. This program teaches you how to sort your trash based on your city. Choose your city: San Francisco, Oakland, Portland') 
    city = city.upper()
    print ('Okay you are in', city, '!'), 
    item = input ('Inspect your trash and type the name of the item or material that it most resembles. Here are some common choices: Paper, Cardboard, Plastic, Food, Aluminium Can , TetraPak, Juice Box, Hazardous, Textile, Durable')
    item = item.upper()
    items(item)
    nextItem(item)
    
def items(item):
    
    item_normalization = {
        'JUICE BOX': 'LANDFILL',
        'BOTTLE CAP': 'LANDFILL',
        'TETRAPAK': 'LANDFILL',
        'GLOVE': 'LANDFILL',
        'LATEX GLOVE': 'LANDFILL',
        'DISPOSABLE GLOVE': 'LANDFILL',
        'WRAPPER': 'LANDFILL',
        'BABY WIPE': 'LANDFILL',
        'SOFT PLASTIC': 'LANDFILL',
        
        'ALUMINUM FOIL': 'RECYCLE',
        'ALUMINUM CAN': 'RECYCLE',
        'FOIL': 'RECYCLE',
        'GLASS': 'RECYCLE',
        'SCRAP METAL': 'RECYCLE',
        'CLEAN PAPER': 'RECYCLE',

        'YARD TRIMMINGS': 'COMPOST',
        'GREEN WASTE': 'COMPOST',
        'FOOD SCRAPS': 'COMPOST',
        'BIOPLASTIC': 'COMPOST',
        'WOOD': 'COMPOST',
        'SKEWER': 'COMPOST',
                
        'ELECTRONIC WASTE': 'HAZARDOUS',
        'ELECTRONIC': 'HAZARDOUS',
        'EWASTE': 'HAZARDOUS',
        'GREY WATER': 'HAZARDOUS',
        'PAINT': 'HAZARDOUS',
        'AUTOMOTIVE FLUIDS': 'HAZARDOUS',
        'BATTERY': 'HAZARDOUS',
        'EWASTE':'HAZARDOUS',

        'NEEDLE': 'MEDICAL',
        'DIAPER': 'MEDICAL',
        'TAMPON': 'MEDICAL',
        'CONDOM': 'MEDICAL',
        'BAND AID': 'MEDICAL',
        'BANDAGE': 'MEDICAL',

        'CARDBOARD': 'PAPER',
        'TISSUE': 'PAPER',
        'NAPKIN': 'PAPER',}
    
    if item in item_normalization:
      normalized = item_normalization[item]
    else:
      normalized = item

    item_responses = {
        'RECYCLE': 'RECYCLE  your %(item)s in the blue bin!',
        'LANDFILL': 'Oh no, your %(item)s is LANDFILL in %(city)s.',
        'COMPOST': 'COMPOST your %(item)s in the green bin!',
        'MEDICAL': 'Your %(item)s is considered MEDICAL WASTE. Please place in seperate marked bag inside the LANDFILL BIN',
        }
    if normalized in item_responses:
       print(item_responses[normalized] % {'item':item, 'city':city})

    elif normalized == 'HAZARDOUS':
        qu = input('Oh no, your %(item)s is considered hazardous waste and cannot be disposed of at this station. Would you like to see a list of facilities in your area that will accept your %(item)s?' % {'item':item, 'city':city})
        if qu.startswith('y'):
            print('List of facilities in %(city)s that will recycle or otherwise properly dispose of your %(item)s' % {'item':item, 'city':city})
        else:
            print('Please dispose of at your preferred %(item)s disposal center' % {'item':item, 'city': city})
        
    elif normalized == 'PAPER':
        qu = input('Is the paper clean? Enter yes or no') 
        if qu.startswith('y') and item == 'CARDBOARD':
            print('RECYCLE  your ' , item , ' in the blue bin!')
        elif item == 'CARDBOARD':
            print ('COMPOST your ',item,'in the green bin!')
        elif qu.startswith('y'):
            qu = input('Can you rip the paper?')
            if qu.startswith('y'):
                print ('RECYCLE  your ' , item , ' in the blue bin!')
            else:
                print('Oh no your %(item)s is LANDFILL in %(city)s. Put it in the black bin.' % {'item':item, 'city': city})
        else:
            print('COMPOST  your ' , item , ' in the green bin!')
 
    elif item == 'PLASTIC':
        qu = input ('Is this a hard plastic? Enter yes or no')
        if qu.startswith('y'):
            qu = input('Does your plastic item say the word COMPOSTABLE anywhere on it? Check the sides and the bottom!')
            if qu.startswith('y') and city!='PORTLAND' or qu == 'y' and city != 'PORTLAND':
                print ('Your item is made from a COMPOSTABLE BIOPLASTIC. In %(city)s we can COMPOST it! Put it in the green bin!' %{'item': item, 'city': city})
            else:    
                resinCode = input ('Enter the number 1-7 printed on the bottom. This is called a Resin Code')
                if city == 'OAKLAND' or city == 'SAN FRANCISCO':
                    print ('RECYCLE your #',resinCode,' ',item,' in the blue bin!')
                elif city == 'PORTLAND' and resinCode != '6' and resinCode !='7':
                    print ('RECYCLE your #',resinCode,' ',item,' in the blue bin!')
                elif city == 'PORTLAND' and resinCode == '6' or city == 'PORTLAND' and resinCode == '7':
                    print ('Oh no your %(item)s is LANDFILL in %(city)s. Put it in the black bin.' % {'item':item, 'city': city})
        else:
            print('Oh no your SOFT %(item)s is LANDFILL in %(city)s. Put it in the black bin.' % {'item':item, 'city': city})
            qu = input('Alternatively would you like to see some alternate diversion suggestions for soft plastics?')
            if qu.startswith('y'):
                print ('List of RECYCLE options for SOFT PLASTIC')
            else:
                print ('LANDFILL or take to your preferred RECYCLE center')
                
    elif item == 'FOOD':
        qu = input('Is the food Still edible. Choose yes or no')
        if qu.startswith('y'):
            qu = input('We recommend donating to a local organization. Would you like to see a list of organizations in your area accepting donations?')
            if qu.startswith('y'):
                print('List of organizations accepting donations')
            else:
                print ('COMPOST  your ' , item , ' in the green bin!')
        else:
            print ('COMPOST  your ' , item , ' in the green bin!')

    elif item == 'CORK':
        qu = input('Does the cork appear to contain plastic?')
        if qu.startswith('y'):
            print ('Oh no your %(item)s is LANDFILL in %(city)s. Put it in the black bin.' % {'item':item, 'city': city})
        else:
            print('COMPOST  your' ,item,'in the green bin! or return to a cork RECYCLE program.')
            qu = input('Would you like to see a list of cork RECYCLE programs in your location?')
            if qu.startswith('y'):
                print ('List of nearby facilities with cork recycling')
            else:
                print ('COMPOST your',item,' in the green bin!')

    elif item == 'TEXTILE' or item == 'FABRIC':
        qu = input('Can the item be re-used or repurposed?')
        if qu.startswith('y'):
            qu = input('Would you like to see a list of nearby facilities that accept textiles?')
            if qu.startswith('y'):
                print ('List of nearby facilities that accept textiles')
            else:
                print ('Please take to your prefered thrift store or other textile recycling facility')
        else:                                    
            qu = input('Is the item 100% natural fibers such as cotton or hemp?')
            if qu.startswith('y'):
                print ('COMPOST your',item,'in the green bin!')
            else:
                print ('Oh no your %(item)s is LANDFILL in %(city)s. Put it in the black bin.' % {'item':item, 'city': city}) 

    elif item == 'COOKING OIL':
        qu = input('Did you know that cooking oil can be repurposed to make biodiesel? Would you like to see a list of nearby organizations that will accept or collect your used cooking oil?')
        if qu.startswith('y'):
            print ('List of nearby places that RECYCLE cooking oil')
        else:
            print ('Please dispose of at your preferred oil collection facility')
            
    elif item == 'DURABLE':
        qu = input('Your item can still be used. Hang on to it. or would you like to see a list of nearby facilties that accept durable items?')
        if qu.startswith('y'):
            print ('List of nearby facilities that accept durable items')
        else:
            print ('Please return at your preferred thrift store or other durable item donation center')

    else:
        print ('Sorry we did not understand your selection.')

    nextItem(item)
            
def nextItem(item):
    qu = input('Would you like to check another item?')
    if qu.startswith('y'):
        item = input ('Enter your next item')
        item = item.upper()
        items(item)
    else: 
        qu = input('Thank you for using Waste Wizard. Sorting your trash reduces your ecological foott dont forget to choose durable items whenever possible. Would you like to see more tips on reducing your waste impact?')
        if qu.startswith('y'):
            print ('Tips')
        print ('Thanks have a nice day. The program will end')
        exit()
main()
