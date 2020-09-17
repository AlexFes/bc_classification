import os
import csv
import tarfile
from pathlib import Path

if __name__ == "__main__":
    data_dir = "data"
    Path(data_dir).mkdir(parents=True, exist_ok=True)

    tar = tarfile.open("bc.tgz")
    tar.extractall(data_dir)

    for item in tar:
        extracted = open("{}/{}".format(data_dir, item.name))
        reader = csv.reader(extracted, delimiter="\t")
        target = open("{}/{}.csv".format(data_dir, item.name[:-4]), "w")

        for row in reader:
            writer = csv.writer(target)
            writer.writerow(row)

        os.remove("{}/{}".format(data_dir, item.name))
