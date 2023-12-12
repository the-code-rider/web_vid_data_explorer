import pandas as pd
import string

from web_vid_explorer.desciption_summary import DescriptionSummary


class VideoDescriptionExplorer:

    def get_summary(self, data_df: pd.DataFrame):
        summary = data_df.name.describe()
        ds = DescriptionSummary(total_count=summary[0],
                           unique_count=summary[1],
                           most_common_phrase=summary[2],
                           freq_of_most_common_phrase=summary[3])
        return ds

    def most_common_words(self, data_df: pd.DataFrame):
        text = ' '.join(data_df['name'])
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()



