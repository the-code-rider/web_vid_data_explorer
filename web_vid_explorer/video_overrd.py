from pathlib import Path
from typing import Union


from nicegui.elements.video import Video

class VideoOvrd(Video):
    def __init__(self, src: Union[str, Path], *,
                 controls: bool = True,
                 autoplay: bool = False,
                 muted: bool = False,
                 loop: bool = False,
                 ) -> None:
        """Video

        Displays a video.

        :param src: URL or local file path of the video source
        :param controls: whether to show the video controls, like play, pause, and volume (default: `True`)
        :param autoplay: whether to start playing the video automatically (default: `False`)
        :param muted: whether the video should be initially muted (default: `False`)
        :param loop: whether the video should loop (default: `False`)

        See `here <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#events>`_
        for a list of events you can subscribe to using the generic event subscription `on()`.
        """
        super().__init__()
        # if Path(src).is_file():
        #     src = core.app.add_media_file(local_file=src)
        self._props['src'] = src
        self._props['controls'] = controls
        self._props['autoplay'] = autoplay
        self._props['muted'] = muted
        self._props['loop'] = loop
