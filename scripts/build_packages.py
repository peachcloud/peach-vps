from utils import render_template

import subprocess
import os
import argparse

from constants import *


# parse CLI args
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debs", help="build release debs", action="store_true")
parser.add_argument("-b", "--binaries", help="build release binaries", action="store_true")
args = parser.parse_args()

# below is code for git updating the microservices, and building them (debs or binaries)
print("[ BUILDING AND UPDATING MICROSERVICE PACKAGES ]")
for service in SERVICES:
    service_name = service["name"]
    service_path = os.path.join(MICROSERVICES_SRC_DIR, service_name)
    print("[ BUILIDING SERVICE {} ]".format(service_name))
    subprocess.call(["git", "pull"], cwd=service_path)

    if args.binaries:
        subprocess.check_output(["/home/rust/.cargo/bin/cargo", "build", "--release", "--target=aarch64-unknown-linux-gnu"], cwd=service_path).decode("utf-8").strip()
        binary_path = "{}/target/aarch64-unknown-linux-gnu/release/{}".format(service_path, service_name)
        output_path = "/srv/peachcloud/releases/notplants/binaries/{}".format(service_name)
        print("{} -> {}".format(binary_path, output_path))
        subprocess.call(["cp", binary_path, output_path])

    if args.debs:
        debian_package_path = subprocess.check_output(["/home/rust/.cargo/bin/cargo", "deb", "--target", "aarch64-unknown-linux-gnu"], cwd=service_path).decode("utf-8").strip()
        output_path = "/srv/peachcloud/releases/notplants/debs/{}.deb".format(service_name)
        print("{} -> {}".format(debian_package_path, output_path))
        subprocess.call(["cp", debian_package_path, output_path])


print("[ BUILD PACKAGES COMPLETE ]")

