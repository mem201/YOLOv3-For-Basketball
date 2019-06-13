import cv2
from yolo import YOLO

def cell(image_box, image_class, yolo):

    person_boxes = []
    cell_classes = []

    for i, c in reversed(list(enumerate(image_class))):
        predicted_class_p = yolo.class_names[c]
        if predicted_class_p != 'person':
            continue
        person_box = image_box[i]
        cells = []
        cell_boxes = []
        person_boxes.append(person_box)

        for a, b in reversed(list(enumerate(image_class))):
            predicted_class_c = yolo.class_names[b]
            if predicted_class_c != 'cell phone':
                continue
            cell_box = image_box[a]

            if cell_box[0] > person_box[0] and cell_box[0] + cell_box[2] < person_box[0] + person_box[2]:
                if cell_box[1] > person_box[1] and cell_box[1] + cell_box[3] < person_box[1] + person_box[3]:
                    cells.append(predicted_class_c)
                    cell_boxes.append(cell_box)

        cell_class = ' '
        if len(cells) == 0:
            cell_classes.append(predicted_class_p)
        else:
            for k in range(len(cells)):
                cell_class = cell_class+str(cells[k])
            cell_classes.append(cell_class)


    return person_boxes, cell_classes