import os

UNIT = 3
UNIT_NAME = "Navigation and Workflows"
SOURCE_DIR = f"/Users/mathewsoto/Downloads/teacher/{UNIT} - {UNIT_NAME}"
TARGET_DIR = "/Users/mathewsoto/Desktop/Code/assortedPythonScripts"

os.chdir(SOURCE_DIR)

for pathname in os.scandir():

    #all of the lessons start with a number
    if (labNumber := pathname.name[0]).isdigit():
        os.chdir(pathname.name)
        for f in os.scandir():
            if f.name.startswith("Lab"):
                #enter the directory
                os.chdir(f.name + "/Pages")

                #do stuff
                #1. mkdir with all pages in a playground
                labDirectory = f"{TARGET_DIR}/lab{UNIT}_{labNumber}"
                os.mkdir(labDirectory)

                #2. add pages to the directory
                for playgroundPage in os.scandir():
                    with open(playgroundPage.name + "/Contents.swift") as pageFile:
                        pageNumber = playgroundPage.name.split(".")[0]
                        #read full page
                        page = pageFile.read()

                        #write to new file
                        newPlaygroundFileName = f"{labDirectory}/page{pageNumber}.swift"
                        with open(newPlaygroundFileName, "w") as g:
                            g.write(page)


                #exit the directory
                os.chdir("../..")

        #back to root
        os.chdir("..")