import pygame
from sys import exit
from data import data_planet

pygame.init()

HEIGHT, WIDTH = 500, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interstellar")
FRAME = pygame.time.Clock()

image_background = pygame.image.load('./assets/Background.jpg')
BG = pygame.transform.scale(image_background, (WIDTH, HEIGHT))
current_page = "welcome"
wiki_index = 0
ARROW_HEIGHT, ARROW_WIDTH = 30, 20
PANEL_WIDTH, PANEL_HEIGHT = 300, 300
MARGIN = 20

# Game Variable
username = 'Masukkan nama'

def display_text(text, size, color):
    FONT = pygame.font.Font('./assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf', size)
    return FONT.render(text, False, color)

def panel_text(text, font_size, color, max_width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if current_line:
            test_line = ' '.join(current_line + [word])
        else:
            test_line = word

        line_width = pygame.font.Font('./assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf', font_size).size(test_line)[0]

        if line_width <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))
    return lines


def draw_panel_text(text_lines, font_size, color, position, line_spacing):
    font = pygame.font.Font('./assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf', font_size)
    line_height = font.get_linesize()

    for i, line in enumerate(text_lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(topleft=(position[0], position[1] + i * (line_height + line_spacing)))
        SCREEN.blit(text_surface, text_rect)
        
def draw_panel_and_text(text, font_size, color, max_width, panel_position):
    panel_surface = pygame.image.load('./assets/misc/Panel.png')
    panel_surface = pygame.transform.scale(panel_surface, (PANEL_WIDTH, PANEL_HEIGHT))
    panel_rect = pygame.Rect(*panel_position, PANEL_WIDTH, PANEL_HEIGHT)
    SCREEN.blit(panel_surface, panel_rect)

    text_lines = panel_text(text, font_size, color, max_width)
    draw_panel_text(text_lines, font_size, color, (panel_rect.topleft[0] + MARGIN, panel_rect.topleft[1] + MARGIN), 6)

def welcome():
    # Display Text
    text_surface = display_text("Welcome To Interstellar", 24, "White")
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(text_surface, text_rect)
    
    # Display Text
    text_surface = display_text("Klik layar untuk mulai bermain >>", 12, "White")
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    SCREEN.blit(text_surface, text_rect)
    
def input_name():
    # Display Text
    text_surface = display_text("Siapa nama kamu?", 24, "White")
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75))
    SCREEN.blit(text_surface, text_rect)
    
    # Init Textbox
    input_rect = pygame.Rect(WIDTH // 2 - 200,text_rect.bottom + 20,400,40)
    color = 'white'
    
    # Render Textbox To Screen
    pygame.draw.rect(SCREEN, color, input_rect,2)
    
    # Render username
    SCREEN.blit(display_text(username, 20, "white"), (input_rect.x + 5, input_rect.y + 10))
    
    # Next Button
    button_width, button_height = 100, 40
    button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, input_rect.bottom + 20, button_width, button_height)
    button_color = 'white'

    # Draw the button with a white background
    pygame.draw.rect(SCREEN, button_color, button_rect)

    # Render button text
    button_text = display_text("Next", 20, "Black")  # You can adjust the text color
    button_text_rect = button_text.get_rect(center=button_rect.center)
    SCREEN.blit(button_text, button_text_rect)
    
    return button_rect

def main_menu():
    # Main menu button size
    BUTTON_WIDTH = 125
    BUTTON_HEIGHT = 65
    
    # Display username in menu
    text_surface = display_text("Hello, " + username + "!", 16, "White")
    text_rect = text_surface.get_rect(topleft=(10, 10))
    SCREEN.blit(text_surface, text_rect)
    
    # Display Main Menu Text
    main_menu_surface = display_text("MAIN MENU", 30, "White")
    main_menu_rect = main_menu_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    SCREEN.blit(main_menu_surface, main_menu_rect)
    
    # Wiki Button
    wiki_button_surface = pygame.image.load('./assets/buttons/WikiButton.png')
    wiki_button_surface = pygame.transform.scale(wiki_button_surface, (BUTTON_WIDTH, BUTTON_HEIGHT))
    wiki_button_rect = wiki_button_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2 + 20))
    SCREEN.blit(wiki_button_surface, wiki_button_rect)
    
    # Quiz Button
    quiz_button_surface = pygame.image.load('./assets/buttons/QuizButtons.png')
    quiz_button_surface = pygame.transform.scale(quiz_button_surface, (BUTTON_WIDTH, BUTTON_HEIGHT))
    quiz_button_rect = quiz_button_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    SCREEN.blit(quiz_button_surface, quiz_button_rect)
    
    # About Button
    about_button_surface = pygame.image.load('./assets/buttons/AboutButton.png')
    about_button_surface = pygame.transform.scale(about_button_surface, (BUTTON_WIDTH, BUTTON_HEIGHT))
    about_button_rect = about_button_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2 + 20))
    SCREEN.blit(about_button_surface, about_button_rect)
    
    return wiki_button_rect, quiz_button_rect, about_button_rect

def about():
    # Display username in menu
    text_surface = display_text("About", 24, "White")
    text_rect = text_surface.get_rect(midtop=(WIDTH // 2, 20))
    SCREEN.blit(text_surface, text_rect)
    
    # Home Button
    home_button_surface = pygame.image.load('./assets/buttons/HomeButton.png')
    home_button_surface = pygame.transform.scale(home_button_surface, (50, 50))
    home_button_rect = home_button_surface.get_rect(topleft=(20,20))
    SCREEN.blit(home_button_surface, home_button_rect)
    
    PANEL_WIDTH, PANEL_HEIGHT = 300, 150
    
    # Panel
    panel_surface = pygame.image.load('./assets/misc/Panel.png')
    panel_surface = pygame.transform.scale(panel_surface, (PANEL_WIDTH, PANEL_HEIGHT))
    panel_rect = pygame.Rect(420, 125, PANEL_WIDTH, PANEL_HEIGHT)
    SCREEN.blit(panel_surface, panel_rect)
    
    # Foto Jonathan
    jo_image = pygame.image.load('./assets/misc/Jo.png').convert_alpha()
    jo_image = pygame.transform.scale(jo_image, (225,225))
    SCREEN.blit(jo_image, (150, 125))
    
    MARGIN = 20
    
    # Text - NAMA
    nama_panel_text = display_text("Nama : Jonathan Vince", 12, "Black")
    nama_panel_text_rect = nama_panel_text.get_rect(topleft=(panel_rect.topleft[0] + MARGIN, panel_rect.topleft[1] + MARGIN))
    SCREEN.blit(nama_panel_text, nama_panel_text_rect)

    # Text - KELAS
    kelas_panel_text = display_text("Kelas : AA203", 12, "Black")
    kelas_panel_text_rect = kelas_panel_text.get_rect(topleft=(nama_panel_text_rect.left, nama_panel_text_rect.bottom + MARGIN))
    SCREEN.blit(kelas_panel_text, kelas_panel_text_rect)

    # Text - NIM
    nim_panel_text = display_text("NIM : 200030352", 12, "Black")
    nim_panel_text_rect = nim_panel_text.get_rect(topleft=(kelas_panel_text_rect.left, kelas_panel_text_rect.bottom + MARGIN))
    SCREEN.blit(nim_panel_text, nim_panel_text_rect)

    # Text - BOD
    bod_panel_text = display_text("BOD : 16 April 2002", 12, "Black")
    bod_panel_text_rect = bod_panel_text.get_rect(topleft=(nim_panel_text_rect.left, nim_panel_text_rect.bottom + MARGIN))
    SCREEN.blit(bod_panel_text, bod_panel_text_rect)

    return home_button_rect

def wiki(i):    
    # Display username in menu
    text_surface = display_text(data_planet[i]['nama'], 24, "White")
    text_rect = text_surface.get_rect(midtop=(WIDTH // 2, 20))
    SCREEN.blit(text_surface, text_rect)
    
    # Home Button
    home_button_surface = pygame.image.load('./assets/buttons/HomeButton.png')
    home_button_surface = pygame.transform.scale(home_button_surface, (50, 50))
    home_button_rect = home_button_surface.get_rect(topleft=(20,20))
    SCREEN.blit(home_button_surface, home_button_rect)
    
    # Previous Button
    previous_button_surface = pygame.image.load('./assets/buttons/LeftArrow.png')
    previous_button_surface = pygame.transform.scale(previous_button_surface, ( ARROW_WIDTH, ARROW_HEIGHT))
    previous_button_rect = previous_button_surface.get_rect(midleft=(20, HEIGHT // 2))

    if i > 0:
        SCREEN.blit(previous_button_surface, previous_button_rect)

    # Next Button
    next_button_surface = pygame.image.load('./assets/buttons/RightArrow.png')
    next_button_surface = pygame.transform.scale(next_button_surface, (ARROW_WIDTH, ARROW_HEIGHT))
    next_button_rect = next_button_surface.get_rect(midright=(WIDTH - 20, HEIGHT // 2))

    if i < (len(data_planet) - 1):
        SCREEN.blit(next_button_surface, next_button_rect)
        
    draw_panel_and_text(data_planet[i]['desc'], 16, (0, 0, 0), PANEL_WIDTH - 2 * MARGIN, (400, 125))
    
    # Planet Image
    planet_image_surface = pygame.image.load(data_planet[i]['image'])
    # planet_image_surface = pygame.transform.scale(planet_image_surface,(250,250))
    planet_image_rect = planet_image_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2))
    SCREEN.blit(planet_image_surface, planet_image_rect)


    return home_button_rect, previous_button_rect, next_button_rect;


def quiz():
    print("Quiz")
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and current_page == "input_name":
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            elif event.key == pygame.K_TAB:
                pass  # Ignore Tab key
            elif event.unicode and event.type != pygame.MOUSEBUTTONDOWN:
                username += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN and event.button in (1, 3):
            if current_page == "welcome":
                button_rect = input_name()
                current_page = "input_name"
            elif current_page == "input_name":
                if button_rect.collidepoint(event.pos):
                    main_menu()
                    current_page = "main_menu"
            elif current_page == "main_menu":
                main_menu_rects = main_menu()
                wiki_rect, quiz_rect, about_rect = main_menu_rects
                if wiki_rect.collidepoint(event.pos):
                    wiki_index = 0
                    wiki(wiki_index)
                    current_page = "wiki"
                elif quiz_rect.collidepoint(event.pos):
                    quiz()
                elif about_rect.collidepoint(event.pos):
                    about()
                    current_page = "about"
            elif current_page == "about":
                home_button_rect = about()
                if home_button_rect.collidepoint(event.pos):
                    main_menu()
                    current_page = "main_menu"
            elif current_page == "wiki":
                wiki_rects = wiki(wiki_index)
                home_button_rect, previous_button_rect, next_button_rect = wiki_rects
                if home_button_rect.collidepoint(event.pos):
                    main_menu()
                    current_page = "main_menu"
                if next_button_rect.collidepoint(event.pos) and wiki_index < (len(data_planet) - 1):
                    wiki_index += 1
                    wiki(wiki_index)
                    current_page = "wiki"
                if previous_button_rect.collidepoint(event.pos) and wiki_index > 0:
                    wiki_index -= 1
                    wiki(wiki_index)
                    current_page = "wiki"
                    
    SCREEN.blit(BG, (0,0))  # Clear the screen
    
    if current_page == "welcome":
        welcome()
    elif current_page == "input_name":
        input_name()
    elif current_page == "main_menu":
        main_menu()
    elif current_page == "about":
        about()
    elif current_page == "wiki":
        wiki(wiki_index)
                
    pygame.display.update()
    FRAME.tick(60)
    