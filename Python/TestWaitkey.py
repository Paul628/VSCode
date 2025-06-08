import cv2


if __name__ == "__main__":
    # Create a black image
    img = cv2.imread(r"C:\Users\paull\Pictures\Sudoku.png")
    cv2.imshow('image', img)

    while True:
        c = cv2.waitKey(0) & 0xFF  # Wait for a key press
        if c == 27:  # ESC key
            break
        elif c == 10:  # Enter key
            print("Enter key pressed")
        else:
            print(f"Key pressed: {c}")

    cv2.destroyAllWindows()
      


