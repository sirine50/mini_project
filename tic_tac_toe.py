import pygame 

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running: bool = True
font = pygame.font.Font(None, 100)
font2 = pygame.font.Font(None, 60)
font3 = pygame.font.Font(None, 50)
text1 = font3.render("Click space to reset the board", True, "white")
text1_rect = text1.get_rect(topleft=(110, 30))
text2 = font3.render("Click enter to reset the score", True, "White")
text2_rect = text2.get_rect(topleft=(60, 650))
x_turn = True
winning_patternes = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                   [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                   [0, 4, 8], [2, 4, 6]]
pattern = ["", "", "", "", "", "", "", "", ""]
winner = ""
stop_game = False
x_score = 0
o_score = 0
draw = 0


def display_score(x:int, o:int, d:int = 0):
    x_score_text = font2.render(f"X: {x}", True, "white")
    x_score_text_rect = x_score_text.get_rect(center=(50, 30))
    screen.blit(x_score_text, x_score_text_rect)
    o_score_text = font2.render(f"O: {o}", True, "white")
    o_score_text_rect = o_score_text.get_rect(center=(50, 70))
    screen.blit(o_score_text, o_score_text_rect)
    draw_text = font2.render(f"Draw: {draw}", True, "white")
    draw_text_rect = draw_text.get_rect(center=(70, 110))
    screen.blit(draw_text, draw_text_rect)

def which_winner():
    for winning_pattern in winning_patternes:
        i, j, k = winning_pattern
        if pattern[i] == pattern[j] == pattern[k]:
            return pattern[i]

    
def which_to_draw(turn: bool, index:int) -> bool:
    if turn: 
        pattern[index] = "X"
        return False
    else:
        pattern[index] = "O"
        return True


def square_clicked(x: int, y: int, turn: bool):
    if 90 < x < 250 and 90 < y < 250:
        return which_to_draw(turn, 0)
    elif 250 < x < 430 and 90 < y < 250:
        return which_to_draw(turn, 1)
    elif 430 < x < 600 and 90 < y < 250:
        return which_to_draw(turn, 2)
    elif 90 < x < 250 and 250 < y < 430:
        return which_to_draw(turn, 3)
    elif 250 < x < 430 and 250 < y < 430:
        return which_to_draw(turn, 4)
    elif 430 < x < 600 and 250 < y < 430:
        return which_to_draw(turn, 5)
    elif 90 < x < 250 and 430 < y < 600:
        return which_to_draw(turn, 6)
    elif 250 < x < 430 and 430 < y < 600:
        return which_to_draw(turn, 7)
    elif 430 < x < 600 and 430 < y < 600:
        return which_to_draw(turn, 8)
    else:
        return turn
   
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not stop_game:
                x, y = pygame.mouse.get_pos()
                x_turn = square_clicked(x, y, x_turn)
                winner = which_winner()
                if winner == "X":
                    x_score += 1
                elif winner == "O":
                    o_score += 1    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if stop_game:
                    pattern = ["", "", "", "", "", "", "", "", ""]
                    winner = ""
                    stop_game = False
            elif event.key == pygame.K_RETURN:
                if stop_game:
                    x_score = 0
                    o_score = 0
                    draw = 0
                    pattern = ["", "", "", "", "", "", "", "", ""]
                    winner = ""   
                    stop_game = False    

    if "" not in pattern and not winner:
        winner = "draw"
        draw += 1


    if winner:
        stop_game = True
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
    
              
    position = [(160, 160), (340, 160), (520, 160),
                (160, 340), (340, 340), (520, 340),
                (160, 520), (340, 520), (520, 520)]
    
    for i ,element in enumerate(pattern):
        if element:
            text = font.render(element, True, "white")
            text_rect = text.get_rect(center=position[i])
            screen.blit(text, text_rect)


    pygame.draw.line(screen, "white", (250, 90), (250, 600), 15)
    pygame.draw.line(screen, "white", (430, 90), (430, 600), 15)
    pygame.draw.line(screen, "white", (90, 250), (600, 250), 15)
    pygame.draw.line(screen, "white", (90, 430), (600, 430), 15)
    display_score(x_score, o_score, draw)

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()