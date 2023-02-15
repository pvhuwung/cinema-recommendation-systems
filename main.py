# Import the required libraries  
import pygame  
import pygame_menu  
  
customTheme = pygame_menu.Theme(background_color=(0, 0, 0), widget_font_color=(255,232 ,131)) 
backgroundImage1 = pygame_menu.baseimage.BaseImage( 
    image_path="cinema bg MAIN IMG.jpg", 
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL 
) 
customTheme.background_color = backgroundImage1 
 
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
Map = pygame_menu.Menu('Map', 600, 400, theme=customTheme)  
 
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
Text =''' insert 
Text 
here''' 
GV.add.button('Prices GV', PricesGV) 
 
PricesGVGold = pygame_menu.Menu('Prices GV Gold', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
GV.add.button('Prices GV Gold', PricesGVGold) 
 
VenuesGV = pygame_menu.Menu('Venues GV', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
GV.add.button('Venues GV', VenuesGV) 
 
VenuesGVGold = pygame_menu.Menu('Venues GV Gold', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
GV.add.button('Venues GV Gold', VenuesGVGold) 
 
 
PricesShawiMax = pygame_menu.Menu('Prices Shaw iMax', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
Shaw.add.button('Prices Shaw iMax', PricesShawiMax) 
 
PricesShaw = pygame_menu.Menu('Prices Shaw', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
Shaw.add.button('Prices Shaw', PricesShaw) 
 
 
VenuesShaw = pygame_menu.Menu('Venues Shaw', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
Shaw.add.button('Venues Shaw', VenuesShaw) 
 
 
PricesCathay = pygame_menu.Menu('Prices Cathay', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
Cathay.add.button('Prices Cathay', PricesCathay) 
 
VenuesCathay = pygame_menu.Menu('Venues Cathay', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
Cathay.add.button('Venues Cathay', VenuesCathay) 
 
 
PricesEngWah = pygame_menu.Menu('Prices Eng Wah', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
EngWah.add.button('Prices Eng Wah', PricesEngWah) 
 
VenuesEngWah = pygame_menu.Menu('Venues Eng Wah', 600 , 400, theme=customTheme) 
#(screen to draw on).add.button(‘Text’, screen to change to when button press) 
Text =''' insert 
Text 
here''' 
EngWah.add.button('Venues Eng Wah', VenuesEngWah) 
 
 
 
PricesGV.add.label('standard adult: $10', font_size=20) 
PricesGV.add.label('friday to sunday + public holidays: $14.50', font_size=20) 
PricesGV.add.label('mon-thurs (before 6pm) students: $7', font_size=20)
PricesGV.add.label('mon-thurs(before 6pm) seniors: $5', font_size=20) 
 
PricesGVGold.add.label('mon-wed : before 5pm $29 after 5 $32', font_size=20) 
PricesGVGold.add.label('thurs-sun + public holiday: $42', font_size=20) 
 
VenuesGV.add.label('Paya Lebar', font_size=20) 
VenuesGV.add.label('Jurong Point', font_size=20) 
VenuesGV.add.label('City Square', font_size=20) 
VenuesGV.add.label('Bishan', font_size=20) 
VenuesGV.add.label('Tampines', font_size=20) 
VenuesGV.add.label('Tiong Bahru', font_size=20) 
VenuesGV.add.label('Vivo City', font_size=20) 
VenuesGV.add.label('Yishun', font_size=20) 
 
VenuesGVGold.add.label('Funan', font_size=20) 
VenuesGVGold.add.label('Katong', font_size=20) 
VenuesGVGold.add.label('Suntec', font_size=20) 
VenuesGVGold.add.label('Vivo City', font_size=20) 
VenuesGVGold.add.label('Great World City', font_size=20) 
 
 
 
 
PricesEngWah.add.label('Mon-thurs: $9.50', font_size=20) 
PricesEngWah.add.label('Fri-sun: $14.50', font_size=20) 
PricesEngWah.add.label('Student before 6pm: $7', font_size=20) 
PricesEngWah.add.label('Senior before 6pm: $4.50', font_size=20) 
 
VenuesEngWah.add.label('321 Clementi' , font_size=20) 
 
 
 
 
PricesShaw.add.label('mon to thurs: $9', font_size=20)  
PricesShaw.add.label('friday to sunday + public holidays: $14.50', font_size=20)  
PricesShaw.add.label('mon-thurs (before 6pm) students: $7', font_size=20)  
PricesShaw.add.label('mon-thurs (before 6pm) seniors: $4.50', font_size=20) 
PricesShawiMax.add.label('mon to thurs: $17', font_size=20)  
PricesShawiMax.add.label('friday to sunday + public holidays: $19', font_size=20)  
PricesShawiMax.add.label('monday to thursday (before 6pm) students & seniors: $12', font_size=20)  
PricesShawiMax.add.label('friday to sunday (before 6pm) students & seniors: $15', font_size=20) 
 
 
 
VenuesShaw.add.label('Lido', font_size=20) 
VenuesShaw.add.label('Jewel', font_size=20) 
VenuesShaw.add.label('Paya Lebar Quarter', font_size=20) 
VenuesShaw.add.label('Waterway Point', font_size=20) 
VenuesShaw.add.label('Nex', font_size=20) 
VenuesShaw.add.label('Seletar', font_size=20) 
VenuesShaw.add.label('Jcube', font_size=20) 
VenuesShaw.add.label('Lot One', font_size=20) 
 
 
 
 
 
 
 
PricesCathay.add.label('weekdays : $10', font_size=20) 
PricesCathay.add.label('weekends : $14.50', font_size=20)  
PricesCathay.add.label('weekdays (before 6pm) students: $7', font_size=20) 
PricesCathay.add.label('weekdays (before 6pm) seniors: $5', font_size=20 
 
         
VenuesCathay.add.label('Causeway Point', font_size=20) 
VenuesCathay.add.label('The Cathay', font_size=20) 
VenuesCathay.add.label('AMK Hub', font_size=20) 
VenuesCathay.add.label('West Mall', font_size=20) 
VenuesCathay.add.label('Downtown East', font_size=20) 
VenuesCathay.add.label('Jem', font_size=20) 
VenuesCathay.add.label('Parkway Parade', font_size=20) 
VenuesCathay.add.label('Cineleisure Orchard', font_size=20)
