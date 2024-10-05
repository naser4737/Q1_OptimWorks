# Q1_OptimWorks

Question 1: File System Structure (Tree-Based Problem)
Problem Statement: You are given a nested dictionary representing a file system. Each directory can contain subdirectories or files, and each file has a size. Write a function that calculates the total size of all files in a specified subdirectory, which can be given in dot notation (e.g., "root.dir1" or "root.dir2.dir3"). If a specified directory does not exist, return a message indicating that the directory was not found. If the directory has no files, its size is zero. The function should traverse the directory structure and return the total size of all files in the specified subdirectory.
Input-1: 
path = "root.dir1.subdir1"
Expected Output-1:
Total size: 1000


Input-2: 
path = "root.dir2.subdir4.subsubdir5"
Expected Output-2:
Total size: 3400

