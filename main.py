#imports
import pygame 
import random
import os
from dataclasses import dataclass,field
from typing import Optional
#initializing pygame(music and channels as well)
pygame.init() 
pygame.mixer.init()
pygame.mixer.set_num_channels(16)
#asset folders
IMAGE_FOLDER="images"
MUSIC_FOLDER="music"
#window setup
screen_width=1400
screen_height=700
windowed_width=screen_width
windowed_height=screen_height
gamewindow=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
game_surface=pygame.Surface((screen_width,screen_height))
pygame.display.set_caption("Space Shooter")
fullscreen=False
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)
icon=pygame.image.load(os.path.join(IMAGE_FOLDER,"rocket.png"))
pygame.display.set_icon(icon)
boss_width=250
boss_height_sprite=150
#load images
restart_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"restart.png"))
play_button_img=     pygame.image.load(os.path.join(IMAGE_FOLDER,"play.png"))
resume_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"resume.png"))
pause_img=           pygame.image.load(os.path.join(IMAGE_FOLDER,"pause.png"))
home_img=            pygame.image.load(os.path.join(IMAGE_FOLDER,"home.png"))
background_img=      pygame.image.load(os.path.join(IMAGE_FOLDER,"background.png"))
home_screen_img=     pygame.image.load(os.path.join(IMAGE_FOLDER,"homescreen.png"))
player_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"rocket.png"))
bullet_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"bullet.png"))
enemy_1_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"enemy_1.png"))
enemy_2_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"enemy_2.png"))
enemy_3_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"enemy_3.png"))
enemy_4_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"enemy_4.png"))
enemy_5_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"enemy_5.png"))
enemy_bullet_img=   pygame.image.load(os.path.join(IMAGE_FOLDER,"enemy_bullet.png"))
boss_1_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_1.png"))
boss_2_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_2.png"))
boss_3_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_3.png"))
boss_4_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_4.png"))
boss_entry_img=      pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_entry.png"))
boss_bullet_1_img=   pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_bullet_1.png"))
boss_bullet_2_img=   pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_bullet_2.png"))
boss_health_img=     pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_health.png"))
boss_defeating_img=  pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_defeating.png"))
boss_bar_img=        pygame.image.load(os.path.join(IMAGE_FOLDER,"boss_bar.png"))
game_over_img=       pygame.image.load(os.path.join(IMAGE_FOLDER,"game_over.png"))
score_img=           pygame.image.load(os.path.join(IMAGE_FOLDER,"score.png"))
highscore_img=       pygame.image.load(os.path.join(IMAGE_FOLDER,"highscore.png"))
life_img=            pygame.image.load(os.path.join(IMAGE_FOLDER,"life.png"))
player_blast_img=    pygame.image.load(os.path.join(IMAGE_FOLDER,"rocket_blast.png"))
warning_img=         pygame.image.load(os.path.join(IMAGE_FOLDER,"warning.png"))
quit_img=            pygame.image.load(os.path.join(IMAGE_FOLDER,"quit.png"))
health_powerup_img=  pygame.image.load(os.path.join(IMAGE_FOLDER,"health_powerup.png"))
rapid_fire_img=      pygame.image.load(os.path.join(IMAGE_FOLDER,"rapid_fire.png"))
shield_img=          pygame.image.load(os.path.join(IMAGE_FOLDER,"shield.png"))
double_shoot_img=     pygame.image.load(os.path.join(IMAGE_FOLDER,"double_shoot.png"))
shield_shell_img=    pygame.image.load(os.path.join(IMAGE_FOLDER,"shield_shell.png"))
#scale images
restart_img=         pygame.transform.scale(restart_img,(280,80))
play_button_img=     pygame.transform.scale(play_button_img,(210,70))
resume_img=          pygame.transform.scale(resume_img,(280,80))
pause_img=           pygame.transform.scale(pause_img,(500,250))
home_img=            pygame.transform.scale(home_img,(240,80))
background_img=      pygame.transform.scale(background_img,(screen_width,screen_height))
home_screen_img=     pygame.transform.scale(home_screen_img,(screen_width,screen_height))
player_img=          pygame.transform.scale(player_img,(40,60))
bullet_img=          pygame.transform.scale(bullet_img,(35,35))
enemy_1_img=         pygame.transform.scale(enemy_1_img,(50,50))
enemy_2_img=         pygame.transform.scale(enemy_2_img,(50,50))
enemy_3_img=         pygame.transform.scale(enemy_3_img,(50,50))
enemy_4_img=         pygame.transform.scale(enemy_4_img,(50,50))
enemy_5_img=         pygame.transform.scale(enemy_5_img,(55,55))
enemy_bullet_img=   pygame.transform.scale(enemy_bullet_img,(20,25))
boss_1_img=          pygame.transform.scale(boss_1_img,(boss_width,boss_height_sprite))
boss_2_img=          pygame.transform.scale(boss_2_img,(boss_width*1.2,boss_height_sprite*1.2))
boss_3_img=          pygame.transform.scale(boss_3_img,(boss_width*1.4,boss_height_sprite*1.4))
boss_4_img=          pygame.transform.scale(boss_4_img,(boss_width*1.6,boss_height_sprite*1.6))
boss_entry_img=      pygame.transform.scale(boss_entry_img,(600,400))
boss_bullet_1_img=   pygame.transform.scale(boss_bullet_1_img,(30,60))
boss_bullet_2_img=   pygame.transform.scale(boss_bullet_2_img,(40,300))
boss_health_img=     pygame.transform.scale(boss_health_img,(250,50))
boss_defeating_img=  pygame.transform.scale(boss_defeating_img,(600,400))
boss_bar_img=        pygame.transform.scale(boss_bar_img,(290,40))
game_over_img=       pygame.transform.scale(game_over_img,(screen_width,screen_height)) 
score_img=           pygame.transform.scale(score_img,(150,45))
highscore_img=       pygame.transform.scale(highscore_img,(180,45))
life_img=            pygame.transform.scale(life_img,(40,40))
player_blast_img=    pygame.transform.scale(player_blast_img,(100,100))
warning_img=         pygame.transform.scale(warning_img,(300,150))
quit_img=            pygame.transform.scale(quit_img,(250,80))
health_powerup_img=  pygame.transform.scale(health_powerup_img,(40,40))
rapid_fire_img=      pygame.transform.scale(rapid_fire_img,(40,40))
shield_img=          pygame.transform.scale(shield_img,(40,40))
double_shoot_img=     pygame.transform.scale(double_shoot_img,(40,40))
shield_shell_img=    pygame.transform.scale(shield_shell_img,(90,90))
#load audios
gun_shooting_tune=pygame.mixer.Sound(os.path.join(MUSIC_FOLDER,"gun_shooting_tune.mp3"))
gun_shooting_tune.set_volume(0.4)
boss_explosion_tune=pygame.mixer.Sound(os.path.join(MUSIC_FOLDER,"boss_explosion.mp3"))
boss_explosion_tune.set_volume(0.7)
boss_explosion_channel=pygame.mixer.Channel(0)
enemy_shoot_tune=pygame.mixer.Sound(os.path.join(MUSIC_FOLDER,"enemy_shoot.mp3"))
enemy_shoot_tune.set_volume(0.4)
shield_breaking_tune=pygame.mixer.Sound(os.path.join(MUSIC_FOLDER,"shield_breaking.mp3"))
shield_breaking_tune.set_volume(0.7)
game_over_tune=pygame.mixer.Sound(os.path.join(MUSIC_FOLDER,"game_over_tune.mp3"))
pygame.mixer.music.load(os.path.join(MUSIC_FOLDER,"background_music.mp3"))
pygame.mixer.music.set_volume(0.4)
 
#asset collections
enemy_imgs=[
    enemy_1_img,
    enemy_2_img,
    enemy_3_img,
    enemy_4_img
]
fast_enemy_imgs=[pygame.transform.scale(enemy_1_img,(40,40)),
                 pygame.transform.scale(enemy_2_img,(40,40)),
                 pygame.transform.scale(enemy_3_img,(40,40)),
                 pygame.transform.scale(enemy_4_img,(40,40)),]

powerup_imgs={
    "health":health_powerup_img,
    "rapid_fire":rapid_fire_img,
    "shield":shield_img,
    "double_shoot":double_shoot_img
}

 
 
# Minimum window size so the game surface never gets scaled down to something unusable
MIN_WINDOW_WIDTH=400
MIN_WINDOW_HEIGHT=200
#Game constants
POWERUP_SPEED=3
BULLET_SPEED=7.5
FAST_ENEMY_CHANCE=0.15 
CARRIER_ENEMY_CHANCE=0.10
ZIGZAG_ENEMY_CHANCE=0.10
SHOOTER_ENEMY_CHANCE=0.05
MARGIN=80
ZIGZAG_RANGE=150
SHOOTER_FIRE_DELAY=1500
#Dataclasses
@dataclass
class Player:
    x:int
    y:int
    velocity:int
    lives:int

@dataclass
class WeaponState:
    rapid_fire:bool
    rapid_fire_start_time:int
    rapid_fire_duration:int

    double_shoot:bool
    double_shoot_start_time:int
    double_shoot_duration:int

    last_shoot_time:int
    normal_shoot_delay:int
    rapid_fire_shoot_delay:int

@dataclass
class ShieldState:
    active:bool

@dataclass
class EnemyState:
    x:int
    y:int
    speed:float
    image:pygame.Surface
    enemy_type:str="normal"
    health:int=1
    direction:int=1
    last_shot_time:int=0
    zigzag_distance:int=0

@dataclass
class BossState:
    active:bool
    entry:bool
    defeated:bool
    x:float
    y:float
    level:int
    image:Optional[pygame.Surface]
    health:int
    max_health:int
    speed:float
    move_type:int
    direction:int
    shoot_delay:int
    BULLET_SPEED:int
    beam_speed:int
    bullets_before_beam:int
    attack_count:int
    shoot_time:int
    beam_warning:bool
    beam_warning_x:float 
    beam_warning_time:int
    entry_time:int
    defeated_time:int
    bullets:list=field(default_factory=list)


def load_highscore():#load the highscore
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt","w") as f:
            f.write("0")
        return 0
    with open("highscore.txt","r") as f:
        return int(f.read())

def save_highscore(highscore):#saves the highscore
    with open("highscore.txt","w")as f:
        f.write(str(highscore))
 
desktop_width,desktop_height=pygame.display.get_desktop_sizes()[0]
def toggle_fullscreen():#toggle between fulllscreen and windowed mode
    global gamewindow,fullscreen
    fullscreen=not fullscreen
    if fullscreen:
        gamewindow=pygame.display.set_mode((desktop_width,desktop_height),pygame.FULLSCREEN)
    else:
        gamewindow=pygame.display.set_mode((windowed_width,windowed_height),pygame.RESIZABLE)
 
def handle_resize(event):#window resizeing
    global gamewindow,windowed_width,windowed_height
    if fullscreen:
        return
    new_width=max(event.w,MIN_WINDOW_WIDTH)
    new_height=max(event.h,MIN_WINDOW_HEIGHT)
    windowed_width,windowed_height=new_width,new_height
    gamewindow=pygame.display.set_mode((new_width,new_height),pygame.RESIZABLE)
 
def display_surface(shake_x=0,shake_y=0):#display helpers
    window_width,window_height=gamewindow.get_size()
    scaled_surface=pygame.transform.scale(game_surface,(window_width,window_height))
    scaled_shake_x=int(shake_x*(window_width/screen_width))
    scaled_shake_y=int(shake_y*(window_height/screen_height))
    gamewindow.blit(scaled_surface,(scaled_shake_x,scaled_shake_y))
 
def get_scaled_mouse_position(mouse_position):
    window_width,window_height=gamewindow.get_size()
    mouse_x=mouse_position[0]*(screen_width/window_width)
    mouse_y=mouse_position[1]*(screen_height/window_height)
    return mouse_x,mouse_y
 
def home_screen():#Menu screen(home screen)
    
    play_x=screen_width//2-105
    play_y=365
    play_rect=pygame.Rect(play_x,play_y,play_button_img.get_width(),play_button_img.get_height())
    
    while True:
        game_surface.blit(home_screen_img,(0,0))
        game_surface.blit(play_button_img,(play_x,play_y))
        pygame.draw.rect(game_surface,"#FFEE00",play_rect,3)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.VIDEORESIZE:
                handle_resize(event)
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_position=get_scaled_mouse_position(event.pos)
                if play_rect.collidepoint(mouse_position):
                    return
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_F11:
                    toggle_fullscreen()
        display_surface()
        pygame.display.update()
        clock.tick(60)
 
def pause_screen():#Menu screen(pause screen)

    pause_x=screen_width//2-250
    pause_y=30
    resume_x=screen_width//2-140
    resume_y=270
    resume_rect=pygame.Rect(resume_x,resume_y,resume_img.get_width(),resume_img.get_height())
    restart_x=screen_width//2-340
    restart_y=400
    restart_rect=pygame.Rect(restart_x,restart_y,restart_img.get_width(),restart_img.get_height())
    home_x=screen_width//2+100
    home_y=400
    home_rect=pygame.Rect(home_x,home_y,home_img.get_width(),home_img.get_height())
    quit_x=screen_width//2-125
    quit_y=530
    quit_rect=pygame.Rect(quit_x,quit_y,quit_img.get_width(),quit_img.get_height())

    pause_overlay=pygame.Surface((screen_width,screen_height),pygame.SRCALPHA)
    pause_overlay.fill((0,0,0,170))
    paused_frame=game_surface.copy()

    overlay_alpha=0

    while True:
        game_surface.blit(paused_frame,(0,0))
        if overlay_alpha<170:
            overlay_alpha+=12
        pause_overlay.set_alpha(overlay_alpha)
        game_surface.blit(pause_overlay,(0,0))
        if overlay_alpha>=150:
            game_surface.blit(pause_img,(pause_x,pause_y))
            game_surface.blit(resume_img,(resume_x,resume_y))
            game_surface.blit(restart_img,(restart_x,restart_y))
            game_surface.blit(home_img,(home_x,home_y))
            game_surface.blit(quit_img,(quit_x,quit_y))

            pygame.draw.rect(game_surface,"#FF0000",resume_rect,3)
            pygame.draw.rect(game_surface,"#FF0000",restart_rect,3)
            pygame.draw.rect(game_surface,"#FF0000",home_rect,3)
            pygame.draw.rect(game_surface,"#FF0000",quit_rect,3)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "quit"
            if event.type==pygame.VIDEORESIZE:
                handle_resize(event)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_F11:
                    toggle_fullscreen()
                if event.key==pygame.K_ESCAPE or event.key==pygame.K_p:
                    return "resume"
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouseposition=get_scaled_mouse_position(event.pos)
                if resume_rect.collidepoint(mouseposition):
                    return "resume"
                if restart_rect.collidepoint(mouseposition):
                    return "restart"
                if home_rect.collidepoint(mouseposition):
                    return "home"
                if  quit_rect.collidepoint(mouseposition):
                    return "quit"
        display_surface()
        pygame.display.update()
        clock.tick(60)

def game_over_screen(score):#Menu screen(game over screen)
    game_over_tune.play()
    quit_x=screen_width//2-525
    quit_y=550
    quit_rect=pygame.Rect(quit_x,quit_y,quit_img.get_width(),quit_img.get_height())
    restart_x=screen_width//2-125
    restart_y=550
    restart_rect=pygame.Rect(restart_x,restart_y,restart_img.get_width(),restart_img.get_height())
    home_x=screen_width//2+275
    home_y=550
    home_rect=pygame.Rect(home_x,home_y,home_img.get_width(),home_img.get_height())
    while True:
        game_surface.blit(game_over_img,(0,0))
        game_surface.blit(quit_img,(quit_x,quit_y))
        game_surface.blit(restart_img,(restart_x,restart_y))
        game_surface.blit(home_img,(home_x,home_y))
        pygame.draw.rect(game_surface,(255,0,0),quit_rect,3)
        pygame.draw.rect(game_surface,(255,0,0),restart_rect,3)
        pygame.draw.rect(game_surface,(255,0,0),home_rect,3)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.VIDEORESIZE:
                handle_resize(event)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return "restart"
                if event.key==pygame.K_F11:
                    toggle_fullscreen()
 
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_position=get_scaled_mouse_position(event.pos)
                if quit_rect.collidepoint(mouse_position):
                    pygame.quit()
                    quit()
                if restart_rect.collidepoint(mouse_position):
                    return "restart"
                if home_rect.collidepoint(mouse_position):
                    return "home"
                
        game_surface.blit(score_img,(screen_width//2-120,440))
        score_text=font.render(str(score),True,"#FFFFFF")
        score_rect=score_text.get_rect(center=(screen_width//2+60,465))
        game_surface.blit(score_text,score_rect)
        display_surface()
        pygame.display.update()
        clock.tick(60)

"""PLAYER SYSTEM"""
def handle_player_input(player):
        keys=pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x>0:
            player.x-=player.velocity
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x<screen_width-60:
            player.x+=player.velocity
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y>screen_height//2:
            player.y-=player.velocity
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y<screen_height-60:
            player.y+=player.velocity

def update_weapon_timers(weapon,current_time):
    if weapon.rapid_fire:
        if current_time-weapon.rapid_fire_start_time>=weapon.rapid_fire_duration:
            weapon.rapid_fire=False
    if weapon.double_shoot:
        if current_time-weapon.double_shoot_start_time>=weapon.double_shoot_duration:
            weapon.double_shoot=False

def update_player_bullets(bullets):
    for bullet in bullets[:]:
        bullet[1]-=BULLET_SPEED
        if bullet[1]<-30:
            bullets.remove(bullet)
        else:
            game_surface.blit(bullet_img,(bullet[0],bullet[1]))

def update_powerups(powerups,player,player_rect,weapon,shield,current_time):
    for powerup in powerups[:]:
                powerup[1]+=POWERUP_SPEED
                if powerup[1]>screen_height-10:
                    powerups.remove(powerup)
                    continue

                powerup_rect=pygame.Rect(powerup[0],powerup[1],powerup_imgs[powerup[2]].get_width(),powerup_imgs[powerup[2]].get_height())
                if powerup_rect.colliderect(player_rect):
                    activate_powerup(powerup[2],player,weapon,shield,current_time)
                    powerups.remove(powerup)
                    continue
                game_surface.blit(powerup_imgs[powerup[2]],(powerup[0],powerup[1]))

def activate_powerup(powerup_type,player,weapon,shield,current_time):
    if powerup_type=="health":
        player.lives=min(5,player.lives+1)
    elif powerup_type=="rapid_fire":
        weapon.rapid_fire=True
        weapon.rapid_fire_start_time=current_time
    elif powerup_type=="double_shoot":
        weapon.double_shoot=True
        weapon.double_shoot_start_time=current_time
    elif powerup_type=="shield":
        shield.active=True

"""ENEMY SYSTEM"""
def spawn_enemy(speed,enemy_type="normal"):
    if enemy_type=="normal":
        image=random.choice(enemy_imgs)
        enemy_speed=speed
    elif enemy_type=="fast":
        image=random.choice(fast_enemy_imgs)
        enemy_speed=speed*1.8
    elif enemy_type=="carrier":
        image=enemy_5_img
        enemy_speed=speed*0.5
    elif enemy_type=="zigzag":
        image=random.choice(enemy_imgs)
        enemy_speed=speed*0.8
    elif enemy_type=="shooter":
        image=random.choice(enemy_imgs)
        enemy_speed=speed
    if enemy_type=="carrier":
        x=random.randint(MARGIN,screen_width-image.get_width()-MARGIN)
    elif enemy_type=="zigzag":
        x=random.randint(ZIGZAG_RANGE,screen_width-image.get_width()-ZIGZAG_RANGE)
    else:
        x=random.randint(0,screen_width-image.get_width())
    return EnemyState(x=x,y=-image.get_height(),speed=enemy_speed,image=image,enemy_type=enemy_type,health=1,direction=1,last_shot_time=pygame.time.get_ticks()-random.randint(0,SHOOTER_FIRE_DELAY))


def spawn_next_enemy(enemy_base_speed):
    roll=random.random()
    if roll<FAST_ENEMY_CHANCE:
        return spawn_enemy(enemy_base_speed,"fast")
    elif roll<FAST_ENEMY_CHANCE+CARRIER_ENEMY_CHANCE:
        return spawn_enemy(enemy_base_speed,"carrier")
    elif roll<(FAST_ENEMY_CHANCE+CARRIER_ENEMY_CHANCE+ZIGZAG_ENEMY_CHANCE):
        return spawn_enemy(enemy_base_speed,"zigzag")
    elif roll<(FAST_ENEMY_CHANCE+CARRIER_ENEMY_CHANCE+ZIGZAG_ENEMY_CHANCE+SHOOTER_ENEMY_CHANCE):
        return spawn_enemy(enemy_base_speed,"shooter")
    
    return spawn_enemy(enemy_base_speed)

def update_enemy(enemy):
    enemy.y+=enemy.speed
    if enemy.enemy_type=="zigzag":
        enemy.x+=enemy.direction*3
        enemy.zigzag_distance+=3
        if enemy.zigzag_distance>=ZIGZAG_RANGE:
            enemy.direction*=-1
            enemy.zigzag_distance=0
    return pygame.Rect(enemy.x,enemy.y,enemy.image.get_width(),enemy.image.get_height())

def enemy_attack(enemy,enemy_bullets,current_time):
    if enemy.enemy_type!="shooter":
        return 
    if current_time-enemy.last_shot_time>=SHOOTER_FIRE_DELAY:
        enemy.last_shot_time=current_time
        bullet_x=enemy.x+enemy.image.get_width()//2-enemy_bullet_img.get_width()//2
        bullet_y=enemy.y+enemy.image.get_height()
        bullet_speed=enemy.speed+3
        enemy_bullets.append([bullet_x,bullet_y,bullet_speed])

def update_enemy_bullets(enemy_bullets,player_rect,player,shield):
    for bullet in enemy_bullets[:]:
        bullet[1]+=bullet[2]
        bullet_rect=pygame.Rect(bullet[0],bullet[1],enemy_bullet_img.get_width(),enemy_bullet_img.get_height())
        if bullet_rect.colliderect(player_rect):
            enemy_bullets.remove(bullet)
            player_take_damage(player,shield)
        elif bullet[1]>screen_height-10:
            enemy_bullets.remove(bullet)
        else:
            game_surface.blit(enemy_bullet_img,(bullet[0],bullet[1]))

def player_take_damage(player,shield):
    if shield.active:
        shield.active=False
        shield_breaking_tune.play()
        return
    player.lives-=1


def process_enemy(enemy,enemies,enemy_rect,bullets,player_rect,player,shield,powerups,score,highscore,enemy_base_speed):
    for bullet in bullets[:]:
        bullet_rect=pygame.Rect(bullet[0],bullet[1],bullet_img.get_width(),bullet_img.get_height())
 
        if bullet_rect.colliderect(enemy_rect):
            bullets.remove(bullet)
            enemy_shoot_tune.play()
            enemy_base_speed+=0.005
            score+=10
            if score>highscore:
                highscore=score
                save_highscore(highscore)
            if random.random()<0.25:
                powerup_type=random.choice([
                    "health",
                    "rapid_fire",
                    "shield",
                    "double_shoot"
                ])
                powerups.append([enemy.x,enemy.y,powerup_type])
            if enemy.enemy_type=="carrier":
                return(enemy,"split",score,highscore,enemy_base_speed)
            return None,"destroy",score,highscore,enemy_base_speed,
    
    if enemy_rect.colliderect(player_rect):
        player_take_damage(player,shield)
        return None,"destroy",score,highscore,enemy_base_speed

    if enemy.y > screen_height:
        player_take_damage(player,shield)
        return None,"destroy",score,highscore,enemy_base_speed

    return enemy,None,score,highscore,enemy_base_speed

"""BOSS SYSTEM"""
def setup_boss(boss):
    if boss.level==1:
        boss.image=boss_1_img
        boss.health=20
        boss.max_health=20
        boss.speed=2
        boss.shoot_delay=1000
        boss.BULLET_SPEED=5
        boss.move_type=0
        boss.bullets_before_beam=4
        boss.beam_speed=7
    elif boss.level==2:
        boss.image=boss_2_img
        boss.health=35
        boss.max_health=35
        boss.speed=2.5
        boss.shoot_delay=850
        boss.BULLET_SPEED=6
        boss.move_type=1
        boss.bullets_before_beam=5
        boss.beam_speed=6
    elif boss.level==3:
        boss.image=boss_3_img
        boss.health=50
        boss.max_health=50
        boss.speed=3
        boss.shoot_delay=700
        boss.BULLET_SPEED=7
        boss.move_type=2
        boss.bullets_before_beam=6
        boss.beam_speed=5
    else:
        boss.image=boss_4_img
        boss.health=70+(boss.level-4)*15
        boss.max_health=boss.health
        boss.speed=3.5
        boss.shoot_delay=max(350,650-(boss.level-4)*20)
        boss.BULLET_SPEED=8+(boss.level-4)*0.25
        boss.move_type=3
        boss.bullets_before_beam=7
        boss.beam_speed=4-(boss.level-4)*0.5


def move_boss(boss):
    if boss.y<50:
            boss.y+=boss.speed
    else:
        if boss.move_type==1:
            boss.x+=boss.speed*boss.direction
            if boss.x<=0:
                boss.direction=1
            elif boss.x>=screen_width-boss.image.get_width():
                boss.direction=-1
        elif boss.move_type==2:
            boss.x+=(boss.speed+2)*boss.direction
            if boss.x<=0:
                boss.direction=1
            elif boss.x>=screen_width-boss.image.get_width():
                boss.direction=-1
        elif boss.move_type>=3:
            boss.x+=(boss.speed+2)*boss.direction
            if random.randint(1,120)==1:
                boss.direction*=-1
            if boss.x<=0:
                boss.x=0
                boss.direction=1
            elif boss.x>=screen_width-boss.image.get_width():
                boss.x=screen_width-boss.image.get_width()
                boss.direction=-1

def boss_attack(current_time,boss,player):
    if boss.y>=50 and not boss.beam_warning and current_time-boss.shoot_time>=boss.shoot_delay:
        boss.attack_count+=1
        if boss.attack_count<=boss.bullets_before_beam:
            boss_bullet_x=boss.x+boss.image.get_width()//2
            boss_bullet_y=boss.y+boss.image.get_height()-30
            target_x=player.x+30
            target_y=player.y+30
            dx=target_x-boss_bullet_x
            dy=target_y-boss_bullet_y
            distance=(dx**2+dy**2)**0.5
            if distance==0:
                distance=1
            velocity_x=(dx/distance)*boss.BULLET_SPEED
            velocity_y=(dy/distance)*boss.BULLET_SPEED
            boss.bullets.append([boss_bullet_x,boss_bullet_y,velocity_x,velocity_y,"bullet"])
            
        else:
            boss.beam_warning_x=player.x+30
            boss.beam_warning=True
            boss.beam_warning_time=current_time
            boss.attack_count=0
        boss.shoot_time=current_time
    if boss.beam_warning:
        game_surface.blit(warning_img,(screen_width//2-150,screen_height//2-75))
        if current_time-boss.beam_warning_time>=500:
            beam_x=boss.beam_warning_x-20
            beam_y=-200
            boss.bullets.append([beam_x,beam_y,0,boss.beam_speed,"beam"])
            boss.beam_warning=False


def update_boss_bullets(player_rect,boss,player,shield):
    for boss_bullet in boss.bullets[:]: 
        boss_bullet[0]+=boss_bullet[2]
        boss_bullet[1]+=boss_bullet[3]
        if boss_bullet[4]=="bullet":
            boss_bullet_rect=pygame.Rect(boss_bullet[0],boss_bullet[1],boss_bullet_1_img.get_width(),boss_bullet_1_img.get_height())
            if boss_bullet_rect.colliderect(player_rect):
                boss.bullets.remove(boss_bullet)
                player_take_damage(player,shield)
            elif(boss_bullet[0]< -30 or boss_bullet[0]>screen_width or boss_bullet[1]<-60 or boss_bullet[1]>screen_height):
               boss.bullets.remove(boss_bullet)
            else:
                game_surface.blit(boss_bullet_1_img,(boss_bullet[0],boss_bullet[1])) 
        elif boss_bullet[4]=="beam":
            beam_rect=pygame.Rect(boss_bullet[0],boss_bullet[1],boss_bullet_2_img.get_width(),boss_bullet_2_img.get_height())
            if beam_rect.colliderect(player_rect):
                boss.bullets.remove(boss_bullet)
                player_take_damage(player,shield)
            elif boss_bullet[1]>screen_height-10:
                boss.bullets.remove(boss_bullet)
            else:
                game_surface.blit(boss_bullet_2_img,(boss_bullet[0],boss_bullet[1]))


def boss_take_damage(current_time,boss_rect,boss,bullets):
    for bullet in bullets[:]:
        bullet_rect=pygame.Rect(bullet[0],bullet[1],bullet_img.get_width(),bullet_img.get_height())
        if bullet_rect.colliderect(boss_rect):
            bullets.remove(bullet)
            enemy_shoot_tune.play()
            boss.health-=1
            break
    
    if boss.health<=0:
        boss.active=False
        boss.bullets.clear()
        boss.defeated=True
        boss.defeated_time=current_time
        return True
    return False



def draw_boss(boss):
    game_surface.blit(boss.image,(boss.x,boss.y))


"""VISUAL EFFECTS"""
def update_screen_shake(current_time,screen_shaking,shake_start_time,shake_duration,shake_strength):
    shake_x=0
    shake_y=0
    if screen_shaking:
        elapsed_time=current_time-shake_start_time
        if elapsed_time<shake_duration:
            remaining_strength=1-(elapsed_time/shake_duration)
            current_strength=int(shake_strength*remaining_strength)
            shake_x=random.randint(-current_strength,current_strength)
            shake_y=random.randint(-current_strength,current_strength)
        else:
            screen_shaking=False
    return shake_x,shake_y,screen_shaking

def start_screen_shake(current_time,duration,strength):
    return True,current_time,duration,strength

def handle_boss_defeat(boss,score,highscore):#Game helpers
    score+=1000
    if score>highscore:
        highscore=score
        save_highscore(highscore)
    boss.level+=1
    next_boss_appears=score+boss.level*50
    return score,highscore,next_boss_appears

def boss_inactive(boss):
    return(not boss.active and not boss.entry and not boss.defeated)


def draw_entities(player,enemies,shield,player_dead,boss):#Rendering
    if boss_inactive(boss):
        for enemy in enemies:
            game_surface.blit(enemy.image,(enemy.x,enemy.y))

    if not player_dead:
        game_surface.blit(player_img,(player.x,player.y))
        if shield.active:
            shield_x=player.x+player_img.get_width()//2-shield_shell_img.get_width()//2
            shield_y=player.y+player_img.get_height()//2-shield_shell_img.get_height()//2
            game_surface.blit(shield_shell_img,(shield_x,shield_y))
    else:
        game_surface.blit(player_blast_img,(player.x-40,player.y-30))


def draw_hud(player,score,highscore,boss):
    for i in range(player.lives):
        game_surface.blit(life_img,(10+i*50,10))

    game_surface.blit(highscore_img,(850,10))
    highscore_text=font.render(str(highscore),True,"#ffffff")
    game_surface.blit(highscore_text,(1040,17))
    game_surface.blit(score_img,(1130,10))
    score_text=font.render(str(score),True,"#ffffff")
    game_surface.blit(score_text,(1280,17))
    if boss.active:
        game_surface.blit(boss_health_img,(screen_width//2-125,15))
        boss_bar_x=screen_width//2-180
        boss_bar_y=55
        health_width=int((boss.health/boss.max_health)*225)
        pygame.draw.rect(game_surface,"#FF0000",(screen_width//2-125,65,health_width,20))
        game_surface.blit(boss_bar_img,(boss_bar_x,boss_bar_y))


def create_normal_enemy(x,y,speed):
    return EnemyState(x=x,y=y,speed=speed,image=random.choice(enemy_imgs),enemy_type="normal",health=1,direction=1,last_shot_time=0)


"""MAIN GAME LOOP"""
def shooting_game():
    pygame.mixer.music.play(-1)
    player=Player(x=100,y=500,velocity=8,lives=3)
    score= 0
    highscore=load_highscore()
    bullets=[]
    enemy_bullets=[]
    enemy_base_speed=2
    enemies=[spawn_next_enemy(enemy_base_speed)]
    running=True
    
    powerups=[]

    weapon=WeaponState(last_shoot_time=0,normal_shoot_delay=250,rapid_fire_shoot_delay=100,rapid_fire=False,rapid_fire_start_time=0,rapid_fire_duration=10000,double_shoot=False,double_shoot_start_time=0,double_shoot_duration=10000)
    shield=ShieldState(active=False)

    boss=BossState(active=False,entry=False,defeated=False,x=screen_width//2-125,y=-150,level=1,image=None,health=0,max_health=0,speed=0,move_type=0,direction=1,shoot_delay=0,BULLET_SPEED=0,beam_speed=0,bullets_before_beam=4,attack_count=0,shoot_time=0,beam_warning=False,beam_warning_x=0,beam_warning_time=0,entry_time=0,defeated_time=0)
    
    next_boss_appears=50


    def fire_weapon():
        bullet_y=player.y
        if weapon.double_shoot:
            bullets.append([player.x-8,bullet_y])
            bullets.append([player.x+28,bullet_y])
        else:
            bullets.append([player.x+10,bullet_y])
        gun_shooting_tune.play()


    screen_shaking=False
    shake_start_time=0
    shake_duration=0
    shake_strength=0
    player_dead=False
    player_death_time=0
    while running:
        current_time=pygame.time.get_ticks()

        update_weapon_timers(weapon,current_time)

        game_surface.blit(background_img,(0,0)) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            if event.type==pygame.VIDEORESIZE:
                handle_resize(event)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE or event.key==pygame.K_p:
                    pause_action=pause_screen()
                    if pause_action=="restart":
                        pygame.mixer.music.stop()
                        return "restart"
                    elif pause_action=="home":
                        pygame.mixer.music.stop()
                        return "home"
                    elif pause_action=="quit":
                        pygame.quit()
                        quit()
                if event.key==pygame.K_F11:
                    toggle_fullscreen()
                if event.key==pygame.K_SPACE:
                    
                    if weapon.rapid_fire:
                        shoot_delay=weapon.rapid_fire_shoot_delay
                    else: 
                        shoot_delay=weapon.normal_shoot_delay
                    if current_time-weapon.last_shoot_time>=shoot_delay:
                        fire_weapon()
                        weapon.last_shoot_time=current_time
 
 
        handle_player_input(player)
 
 
        update_player_bullets(bullets)
 
        if score>=next_boss_appears and boss_inactive(boss):
            boss.entry=True
            boss.entry_time=current_time
            boss.x=screen_width//2-125
            boss.y=-150
            setup_boss(boss)
            boss.bullets.clear()
        if boss.entry:
            
            if current_time-boss.entry_time<1500:
                game_surface.blit(boss_entry_img,(screen_width//2-300,screen_height//2-200))
            else:
                boss.entry=False
                boss.active=True
                (screen_shaking,shake_start_time,shake_duration,shake_strength)=start_screen_shake(current_time,600,18)
        player_rect=pygame.Rect(player.x,player.y,player_img.get_width(),player_img.get_height())
        if boss_inactive(boss):
            for i in range(len(enemies)-1,-1,-1):
                enemy=enemies[i]
                enemy_rect=update_enemy(enemy)
                enemy_attack(enemy,enemy_bullets,current_time)
                enemy,action,score,highscore,enemy_base_speed=process_enemy(enemy,enemies,enemy_rect,bullets,player_rect,player,shield,powerups,score,highscore,enemy_base_speed)
                if action=="split":
                    left_enemy=create_normal_enemy(enemy.x-MARGIN,enemy.y,enemy_base_speed)
                    right_enemy=create_normal_enemy(enemy.x+MARGIN,enemy.y,enemy_base_speed)
        
                    enemies[i]=left_enemy 
                    enemies.append(right_enemy)
                elif action=="destroy":
                    enemies.pop(i)
                else:
                    enemies[i]=enemy
            if boss_inactive(boss) and len(enemies)==0:
                enemies.append(spawn_next_enemy(enemy_base_speed))


        update_powerups(powerups,player,player_rect,weapon,shield,current_time)
        update_enemy_bullets(enemy_bullets,player_rect,player,shield)
        if boss.active:
            move_boss(boss)
            boss_attack(current_time,boss,player)
            boss_rect=pygame.Rect(boss.x,boss.y,boss.image.get_width(),boss.image.get_height())
            update_boss_bullets(player_rect,boss,player,shield)
            
            boss_killed=boss_take_damage(current_time,boss_rect,boss,bullets)
            if boss_killed:
                boss_explosion_channel.play(boss_explosion_tune)
                (screen_shaking,shake_start_time,shake_duration,shake_strength)=start_screen_shake(current_time,1500,12)
                score,highscore,next_boss_appears=handle_boss_defeat(boss,score,highscore)
            draw_boss(boss)
            

        if boss.defeated:
            
            if current_time-boss.defeated_time<1500:
                game_surface.blit(boss_defeating_img,(screen_width//2-300,screen_height//2-200))
            else:
                boss.defeated=False
 
        if player.lives<=0 and player_dead==False:
            pygame.mixer.music.stop()
            player_dead=True
            player_death_time=current_time
            screen_shaking=True
            shake_start_time=current_time
            shake_duration=800
            shake_strength=15
 
        if player_dead:
            
            if current_time-player_death_time>=800:
                
                highscore=load_highscore()
                if score>highscore:
                    save_highscore(score)
                return score
        

        draw_entities(player,enemies,shield,player_dead,boss)
        draw_hud(player,score,highscore,boss)
        shake_x,shake_y,screen_shaking=update_screen_shake(current_time,screen_shaking,shake_start_time,shake_duration,shake_strength)
        display_surface(shake_x,shake_y)
 
        clock.tick(60)
        pygame.display.update()

"""GAME ENTRY POINT"""
while True:
    home_screen() 
    while True:
        final_score=shooting_game()
        if final_score=="restart":
            continue
        elif final_score=="home":
            break
        else:
            game_over_action=game_over_screen(final_score)
            if game_over_action=="restart":
                continue
            elif game_over_action=="home":
                break