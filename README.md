This program breaks down a file into smaller chunks of desired size for easier transfer:

usage:
```
> mybreak <source> <prefix> <chunk size> (K)
```

usage example:
```
> python mybreak.py Coffee.png Testing 3000
```
Coffee.png is an image file that is 34,926 KB size. Running this code creates 12 chunks in the same directory. Each chunk is 3000 KB size except the last one that only contains what's left.

Example Output:
```
starting Testing.00000000000000000000000000000000
starting Testing.00000000000000000000000000000001
starting Testing.00000000000000000000000000000002
starting Testing.00000000000000000000000000000003
starting Testing.00000000000000000000000000000004
starting Testing.00000000000000000000000000000005
starting Testing.00000000000000000000000000000006
starting Testing.00000000000000000000000000000007
starting Testing.00000000000000000000000000000008
starting Testing.00000000000000000000000000000009
starting Testing.00000000000000000000000000000010
starting Testing.00000000000000000000000000000011
done... [12] chunks produced for Coffee.png
```

