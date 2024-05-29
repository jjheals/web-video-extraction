from pytube import YouTube
import os 

def clean_yt_title(title:str) -> str:
    ''' Cleans the given title to a valid and preferred filename format. 
    
        Args: 
            title (str): raw title to clean
            
        Returns: 
            str: the title but with invalid chars removed, spaces replaced with hyphens
    ''' 
    clean_title:str = title.replace(' ', '-')   # Replace spaces with hyphens
    clean_title = clean_title.replace(':', '-') # Remove colons (invalid char for filename)
    clean_title = clean_title.replace('"', "")  # Remove double quotes
    clean_title = clean_title.replace('|', "")  # Remove | 
    
    return clean_title
    
    
# Prompt for file input or single URL
print('----------------------------------------------')
try: mode:int = int(input('Select mode:\n\t1. File input\n\t2. Single URL\n\nEnter mode (1 | 2): '))
except ValueError: mode = 0

while mode != 1 and mode != 2: 
    mode = int(input(f'\nERROR: Invalid mode ({mode}).\n\nSelect mode:\n\t1. File input\n\t2. Single URL\n\nEnter mode (1 | 2): '))

# Prompt user for the output directory 
output_dir:str = input('Specify output directory: ')

while not os.path.exists(output_dir): 
    output_dir = input(f'The directory "{output_dir}" does not exist.\n\nSpecify output directory: ')

# Act accordingly to the mode
if mode == 1: 
    # File input mode
    filepath:str = input('Enter the path to a TXT file with URLs separated by newlines: ')
    i:int = 1
    
    # INFO print
    print(f'NOTICE: Scraping URLs from "{filepath}...')
    
    # Get the URLs from the file
    with open(filepath, 'r') as file: 
        urls:list[str] = file.read().splitlines()
        
    # Iterate over and scrape each URL
    for u in urls: 
        # INFO print
        print(f'\n[+] ({i}/{len(urls)}) Scraping "{u}" ...')
        
        try: 
            # Create YT obj
            yt = YouTube(u)             
                          
            # Clean the title 
            title:str = clean_yt_title(yt.title)
            
            # Get the highest res stream      
            stream = yt.streams.get_highest_resolution()    
            
            # Download the video
            stream.download(output_path=f'{output_dir}/', filename=f'{title}.mp4')
            
        except Exception as e: 
            print(f'ERROR: There was an error getting the URL "{u}".')
            print(e)
            i+=1        # Integrate counter for debugs
            continue    # Skip to next iteration

        # INFO prints & increment debug counter
        print(f'[+] Saved video "{title}" to the directory "{output_dir}".')
        i+=1
else: 
    # Single URL mode 
    url:str = input('Enter the URL: ')
    
    # INFO print
    print(f'\nNOTICE: Scraping video from "{url}" ...')
    
    try: 
        # Create YT obj
        yt = YouTube(url) 
        
        # Clean the title 
        title:str = clean_yt_title(yt.title)
            
        # Get highest res stream
        stream = yt.streams.get_highest_resolution()
        
        # Download the video 
        stream.download(output_path=f'{output_dir}/', filename=f'{title}.mp4')
        
    except Exception as e: 
        print(f'ERROR: There was an error getting the URL "{url}".')
        print(e) 

print("\nNOTICE: Done. Check console for errors.")
