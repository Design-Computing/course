# -*- coding: UTF-8 -*-
"""Tests for Set 1 - System Setup and Hello World.

This set checks that the student's environment is set up correctly
and that they can print "Hello world!".
"""

import json
import os
import platform
import re
import inspect
import pytest
import requests
from colorama import Fore

EM = Fore.YELLOW
NORM = Fore.WHITE


@pytest.mark.set1
def test_system_details(repo_path):
    """Check system details and create checkID.json file."""
    system_info = {
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
        "python_implementation": platform.python_implementation(),
        "python_version": platform.python_version(),
        "python_version_tuple": platform.python_version_tuple(),
        "cpu_count": os.cpu_count(),
    }
    
    # Print system info for student
    print("\n📊 Your system details:")
    print(json.dumps(system_info, indent=4, default=str))
    
    # Write to checkID.json
    json_path = os.path.join(repo_path, "set1", "checkID.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(system_info, f, indent=4, default=str)
    
    assert os.path.isfile(json_path), "checkID.json should be created"


@pytest.mark.set1
@pytest.mark.api_call
def test_python_and_requests(repo_path):
    """Test that Python and Requests module work by fetching a message."""
    width = 38
    gh_url = "https://raw.githubusercontent.com/"
    check_repo = "notionparallax/code1161base/"
    file_path = "master/week1/pySuccessMessage.json"
    url = f"{gh_url}{check_repo}{file_path}"
    
    try:
        r = requests.get(url)
        message = json.loads(r.text)["message"]
        sub_message = "All hail his noodly appendage!"
    except Exception as e:
        pytest.fail(
            f"\n{EM}Failed to fetch success message!{NORM}\n"
            f"Error: {e}\n"
            f"This might be a network issue or the URL might be down."
        )
    
    boundary_char = "🍝"
    bar = f"{boundary_char}" * (int(width / 2) + 2)
    blank = "{b}{s:{c}^{n}}{b}".format(n=width, c=" ", s="", b=boundary_char)
    does_it_work = [
        bar,
        blank,
        "{b}{s:{c}^{n}}{b}".format(n=width, c=" ", s=message, b=boundary_char),
        blank,
        "{b}{s:{c}^{n}}{b}".format(n=width, c=" ", s=sub_message, b=boundary_char),
        blank,
        bar,
    ]
    
    print("\n🐍 Python and Requests are working!")
    for line in does_it_work:
        print(line)
    
    # Write to requestsWorking.txt
    output_path = os.path.join(repo_path, "set1", "requestsWorking.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for line in does_it_work:
            f.write(f"{line}\n")
    
    assert os.path.isfile(output_path), "requestsWorking.txt should be created"


@pytest.mark.set1
def test_hello_world(load_exercise, repo_path):
    """Test that exercise 1 prints 'Hello world!'."""
    exercise1 = load_exercise(set_number=1, exercise_number=1, path=repo_path)
    source = "".join(inspect.getsourcelines(exercise1)[0])
    
    # Check for exact match first
    if "print('Hello world!')" in source or 'print("Hello world!")' in source:
        print(f"{Fore.GREEN}✨ That's exactly right! Nice one. 🕺{NORM}")
        assert True
        return
    
    # Check for close match
    regex = r"print *\([\"'][Hh]ello +[Ww]orld!*[\"']\)"
    rough_match = re.search(regex, source)
    
    if rough_match:
        print(
            f"{EM}⚠️  This is close enough to pass, but it's not EXACTLY right.{NORM}\n"
            "Sometimes it really matters what you write.\n"
            f"Be pedantic! It should be exactly:\n{EM}print('Hello world!'){NORM}"
        )
        assert True
    else:
        pytest.fail(
            f"\n{EM}We're looking for:{NORM}\n\n"
            f"{EM}    print('Hello world!'){NORM}\n\n"
            f"But your code is:\n{'═' * 80}\n{EM}{source}{NORM}\n{'═' * 80}\n"
            f"Look carefully at your capitalisation, spelling, brackets, spaces, etc."
        )


@pytest.mark.set1
def test_check_id_exists(repo_path):
    """Test that checkID.json exists."""
    file_path = os.path.join(repo_path, "set1", "checkID.json")
    assert os.path.isfile(file_path), (
        "checkID.json should exist in set1/ directory.\n"
        "It should have been created by the system details test."
    )


@pytest.mark.set1
def test_requests_working_exists(repo_path):
    """Test that requestsWorking.txt exists."""
    file_path = os.path.join(repo_path, "set1", "requestsWorking.txt")
    assert os.path.isfile(file_path), (
        "requestsWorking.txt should exist in set1/ directory.\n"
        "It should have been created by the Python and Requests test."
    )
