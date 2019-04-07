import os
dir = "../../CLionProjects/redis/src"
prefix = "${SRC}"
for file in sorted(os.listdir(dir)):
    print("{}/{}".format(prefix, file))