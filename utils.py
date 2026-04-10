def calculate_density(result, img):
    h, w, _ = img.shape
    image_area = h * w

    total_area = 0
    count = 0

    # vehicle only
    weights = {
        0:1,   # bike
        1:3,   # bus 
        2:2,   # car
        3:2,   # cng
        5:3,   # mini truck
        8:4    # truck 
    }

    for box in result.boxes:
        cls = int(box.cls[0])

        if cls in weights:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

            box_area = (x2-x1)*(y2-y1)

            # normalize big box effect
            box_area = min(box_area, 30000)

            total_area += box_area * weights[cls]
            count += 1

    density = total_area / image_area


    score = (count * 0.5) + (density * 12)

    return float(score)


def get_congestion_level(score):
    if score < 17:
        return "Low"
    elif score < 25:
        return "Medium"
    else:
        return "High"


def get_signal(level):
    if level == "Low":
        return "GREEN", 10
    elif level == "Medium":
        return "YELLOW", 20
    else:
        return "RED", 30