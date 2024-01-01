import pygame
from sys import exit

pygame.init()

HEIGHT, WIDTH = 500, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interstellar")
FRAME = pygame.time.Clock()

image_background = pygame.image.load('./assets/Background.jpg')
BG = pygame.transform.scale(image_background, (WIDTH, HEIGHT))
current_page = "welcome"

# Game Variable
username = 'Masukkan nama'

def display_text(text, size, color):
    FONT = pygame.font.Font('./assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf', size)
    return FONT.render(text, False, color)

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
    # Display username in menu
    text_surface = display_text("Hello, " + username + "!", 16, "White")
    text_rect = text_surface.get_rect(topleft=(10, 10))
    SCREEN.blit(text_surface, text_rect)
    
    # Display Main Menu Text
    main_menu_surface = display_text("MAIN MENU", 30, "White")
    main_menu_rect = main_menu_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
    SCREEN.blit(main_menu_surface, main_menu_rect)
    
    # Wiki Button
    
    # Quiz Button
    
    # About Button

def about():
    print("about")
    
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
                    
    SCREEN.blit(BG, (0,0))  # Clear the screen
    
    if current_page == "welcome":
        welcome()
    elif current_page == "input_name":
        input_name()
    elif current_page == "main_menu":
        main_menu()
    elif current_page == "about":
        about()
                
    pygame.display.update()
    FRAME.tick(60)
    