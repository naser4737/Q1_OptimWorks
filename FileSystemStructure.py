def get_directory_size(filesystem, path):
    path_parts = path.split(".")
    current_dir = filesystem
    for component in path_parts:
        if component in current_dir:
            current_dir = current_dir[component]
        else:
            return f"Directory '{path}' not found."
    
    
    def size(directory):
        total = 0
        for key, value in directory.items():
            if isinstance(value, dict):  
                total += size(value)
            else:  
                total += value
        return total
    
   
    total_size = size(current_dir)
    return f"Total size: {total_size}"


filesystem = {
     "root": {
        "dir1": {
            "subdir1": {
                "file1.txt": 100,
                "file2.txt": 200,
                "subsubdir1": {
                    "file3.txt": 50,
                    "file4.txt": 150,
                    "subsubsubdir1": {
                        "file5.txt": 500,
                        "emptydir1": {}
                    }
                }
            },
            "subdir2": {
                "file6.txt": 300,
                "subsubdir2": {
                    "file7.txt": 700,
                    "subsubsubdir2": {
                        "file8.txt": 800,
                        "file9.txt": 900
                    }
                },
                "emptydir2": {}
            },
            "file10.txt": 1000
        },
        "dir2": {
            "subdir3": {
                "subsubdir3": {
                    "file11.txt": 400,
                    "file12.txt": 500
                },
                "subsubdir4": {
                    "emptydir3": {}
                }
            },
            "subdir4": {
                "file13.txt": 600,
                "subsubdir5": {
                    "file14.txt": 700,
                    "file15.txt": 800,
                    "subsubsubdir3": {
                        "emptydir4": {},
                        "file16.txt": 900,
                        "file17.txt": 1000
                    }
                }
            },
            "emptydir5": {}
        },
        "dir3": {
            "file18.txt": 1100,
            "subdir5": {
                "subsubdir6": {
                    "file19.txt": 1200,
                    "subsubsubdir4": {
                        "file20.txt": 1300,
                        "emptydir6": {}
                    }
                }
            }
        },
        "emptydir7": {},
        "file21.txt": 1400
    }

}

# Input 1 : path = "root.dir1.subdir1"

print(get_directory_size(filesystem, "root.dir1.subdir1"))  #Output :Total size: 1000

# Input 2: path = "root.dir2.subdir4.subsubdir5"
print(get_directory_size(filesystem, "root.dir2.subdir4.subsubdir5"))  #Output :Total size: 3400

# Input 3 : Directory has no files
print(get_directory_size(filesystem, "root.dir1.subdir2.emptydir2")) #Output :Total size: 0

