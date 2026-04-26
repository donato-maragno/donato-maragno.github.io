import subprocess
import os

videos_dir = './videos'
videos = [
    'energy.mp4',
    'inventory.mp4',
    'logistics.mp4',
    'production strategy.mp4'
]

for video in videos:
    input_path = os.path.join(videos_dir, video)
    output_path = os.path.join(videos_dir, f'small_{video}')
    poster_path = os.path.join(videos_dir, f'{os.path.splitext(video)[0]}.jpg')
    
    print(f"Processing {video}...")
    
    # Compress and downscale to 1080p
    cmd_compress = [
        'ffmpeg', '-y', '-i', input_path,
        '-vf', 'scale=1920:-2',
        '-vcodec', 'libx264', '-crf', '30',
        '-preset', 'faster',
        '-movflags', '+faststart',
        '-an', # Remove audio to save space (portfolio videos usually don't need sound)
        output_path
    ]
    subprocess.run(cmd_compress)
    
    # Extract poster (at 1 second)
    cmd_poster = [
        'ffmpeg', '-y', '-i', input_path,
        '-ss', '00:00:01',
        '-vframes', '1',
        '-q:v', '2',
        poster_path
    ]
    subprocess.run(cmd_poster)
    
    # Check sizes
    orig_size = os.path.getsize(input_path) / (1024*1024)
    new_size = os.path.getsize(output_path) / (1024*1024)
    print(f"Done {video}: {orig_size:.2f}MB -> {new_size:.2f}MB")

print("Processing complete!")
