import os
import argparse
from tqdm import tqdm
from random import shuffle

import os

# Path to the root folder containing subfolders with speaker names
def rename_files():
    root_folder = "/l/users/hawau.toyin/FreeVC/FreeVC/dataset/wavlm/cmu_artic_16k/cmu_artic_ar_test/"

    # Loop through each subfolder (speaker) in the root folder
    for speaker in os.listdir(root_folder):
        speaker_folder = os.path.join(root_folder, speaker)
        
        # Check if it's a folder
        if os.path.isdir(speaker_folder):
            # Loop through each audio file in the speaker's folder
            for audio_file in os.listdir(speaker_folder):
                # Get full path of the original file
                original_file_path = os.path.join(speaker_folder, audio_file)
                
                # 
                if ".pt.pt" in original_file_path:
                    new_file_path = original_file_path.replace(".pt.pt", ".pt")
                    os.rename(original_file_path, new_file_path)
                    print(f"Renamed {audio_file} to {new_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_list", type=str, default="./filelists/train.txt", help="path to train list")
    parser.add_argument("--val_list", type=str, default="./filelists/val.txt", help="path to val list")
    parser.add_argument("--test_list", type=str, default="./filelists/test.txt", help="path to test list")
    parser.add_argument("--source_dir", type=str, default="./dataset/cmu_artic_16k/cmu_artic_ar_test", help="path to source dir")
    args = parser.parse_args()
    
    train = []
    val = []
    test = []
    idx = 0
    # rename_files()
    
    
    for speaker in tqdm(os.listdir(args.source_dir)):
        wavs = os.listdir(os.path.join(args.source_dir, speaker))
        # wavs=[speaker+'/'+x for x in wavs]
        shuffle(wavs)
        # train += wavs[2:-10]
        val += wavs[:50]
        test += wavs[-50:]
        
    # # shuffle(train)
    # shuffle(val)
    # shuffle(test)
            
    # # print("Writing", args.train_list)
    # # with open(args.train_list, "w") as f:
    # #     for fname in tqdm(train):
    # #         speaker = fname[:4]
    # #         wavpath = os.path.join("DUMMY", speaker, fname)
    # #         f.write(wavpath + "\n")
        
    print("Writing", args.val_list)
    with open(args.val_list, "w") as f:
        for fname in tqdm(val):
            speaker = fname.split('_')[0]
            wavpath = os.path.join("DUMMY", speaker, fname)
            f.write(wavpath + "\n")
            
    print("Writing", args.test_list)
    with open(args.test_list, "w") as f:
        for fname in tqdm(test):
            speaker = fname.split('_')[0]
            wavpath = os.path.join("DUMMY", speaker,fname)
            f.write(wavpath + "\n")
            