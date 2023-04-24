from os import *

"""Get name of currednt working directory"""
print(getcwd())
""""List content of directory"""
print(listdir())
"""Create a dir"""
#os.mkdir("dirTest") 
"""Remove directory"""
#os.rmdir("dirTest") 
"""Change into 'file' directory"""
chdir("dirTest")
print(f"My current dirctory is {getcwd()}")



