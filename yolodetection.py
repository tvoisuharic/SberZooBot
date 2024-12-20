from ultralytics import YOLO


def get_animal_from_image(img_path: str) -> str:
    model = YOLO('yolo11x-cls.pt')
    results = model(img_path)

    if not results[0].probs:
        return ""

    top_class = results[0].probs.top1
    animal_name = model.names[top_class]

    return animal_name

