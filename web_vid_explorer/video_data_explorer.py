import pandas as pd

from web_vid_explorer.video_summary import VideoSummary


class VideoDataExplorer:

    def get_summary(self, data_df: pd.DataFrame):
        summary = data_df.duration.describe()
        longest_video = data_df.duration.max()
        shortest_video = data_df.duration.min()
        video_summary = VideoSummary(all_video_count=summary[0],
                     longest_video=longest_video,
                     shortest_video=shortest_video,
                     most_frequent_timestamp=summary[2])

        return video_summary