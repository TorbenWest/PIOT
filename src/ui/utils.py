def center_window(window, width: int, height: int) -> None:
    app_center_coordinate_x = (window.winfo_screenwidth() / 2) - (width / 2)
    app_center_coordinate_y = (window.winfo_screenheight() / 2) - (height / 2)
    window.geometry(f"{width}x{height}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")
