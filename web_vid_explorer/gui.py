from nicegui import events,ui
from nicegui.elements.video import Video
from web_vid_explorer.video_overrd import VideoOvrd

def search_query_handler():
    # print(f"you searched for  {query}")
    print(search_query.value)
    ui.label(f'you searched for {search_query.value}')


ui.markdown('## explore the web vid dataset')
search_query = ui.input(value='search phrase').props('clearable')
print(search_query.value)
search_query.on('keydown.enter', handler=search_query_handler)
# search_query.on('keydown.enter',search_query_handler, [search_query.value])


url = 'https://ak.picdn.net/shutterstock/videos/1053841541/preview/stock-footage-travel-blogger-shoot-a-story-on-top-of-mountains-young-man-holds' \
      '-camera-in-forest.mp4'
label = 'Travel blogger shoot a story on top of mountains. young man holds camera in forest'
with ui.card().tight():
    v = Video(url, autoplay=False, muted=True)
    with ui.card_section():
        ui.label(label)


# v.on('ended', lambda _ : ui.notify('Video playback completed'))

ui.run()