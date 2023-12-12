from dataclasses import dataclass

@dataclass
class VideoSummary:
    all_video_count: int
    longest_video: str
    shortest_video: str
    most_frequent_timestamp: str
