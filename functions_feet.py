def converter(feet, inches):
    feet = float(feet)
    inches = float(inches)
    con = feet * 0.3048 + inches * 0.0254
    con = f"{con} m"
    print(con)
    return con