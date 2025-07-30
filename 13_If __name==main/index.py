def calculate_area(base,height):
    print("__name__ :", __name__)
    return 0.5 * base * height

if __name__ == "__main__":
    print("This is index.py file")
    a = calculate_area(10,20)
    print(f"area is : ",a)


# summary is when you run this file directly, __name__ will be "__main__"
#if you import this file, __name__ will be "13_If __name__==main.index"
