def reduce_file_path(path):
    path_array = path.split("/")
    current_path = "/"
    for directory in path_array:
        if directory == '':
            if current_path.endswith("/"):
                continue
            else:
                current_path += "/"
        if directory == ".." or directory == ".":
            if directory == ".":
                continue
            elif directory == "..":
                last_slash = current_path.rfind("/")
                current_path = current_path[:last_slash]
                last_slash = current_path.rfind("/")
                current_path = current_path[:last_slash] + "/"
        else:
            current_path += directory + "/"
    if current_path.endswith("/") and len(current_path) > 1:
        current_path = current_path[:-1]

    print(current_path)

reduce_file_path("/")
reduce_file_path("/srv/../")
reduce_file_path("/srv/www/htdocs/wtf/")
reduce_file_path("/srv/www/../htdocs/wtf")
reduce_file_path("/srv/./././././")
reduce_file_path("/etc//wtf/")
reduce_file_path("/etc/../etc/../etc/../")
reduce_file_path("//////////////")
reduce_file_path("/../")
