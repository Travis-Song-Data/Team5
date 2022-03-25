from game.scripting.action import Action
from constants import *

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds(str(ROOT_PATH.joinpath("pacman/assets/sounds")))
        self._video_service.load_fonts(str(ROOT_PATH.joinpath("pacman/assets/fonts")))
        self._video_service.load_images(str(ROOT_PATH.joinpath("pacman/assets/images")))
        