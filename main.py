# Import the required libraries  
import pygame  
import pygame_menu  
  
customTheme = pygame_menu.Theme(background_color=(0, 0, 0), widget_font_color=(255,255,255)) 
backgroundImage1 = pygame_menu.baseimage.BaseImage( 
    image_path="cinema bg MAIN IMG.jpg", 
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL 
) 
customTheme.background_color = backgroundImage1 
 
customTheme2 = pygame_menu.Theme(background_color=(0, 0, 0), widget_font_color=(255,255,255)) 
backgroundImage2 = pygame_menu.baseimage.BaseImage( 
    image_path="sg cinema map.jpg", 
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL 
) 
customTheme2.background_color = backgroundImage2 
 
 
 
# Initialize pygame  
pygame.init()  
surface = pygame.display.set_mode((600, 400))  
  
# Make Shaw menu  
Shaw = pygame_menu.Menu('Shaw', 600, 400, theme=customTheme)  
 
# Make GV menu   
GV = pygame_menu.Menu('GV', 600, 400, theme=customTheme)  
  
# Make Eng Wah menu   
EngWah = pygame_menu.Menu('Eng Wah', 600, 400, theme=customTheme)  
 
# Make Cathay menu   
Cathay = pygame_menu.Menu('Cathay', 600, 400, theme=customTheme)  
 
# Make Map menu   
Map = pygame_menu.Menu('Map', 600, 400, theme=customTheme2)  
 
# Make main menu  
menu = pygame_menu.Menu('Welcome', 600, 400, theme=customTheme)  
menu.add.button('Shaw', Shaw)  
menu.add.button('GV', GV) 
menu.add.button('Eng Wah', EngWah) 
menu.add.button('Cathay', Cathay) 
menu.add.button('Map', Map) 
 
menu.add.button('Quit', pygame_menu.events.EXIT)  
 
 
 
PricesGV = pygame_menu.Menu('Prices GV', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
PricesGV.add.label('''standard adult: $10 
Fri-sun and public holiday: $14.50       
mon-thurs (before 6pm) students: $7    
mon-thurs (before 6pm) seniors: $5''', font_size = 20)   
GV.add.button('Prices GV', PricesGV) 
 
PricesGVGold = pygame_menu.Menu('Prices GV Gold', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
PricesGVGold.add.label('''mon-wed : before 5pm $29 after 5 $32 
thurs-sun + public holiday: $42''', font_size=20)   
GV.add.button('Prices GV Gold', PricesGVGold) 
 
VenuesGV = pygame_menu.Menu('Venues GV', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
VenuesGV.add.label('''Paya Lebar 
Jurong Point 
City Square 
Bishan 
Tampines 
Tiong Bahru 
Vivo City 
Yishun''', font_size=15)    
GV.add.button('Venues GV', VenuesGV) 
 
VenuesGVGold = pygame_menu.Menu('Venues GV Gold', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
VenuesGVGold.add.label('''Funan 
Katong 
Suntec 
Vivo City 
Great World City''', font_size=20)   
GV.add.button('Venues GV Gold', VenuesGVGold) 
 
WhyGV = pygame_menu.Menu('Why GV', 600 , 400, theme=customTheme)  
#(screen to draw on).add.button(‘Text’, screen to change to when button press)  
WhyGV.add.label('''More venues 
Promotion for students and senior citizens 
Variety of screening choice''', font_size=20) 
GV.add.button('Why GV', WhyGV) 
 
 
PricesShawiMax = pygame_menu.Menu('Prices Shaw iMax', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
PricesShawiMax.add.label('''mon to thurs: $9 
friday to sunday + public holidays: $14.50  
mon-thurs (before 6pm) students: $7                    
mon-thurs (before 6pm) seniors: $4.50 
mon to thurs: $17 
friday to sunday + public holidays: $19 
monday to thursday (before 6pm) students & seniors: $12 
friday to sunday (before 6pm) students & seniors: $15''', font_size=12) 
Shaw.add.button('Prices Shaw iMax', PricesShawiMax) 
 
PricesShaw = pygame_menu.Menu('Prices Shaw', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
PricesShaw.add.label('''mon to thurs: $9 
friday to sunday + public holidays: $14.50  
mon-thurs (before 6pm) students: $7                    
mon-thurs (before 6pm) seniors: $4.50 
mon to thurs:
$17 
friday to sunday + public holidays: $19 
monday to thursday (before 6pm) students & seniors: $12 
friday to sunday (before 6pm) students & seniors: $15''', font_size=12) 
Shaw.add.button('Prices Shaw', PricesShaw) 
 
 
VenuesShaw = pygame_menu.Menu('Venues Shaw', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
VenuesShaw.add.label('''Lido 
Jewel 
Paya Lebar Quarter 
Waterway Point 
Nex 
Seletar 
Jcube 
Lot One''', font_size=15) 
Shaw.add.button('Venues Shaw', VenuesShaw) 
 
WhyShaw = pygame_menu.Menu('Why Shaw', 600 , 400, theme=customTheme)  
#(screen to draw on).add.button(‘Text’, screen to change to when button press)  
WhyShaw.add.label('''Promotion for students and senior citizens 
imax availble 
many venues''' , font_size=20) 
Shaw.add.button('Why Shaw', WhyShaw) 
 
 
 
PricesCathay = pygame_menu.Menu('Prices Cathay', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
PricesCathay.add.label('''weekdays: $10 
weekends: $14.50 
weekdays before 6pm for students: $7 
weekdays before 6pm for seniors: $5''',font_size=20)     
Cathay.add.button('Prices Cathay', PricesCathay) 
 
VenuesCathay = pygame_menu.Menu('Venues Cathay', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
VenuesCathay.add.label('''Causeway Point 
The Cathay 
AMK Hub 
West Mall 
Downtown East 
Jem 
Parkway Parade 
Cineleisure Orchard''', font_size=15) 
Cathay.add.button('Venues Cathay', VenuesCathay) 
 
WhyCathay = pygame_menu.Menu('Why Cathay', 600 , 400, theme=customTheme)  
#(screen to draw on).add.button(‘Text’, screen to change to when button press)  
WhyCathay.add.label('''Promotion for students and senior citizens 
more venues options''', font_size=20) 
Cathay.add.button('Why Cathtay', WhyCathay) 
 
 
PricesEngWah = pygame_menu.Menu('Prices Eng Wah', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
PricesEngWah.add.label('''Mon-thurs: $9.50 
Fri-sun: $14.50 
Student before 6pm: $7 
Senior before 6pm: $4.50''', font_size=20)   
EngWah.add.button('Prices Eng Wah', PricesEngWah) 
 
VenuesEngWah = pygame_menu.Menu('Venues Eng Wah', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
VenuesEngWah.add.label('321 Clementi' , font_size=20) 
EngWah.add.button('Venues Eng Wah', VenuesEngWah) 
 
WhyEngWah = pygame_menu.Menu('Why Eng Wah', 600 , 400, theme=customTheme)  
#(screen to draw on).add.button(‘Text’, screen to change to when button press)  
WhyEngWah.add.label('''Promotion for students and senior citizens 
Cheapest prices for senior citizens 
$1 off for UOB/Standard Chartered/Citibank credit cardholders''', font_size=20) 
EngWah.add.button('Why Eng Wah', WhyEngWah) 
 
 
 
 
 
 
  
 
# Run your menu  
menu.mainloop(surface)
