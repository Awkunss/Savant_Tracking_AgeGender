# Savant_Tracking_AgeGender demo

**NB**: The demo optionally uses **YOLOV8** model which takes up to **10-15 minutes** to compile to TensorRT engine. The first launch may take a decent time.

The pipeline detects and tracking people, predict their age and gender by their face.

Demonstrated operational modes:

- real-time processing: RTSP streams (multiple sources at once);

Demonstrated adapters:
- Video loop adapter;
- Always-ON RTSP sink adapter;

## Build Engines

The demo uses models that are compiled into TensorRT engines the first time the demo is run. This takes time. Optionally, you can prepare the engines before running the demo by using the command:

```bash
# you are expected to be in Savant/ directory

./samples/tracking_ageGender/build_engines.sh
```

## Run Demo

```bash
# you are expected to be in Savant/ directory

# for 1 video input
docker compose -f samples/tracking_ageGender/docker-compose.x86.yml up
# visit 'http://127.0.0.1:888/stream/tracking/' (LL-HLS)

# for multi input
docker compose -f samples/tracking_ageGender/docker-compose-multi-stream.x86.yml up
# visit 'http://127.0.0.1:8881/stream/tracking-1/' and 'http://127.0.0.1:8882/stream/tracking-2/' (LL-HLS)

# Ctrl+C to stop running the compose bundle
```

To create a custom Grafana dashboard, sign in with `admin\admin` credentials.

## Switch Detector Model

The sample includes an option to choose the model used for object detection by changing the env variable in `.env` file:

- `DETECTOR=peoplenet` for peoplnet
- `DETECTOR=yolov8m` for yolov8m
- `DETECTOR=yolov8s` for yolov8s

**Note**: `yolov8m` detector is set by default.
