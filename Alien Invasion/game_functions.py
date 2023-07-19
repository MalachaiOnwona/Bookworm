import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(settings, window, stats, score, button, spaceship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, window, spaceship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_xcoord, mouse_ycoord = pygame.mouse.get_pos()
            check_play_button(settings, window, stats, score, button, spaceship, aliens, bullets, mouse_xcoord, mouse_ycoord)

def check_play_button(settings, window, stats, score, button, spaceship, aliens, bullets, mouse_xcoord, mouse_ycoord):
    button_clicked = button.rect.collidepoint(mouse_xcoord, mouse_ycoord)

    if button_clicked and not stats.game_running:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_running = True

        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        score.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, window, spaceship, aliens)
        spaceship.center_ship()

def check_keydown_events(event, settings, window, spaceship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        spaceship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        spaceship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, window, spaceship, bullets)

def check_keyup_events(event, spaceship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        spaceship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        spaceship.moving_left = False

def fire_bullet(settings, window, spaceship, bullets):
    if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, window, spaceship)
            bullets.add(new_bullet)

def update_bullets(settings, window, stats, score, spaceship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_alien_bullet_collisions(settings, window, stats, score, aliens, bullets, spaceship)

def check_alien_bullet_collisions(settings, window, stats, score, aliens, bullets, spaceship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points
            score.prep_score()
        check_high_score(stats, score)

    if len(aliens) == 0:
        bullets.empty()
        settings.speed_increase()

        stats.game_level += 1
        score.prep_level()

        create_fleet(settings, window, spaceship, aliens)

def update_screen(settings, window, stats, score, spaceship, bullets, aliens, button):
    window.fill(settings.background_color)
    spaceship.draw()

    for bullet in bullets:
        bullet.draw_bullet()
    
    aliens.draw(window)
    score.display_score()

    if not stats.game_running:
        button.draw_button()

    pygame.display.flip() 

def update_aliens(settings, stats, score, window, spaceship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(spaceship, aliens):
        ship_hit(settings, stats, score, window, spaceship, aliens, bullets)

    check_alien_bottom(settings, stats, score,  window, spaceship, aliens, bullets)

def ship_hit(settings, stats, score, window, spaceship, aliens, bullets):
    if stats.num_ships_left > 0:
        stats.num_ships_left -= 1

        score.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, window, spaceship, aliens)
        spaceship.center_ship()

        sleep(0.5)
    else:
        stats.game_running = False
        pygame.mouse.set_visible(True)

def check_alien_bottom(settings, stats, score, window, spaceship, aliens, bullets):
    window_rectangle = window.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= window_rectangle.bottom:
            ship_hit(settings, stats, score, window, spaceship, aliens, bullets)
            break

def create_fleet(settings, window, spaceship, aliens):
    alien = Alien(settings, window)
    number_of_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, spaceship.rect.height, alien.rect.height)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(settings, window, aliens, alien_number, row_number)

def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.window_width - (2*alien_width)
    number_of_aliens_x = int(available_space_x/(2*alien_width))

    return number_of_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.window_height - (10*alien_height) - ship_height)
    number_rows = int(available_space_y / (5*alien_height))

    return number_rows

def create_alien(settings, window, aliens, alien_number, number_of_rows):
    alien = Alien(settings, window)
    alien_width = alien.rect.width
    alien.xcoord = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.xcoord
    alien.rect.y = alien_width + 5 * alien.rect.height * number_of_rows
    aliens.add(alien)

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()