"""Code to test python instalation.

It gets values from the filesystem and the internet
to check that everything works.
"""

import json
import os
import platform
import requests

# LOCAL = os.path.dirname(os.path.realpath(__file__))
REMOTE = "../me/week1"

# print(os.getcwd(), LOCAL)


def check_system_details():
    """Look inside yourself.

    Gets the system details to check that this machine is actually set up
    """

    systemInfo = {
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "os_name": os.name,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "release": platform.release(),
        "system": platform.system(),
        "uname": platform.uname(),
        "version": platform.version(),
        "python_build": platform.python_build(),
        "python_compiler": platform.python_compiler(),
        "python_implementation(": platform.python_implementation(),
        "python_version(": platform.python_version(),
        "python_version_tuple": platform.python_version_tuple(),
        "cpu_count": os.cpu_count(),
    }
    print(json.dumps(systemInfo, indent=4))

    # Write it to a file in this repo
    f = open(os.path.join(REMOTE, "_checkID.json"), "w")
    f.write(json.dumps(systemInfo, indent=4))
    f.close()


def test_for_python_and_requests():
    """Inspect own filesystem.

    GETs a small JSON file and displays a message
    """
    width = 38

    gh_url = "https://raw.githubusercontent.com/"
    repo = "notionparallax/code1161base/"
    file_path = "master/week1/pySuccessMessage.json"
    url = gh_url + repo + file_path

    try:
        r = requests.get(url)
        message = json.loads(r.text)["message"]
        subMessage = "All hail his noodly appendage!"
    except Exception as e:
        message = "We are in the darkness"
        subMessage = "Alas, all is lost"
        print("\nThe error message:", e)

    bar = "*{s:{c}^{n}}*".format(n=width, c="*", s="")
    blank = "*{s:{c}^{n}}*".format(n=width, c=" ", s="")
    doesItWork = [
        bar,
        blank,
        "*{s:{c}^{n}}*".format(n=width, c=" ", s=message),
        blank,
        "*{s:{c}^{n}}*".format(n=width, c=" ", s=subMessage),
        blank,
        bar,
    ]

    print("Let's test Python and Requests:\n")
    for line in doesItWork:
        print(line)

    f = open(os.path.join(REMOTE, "_requestsWorking"), "w")
    for line in doesItWork:
        f.write(line + "\n")
    f.close()


if __name__ == "__main__":
    check_system_details()
    test_for_python_and_requests()
