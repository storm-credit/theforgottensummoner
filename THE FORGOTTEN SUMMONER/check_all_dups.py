import os
import collections

base_dir = r'c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클'

for i in range(31, 43):
    folder_prefix = f'01-{i}'
    target_folder = None
    for foldername in os.listdir(base_dir):
        if foldername.startswith(folder_prefix) and os.path.isdir(os.path.join(base_dir, foldername)):
            target_folder = os.path.join(base_dir, foldername)
            break
            
    if target_folder:
        for root, dirs, files in os.walk(target_folder):
            md_files = [f for f in files if f.endswith('.md')]
            prefix_counts = collections.defaultdict(list)
            for f in md_files:
                parts = f.split('.')
                if len(parts) > 1:
                    prefix = parts[0].strip()
                    # Only track those with a dash like 6-1, 1-1, etc.
                    if '-' in prefix:
                        sub_parts = prefix.split('-')
                        if all(p.replace(' ', '').replace('-', '').isdigit() for p in sub_parts):
                            prefix_counts[prefix].append(f)
                        
            for prefix, flist in prefix_counts.items():
                if len(flist) > 1:
                    print(f'Anomaly found in {root}: Prefix {prefix} has items: {flist}')
