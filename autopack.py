import os
import shutil

folder=os.listdir('YOUR_FILE_PATH')
src="YOUR_FILE_PATH"

#Add Your file extensions here.
catigorys={
    "Image":[".jpg",".png",".gif"],
    "Document":[".pdf",".txt",".docx"],
    "Archive":[".zip",".rar",".7z"],
    "Music":[".mp3",".wav"],
    "Videos":[".mp4",".mkv"]
}


for i in folder:
    root,extention=os.path.splitext(i)
    for key ,val in catigorys.items():
         for k in val: 
              if extention == k:
                   dest_folder=os.path.join(src,key)
                   if not os.path.exists(dest_folder):
                         os.makedirs(dest_folder)
    
                   source=os.path.join(src,i)
                   dest_file=os.path.join(dest_folder,i)

                   shutil.move(source,dest_file)
                   print(f"Moved {i} --> {key}")
                   break
        
      






