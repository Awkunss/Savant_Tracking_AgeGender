from collections import defaultdict
from itertools import chain

import cv2

from samples.traffic_meter.utils import Direction, RandColorIterator
from savant.deepstream.drawfunc import NvDsDrawFunc
from savant.deepstream.meta.frame import BBox, NvDsFrameMeta
from savant.utils.artist import Artist, Position
from savant.meta.object import ObjectMeta

class Overlay(NvDsDrawFunc):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.obj_colors = (0, 255, 0, 255)
    

    def draw_on_frame(self, frame_meta: NvDsFrameMeta, artist: Artist):
        for obj_meta in frame_meta.objects:
            if obj_meta.label == 'person':
                # Lấy track_id, bbox và confidence_score
                track_id = obj_meta.track_id
                bbox = obj_meta.bbox
                confidence = obj_meta.confidence
                color = self.obj_colors
                # Kiểm tra bbox hợp lệ trước khi vẽ
                if bbox.width > 0 and bbox.height > 0:
                    # Vẽ bounding box
                    artist.add_bbox(
                        bbox,
                        border_width=2,
                        border_color=color
                    )
                    
                    # Hiển thị track_id, bbox, confidence_score
                    text = f'ID: {track_id} | Conf: {confidence:.2f}'
                    artist.add_text(
                        text,
                        (int(bbox.left), int(bbox.top) - 10),
                        anchor_point_type=Position.LEFT_TOP,
                        font_scale=1.0,
                        font_color=color
                    )
            if obj_meta.label == 'face':
                age = round(obj_meta.get_attr_meta('smoothed_value', 'age').value)
                gender = str(obj_meta.get_attr_meta('smoothed_value', 'gender').value)

                bbox = obj_meta.bbox
                color = self.obj_colors
                if bbox.width > 0 and bbox.height > 0:
                    # Vẽ bounding box
                    artist.add_bbox(
                        bbox,
                        border_width=2,
                        border_color=color
                    )
                    
                    # Hiển thị track_id, bbox, confidence_score
                    text = f'Age: {age} | Gender: {gender}'
                    artist.add_text(
                        text,
                        (int(bbox.left), int(bbox.top) - 10),
                        anchor_point_type=Position.LEFT_TOP,
                        font_scale=1.0,
                        font_color=color
                    )

        frame_w, _ = artist.frame_wh
        artist.add_bbox(
            BBox(
                frame_w // 2,
                self.overlay_height // 2,
                frame_w,
                self.overlay_height,
            ),
            border_width=0,
            bg_color=(0, 0, 0, 0),
        )
       