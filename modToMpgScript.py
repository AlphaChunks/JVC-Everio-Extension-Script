import os

# IF THIS IS NOT WORKING ITS BECAUSE YOU NEED TO PUT IT IN THE SAME DIRECTORY
# AS THE VIDEOS, PREFERABLY IN A FOLDER. AN EXAMPLE IS SHOWN WITHIN THE GITHUB
# PROJECT.

# Gets directory for videos
script_directory = os.path.dirname(os.path.abspath(__file__))

# Loop thru all videos
for filename in os.listdir(script_directory):
    # Requirement check
    if filename.endswith('.MOD'):
        # Change extension
        new_filename = filename[:-4] + '.mpg'
        
        # Get path
        old_file = os.path.join(script_directory, filename)
        new_file = os.path.join(script_directory, new_filename)
        
        # Rename
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
