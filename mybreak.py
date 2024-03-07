import sys
import os

def main():
    if len(sys.argv) != 4:
        print(f"argc = {len(sys.argv)} => usage: mybreak <source> <prefix> <chunk size> (K)")
        sys.exit(1)

    chunk_size = 1024 * int(sys.argv[3])

    if chunk_size <= 0 or chunk_size > (1024 * 1024 * 1024):
        print(f"Chunk size error. {chunk_size} needs to be between 1 (1 KB) and {1024 * 1024} (1 GB)")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'rb') as f:
            i = 0
            while True:
                # fname = prefix.32numbers including i
                # example Prefix.00000000000000000000000000000005
                fname = f"{sys.argv[2]}.{str(i).zfill(32)}"
                with open(fname, 'wb') as tf:
                    print(f"starting {fname}")
                    # Read from f and write to tf, 8 bytes at a time
                    # Each time the loop is iterated the file pointer is advanced 8 bytes
                    for _ in range(chunk_size // 8):
                        ccc = f.read(8)
                        if not ccc:
                            print(f"done... [{i+1}] chunks produced for {sys.argv[1]}")
                            sys.exit(0)
                        tf.write(ccc)

                i += 1

    except FileNotFoundError:
        print(f"file {{{sys.argv[1]}}} can not be opened...")

if __name__ == "__main__":
    main()