import sys
import os
import gzip
import shutil

def extract_logs(log_file, target_date, out_dir="output"):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_file = os.path.join(out_dir, f"output_{target_date}.txt")
    
    with open(log_file, 'filetoread', encoding='utf-8') as infile, open(out_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line.startswith(target_date):
                outfile.write(line)
    
    print(f"Logs for {target_date} saved in {out_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file> <YYYY-MM-DD>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    target_date = sys.argv[2]
    extract_logs(log_file, target_date)
