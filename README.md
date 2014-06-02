rmv
===
Example commands:

    rmv train_dir
    rmv -g "*.jpg" test_dir
    rmv -p 70 ~/downloads

Usage:

    usage: rmv [-h] [-p PERCENT] [-g GLOB] [source] dest

    Randomly moves files to a directory

    positional arguments:
      source
      dest

    optional arguments:
      -h, --help            show this help message and exit
      -p PERCENT, --percent PERCENT
                            The percent of the directory to move, default is 50
      -g GLOB, --glob GLOB  filters the list of files to move
