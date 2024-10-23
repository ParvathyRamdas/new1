# Python code to move all empty boxes (represented by 0) to the end of the array while maintaining the order of the toys and returning the count of empty boxes:
def move_empty_boxes_to_end(boxes):
    non_empty_boxes = []
    empty_box_count = 0
    for box in boxes:
        if box != 0:
            non_empty_boxes.append(box)
        else:
            empty_box_count += 1
    non_empty_boxes.extend([0] * empty_box_count)
    
    return non_empty_boxes, empty_box_count

