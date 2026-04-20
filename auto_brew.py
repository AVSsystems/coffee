import time
import math

def start_extraction(seconds):
    print(f"Extraction started for {seconds} seconds...")
    time.sleep(seconds)
    print("Extraction complete. Enjoy your AVS-blend.")

if __name__ == "__main__":
    # Standard AeroPress timing
    start_extraction(120)
