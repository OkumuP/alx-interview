def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize triangle with the first row
    triangle = [[1]]

    # Build a  triangle row by row
    for i in range(1, n):
        # Get  previous row
        previous_row = triangle[-1]
        # Start the new row with a 1
        new_row = [1]

        # Calculate inner elements of new row
        for j in range(1, len(previous_row)):
            # Each element is the sum of the two elements above it
            new_row.append(previous_row[j - 1] + previous_row[j])

        # End new row with a 1
        new_row.append(1)
        # Append new row to triangle
        triangle.append(new_row)

    return triangle

