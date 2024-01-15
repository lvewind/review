from hiworker import *


class DetectOnmyoji(DetectImage):
    def __init__(self):
        super(DetectOnmyoji, self).__init__()

    def is_onmyoji_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("yard_is_onmyoji_panel")
        return result
