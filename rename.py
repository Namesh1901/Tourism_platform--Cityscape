
import os

# Replace this with your folder path
folder_path = "C:/Users/DELL.DESKTOP-H115PS2/Desktop/interview/Data_analyst/tourism_project/tourism_platform/media/venue_images"

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        name, ext = os.path.splitext(filename)

        # Apply the transformations
        new_name = name.lower().replace("'", "").replace(" ", "_")

        # Remove leading "the_" if present
        if new_name.startswith("the_"):
            new_name = new_name[4:]
        if new_name.endswith(".jpg"):
            new_name = new_name[:-4]
        # Add the extension back
        new_name += ext.lower()

        # Full paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

       # Skip if new filename already exists
        if os.path.exists(new_path):
            print(f"Skipped (already exists): {new_name}")
            continue

        # Rename file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} ➝ {new_name}")
