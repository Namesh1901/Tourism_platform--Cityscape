import os
import pandas as pd
# Replace this with your folder path
folder_path = "C:/Users/DELL.DESKTOP-H115PS2/Desktop/interview/Data_analyst/tourism_project/tourism_platform/media/hotel_images"
excel_path = "C:/Users/DELL.DESKTOP-H115PS2/Desktop/interview/Data_analyst/tourism_project/hotel_names.csv"
output_csv = "C:/Users/DELL.DESKTOP-H115PS2/Desktop/interview/Data_analyst/tourism_project/hotel_filter.csv"
df = pd.read_csv(excel_path)
new_names_not_in_excel = []
for name in df['name']:
    #if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        #name, ext = os.path.splitext(filename)

        # Apply the transformations
    new_name = name.lower().replace("'", "").replace(" ", "_")

        # Remove leading "the_" if present
    if new_name.startswith("the_"):
        new_name = new_name[4:]

        # Add the extension back
    new_name += ".jpg"

    if new_name not in os.listdir(folder_path):
        new_names_not_in_excel.append(new_name)
    
pd.DataFrame(new_names_not_in_excel, columns=["new_image_name"]).to_csv(output_csv, index=False)