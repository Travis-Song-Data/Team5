import csv
import random
from constants import *
from game.casting.animation import Animation
from game.casting.background import Background
from game.casting.body import Body
from game.casting.wall import Wall
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.pacman import Pacman
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_wall_action import CollideWallAction
from game.scripting.control_pacman_action import ControlPacmanAction
from game.scripting.draw_walls_action import DrawWallsAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_pacman_action import DrawPacmanAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_pacman_action import MovePacmanAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.draw_background_action import DrawBackgroundAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService

from game.casting.rain import Rain
from game.scripting.draw_rain_action import DrawRainAction
from game.services.video_service import VideoService
from game.casting.food import Food
from game.scripting.draw_food_action import DrawFoodAction
from game.scripting.collide_food_action import CollideFoodAction
from game.casting.ghost import Ghost
from game.scripting.draw_ghost_action import DrawGhostAction
from game.scripting.collide_ghost_action import CollideGhostAction
from game.scripting.move_ghost_action import MoveGhostAction
class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_WALLS_ACTION = CollideWallAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_PACMAN_ACTION = ControlPacmanAction(KEYBOARD_SERVICE)
    DRAW_WALLS_ACTION = DrawWallsAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_PACMAN_ACTION= DrawPacmanAction(VIDEO_SERVICE)
    DRAW_BACKGROUND_ACTION = DrawBackgroundAction(VIDEO_SERVICE)
    DRAW_RAIN_ACTION = DrawRainAction(VIDEO_SERVICE)
    DRAW_GHOST_ACTION = DrawGhostAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_PACMAN_ACTION = MovePacmanAction()
    MOVE_GHOST_ACTION = MoveGhostAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    DRAW_FOOD_ACTION = DrawFoodAction(VIDEO_SERVICE)
    COLLIDE_FOODS_ACTION = CollideFoodAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_GHOSTS_ACTION = CollideGhostAction(PHYSICS_SERVICE, AUDIO_SERVICE)

    def __init__(self):
        pass
    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_background(cast)
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_walls(cast)
        self._add_pacman(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_foods(cast)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, BACKGROUND_SOUND)) 
        
    def _prepare_next_level(self, cast, script):
        self._add_background(cast)
        self._add_walls(cast)
        self._add_pacman(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)
        self._add_foods(cast)
        self._add_ghost(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_pacman(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)
        self._add_ghost(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PACMAN_ACTION)
        script.add_action(INPUT, self.MOVE_GHOST_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_rain(cast)    
        self._add_pacman(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    

    def _add_rain(self, cast):
        cast.clear_actors(RAIN_GROUP)

        for n in range(DEFAULT_RAINS):
            x = random.randint(1, SCREEN_WIDTH - 1)
            y = random.randint(1, SCREEN_HEIGHT - 1)
            position = Point(x, y)
            velocity = Point(0, RAIN_VELOCITY)
            size = Point(0, 0)
            image = Image(RAIN_IMAGES)
            body = Body(position, size, velocity)
            rain = Rain(image, body)
            cast.add_actor(RAIN_GROUP, rain)

    def _add_background(self, cast):
        image = Image(BACKGROUND_IMAGE)
        background = Background(image, True)
        cast.add_actor(BACKGROUND_GROUP, background) 

    def _add_foods(self, cast):
        cast.clear_actors(FOOD_GROUP)

        filename = FOOD_FILE

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    if column == '0':
                        x = FIELD_LEFT + c * FOOD_WIDTH
                        y = FIELD_TOP + r * FOOD_HEIGHT
                        
                        position = Point(x, y)
                        size = Point(FOOD_WIDTH, FOOD_HEIGHT)
                        velocity = Point(0, 0)
                        image = Image(FOOD_IMAGES)
                        point = FOOD_POINT
                        body = Body(position, size, velocity)

                        food = Food(body, image, point)
                        cast.add_actor(FOOD_GROUP, food)

    def _add_walls(self, cast):
        cast.clear_actors(WALL_GROUP)
        
        filename = LEVEL_FILE

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    if column == '1':
                        x = FIELD_LEFT + c * WALL_WIDTH
                        y = FIELD_TOP + r * WALL_HEIGHT
                        
                        position = Point(x, y)
                        size = Point(WALL_WIDTH, WALL_HEIGHT)
                        velocity = Point(0, 0)
                        image = Image(WALL_IMAGES)

                        body = Body(position, size, velocity)

                        wall = Wall(body, image)
                        cast.add_actor(WALL_GROUP, wall)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_pacman(self, cast):
        cast.clear_actors(PACMAN_GROUP)
        x = FIELD_LEFT + WALL_WIDTH
        y = FIELD_BOTTOM - WALL_HEIGHT - PACMAN_HEIGHT
        position = Point(x, y)
        size = Point(PACMAN_WIDTH, PACMAN_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(PACMAN_IMAGES_RIGHT, PACMAN_RATE)
        pacman = Pacman(body, animation)
        cast.add_actor(PACMAN_GROUP, pacman)

    def _add_ghost(self, cast):
        cast.clear_actors(GHOST_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        for i in range(1, level * 2):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            position = Point(x, y)
            size = Point(GHOST_WIDTH, GHOST_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            animation = Animation(GHOST_IMAGES, GHOST_RATE)
            ghost = Ghost(body, animation)
            cast.add_actor(GHOST_GROUP, ghost)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_BACKGROUND_ACTION)
        script.add_action(OUTPUT, self.DRAW_WALLS_ACTION)
        script.add_action(OUTPUT, self.DRAW_RAIN_ACTION)
        script.add_action(OUTPUT, self.DRAW_GHOST_ACTION)
        script.add_action(OUTPUT, self.DRAW_PACMAN_ACTION)
        script.add_action(OUTPUT, self.DRAW_FOOD_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_PACMAN_ACTION)
        script.add_action(UPDATE, self.COLLIDE_GHOSTS_ACTION)        
        script.add_action(UPDATE, self.COLLIDE_FOODS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_WALLS_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)