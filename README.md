__Creator: Alex Cardenas__ <br />
Date: July 06, 2022

## Purpose
- This script walks through a folder to find a subtitle file and make it Plex-compliant
- Before the script, subtitles are found in a subfolder "Subs"
- After the script, the subtitles will be copied and renamed in the main folder

## Limitations 
- The subtitle folder must be called "Subs"
- Only the first subtitle file will be taken (whether it's English or not)
  - A future version could check for "en" or "english" in the file name
  
## Issues 
- Line 31 (`x = line[:-1]`) currently removes the last letter of the last entry (which is `\n` for all but the last entry)
  - This makes that file re-checked (since it doesn't match anymore because of that missing last letter)
