import os

folder_path = "."

files = os.listdir(folder_path)

print("Files in folder:")
for file in files:
    print(file)

folders = ["Images", "PDFs", "Documents"]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

moved_files = 0        


for file in files:
    if file.endswith(".pdf"):
        os.rename(file, "PDFs/" + file)
        print(file, "moved to PDFs")
        moved_files += 1

    elif file.endswith(".txt") or file.endswith(".docx"):
        os.rename(file, "Documents/" + file)
        print(file, "moved to Documents")
        moved_files += 1

    elif file.endswith(".jpg") or file.endswith(".png"):
        os.rename(file, "Images/" + file)
        print(file, "moved to Images")   
        moved_files += 1
print("\nFile Organizing Completed")
print("Total files moved:", moved_files) 