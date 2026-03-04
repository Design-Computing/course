# -*- coding: UTF-8 -*-
"""Tests for Set 1 - aboutMe.yml and GitHub setup.

These tests check the student's profile setup and Git configuration.
"""

import json
import os
import pytest
import requests
import git
from git import Repo
from PIL import Image
from ruamel.yaml import YAML
from colorama import Fore

EM = Fore.YELLOW
NORM = Fore.WHITE


@pytest.mark.set1
def test_about_me_filled_in(repo_path):
    """Test that aboutMe.yml has been updated with real information."""
    file_path = os.path.join(repo_path, "aboutMe.yml")
    
    if not os.path.isfile(file_path):
        pytest.fail(
            f"\n{EM}Can't find aboutMe.yml!{NORM}\n"
            "Have you deleted or renamed it? Don't do that!\n"
            "The file should be in the root of your me repository."
        )
    
    with open(file_path, "r", encoding="utf8", errors="ignore") as f:
        yaml = YAML(typ="rt")
        data = yaml.load(f)
    
    # Default values that students need to change
    default_name = "Your Name"
    default_student_number = "z1234567"
    default_github_username = "notionparallax"
    default_stack_overflow_link = "1835727/ben"
    
    # Check if any defaults are still present
    checks = [
        data.get("first_name", "") == default_name,
        data.get("studentNumber", "") == default_student_number,
        default_stack_overflow_link in data.get("stackOverflowLink", ""),
        data.get("github", "") == default_github_username,
    ]
    
    if any(checks):
        print(f"\n{EM}⚠️  You haven't updated all of your aboutMe.yml yet.{NORM}")
        print("\nYour current data (shown as JSON):")
        print(json.dumps(dict(data), indent=2, sort_keys=True))
        print(f"\n{EM}Please update these fields with your real information:{NORM}")
        if checks[0]:
            print("  • first_name")
        if checks[1]:
            print("  • studentNumber")
        if checks[2]:
            print("  • stackOverflowLink")
        if checks[3]:
            print("  • github")
        pytest.fail("aboutMe.yml needs to be updated with your real information")
    
    # All checks passed
    print(f"{Fore.GREEN}✓ aboutMe.yml looks good!{NORM}")


def get_origin_url(repo) -> str:
    """Get the origin URL of a git repository."""
    if os.name == "posix":
        repo_obj = Repo(repo.working_dir)
        return repo_obj.remotes.origin.url
    else:
        return repo.execute("git config --get remote.origin.url")


@pytest.mark.set1
def test_me_repo_is_clone(repo_path):
    """Test that the student is working on their own clone, not the source repo."""
    try:
        repo = git.cmd.Git(repo_path)
        origin_url = get_origin_url(repo)
    except Exception as e:
        pytest.fail(
            f"\n{EM}Couldn't check your git repository!{NORM}\n"
            f"Error: {e}\n"
            "Make sure you're in a git repository."
        )
    
    if "Design-Computing" in origin_url:
        pytest.fail(
            f"\n{EM}⚠️  You're working on the source repository!{NORM}\n"
            f"It looks like you've cloned {EM}Design-Computing/me{NORM}\n"
            f"You should have forked it first, then cloned {EM}[your_github_name]/me{NORM}\n"
            "You need to be working with your own fork.\n"
            "This is hard to explain in text - call a tutor over!"
        )
    
    print(f"{Fore.GREEN}✓ You're working on your own clone!{NORM}")
    print(f"   Origin: {origin_url}")


@pytest.mark.set1
@pytest.mark.api_call
def test_has_pushed_check_id(repo_path):
    """Test that checkID.json has been pushed to GitHub."""
    _test_has_pushed("checkID.json", repo_path)


@pytest.mark.set1
@pytest.mark.api_call
def test_has_pushed_requests_working(repo_path):
    """Test that requestsWorking.txt has been pushed to GitHub."""
    _test_has_pushed("requestsWorking.txt", repo_path)


def _test_has_pushed(file_name: str, repo_path: str):
    """Helper function to test if a file has been pushed to GitHub."""
    try:
        repo = git.cmd.Git(repo_path)
        origin_url = get_origin_url(repo)
        
        # Extract owner from URL
        # URLs can be like: https://github.com/owner/me.git or git@github.com:owner/me.git
        if "github.com" in origin_url:
            if origin_url.startswith("https"):
                owner = origin_url.split("/")[-2]
            else:  # SSH URL
                owner = origin_url.split(":")[-1].split("/")[0]
        else:
            pytest.skip("Not a GitHub repository")
        
        url = f"https://api.github.com/repos/{owner}/me/contents/set1/{file_name}"
        r = requests.get(url)
        
        if r.status_code == 404:
            pytest.fail(
                f"\n{EM}{file_name} not found on GitHub!{NORM}\n"
                f"Have you pushed your work yet?\n"
                f"Type {EM}git status{NORM} to check, then:\n"
                f"  1. {EM}git add set1/{file_name}{NORM}\n"
                f"  2. {EM}git commit -m \"Add {file_name}\"{NORM}\n"
                f"  3. {EM}git push{NORM}"
            )
        elif r.status_code == 200:
            print(f"{Fore.GREEN}✓ {file_name} has been pushed to GitHub!{NORM}")
        else:
            pytest.fail(
                f"\n{EM}Unexpected response from GitHub API{NORM}\n"
                f"Status code: {r.status_code}\n"
                f"This might be a rate limit or authentication issue."
            )
    except Exception as e:
        pytest.fail(
            f"\n{EM}Error checking if file was pushed{NORM}\n"
            f"Error: {e}"
        )


@pytest.mark.set1
@pytest.mark.api_call
@pytest.mark.slow
def test_has_real_photo(repo_path):
    """Test that the student has a real photo on their GitHub profile."""
    try:
        repo = git.cmd.Git(repo_path)
        origin_url = get_origin_url(repo)
        
        # Extract owner from URL
        if "github.com" in origin_url:
            if origin_url.startswith("https"):
                owner = origin_url.split("/")[-2]
            else:  # SSH URL
                owner = origin_url.split(":")[-1].split("/")[0]
        else:
            pytest.skip("Not a GitHub repository")
        
        image_url = f"https://github.com/{owner}.png?size=40"
        img_data = requests.get(image_url).content
        file_name = "avatar_temp.jpg"
        
        with open(file_name, "wb") as handler:
            handler.write(img_data)
        
        image = Image.open(file_name)
        colour_count = len(set(image.getdata()))
        
        if colour_count > 10:
            # Likely a real photo
            im = image.convert("P", palette=Image.Palette.ADAPTIVE, colors=9)
            block_image = _blocky_photo(im, width=60)
            print(f"{Fore.GREEN}✓ You have a real photo!{NORM}")
            print(block_image)
            os.remove(file_name)
            return
        else:
            # Probably default avatar
            block_image = _blocky_photo(image)
            os.remove(file_name)
            pytest.fail(
                f"\n{EM}Your GitHub profile picture only has {colour_count} colours.{NORM}\n"
                "This makes me think it's the default avatar.\n"
                f"Not like this:\n{block_image}\n"
                "But like this:\n"
                "╭───────────╮\n"
                "│  !!!!!!!  │\n"
                "│ /       \\ │\n"
                "│ │  O  O │ │  ⇇ A photo of YOUR face!\n"
                "│<│    v  │>│\n"
                "│  \\  ─── / │\n"
                "│   \\____/  │\n"
                "╰───────────╯\n\n"
                f"{EM}Action required:{NORM}\n"
                "Go to https://github.com/settings/profile and upload a photo of your face.\n"
                "This really helps us understand who's who and be more useful in tutorials."
            )
    except Exception as e:
        pytest.fail(
            f"\n{EM}Error checking GitHub profile photo{NORM}\n"
            f"Error: {e}"
        )


def _blocky_photo(image, width=20):
    """Convert an image to ASCII art."""
    colour_map_list = list(
        zip(
            list(set(image.getdata())),
            ["█", "░", "▒", "▓", "X", "#", "%", "/", ":", "*"],
        )
    )
    colour_map = {x[0]: x[1] for x in colour_map_list}
    image = image.resize((width, int(width / 2)), Image.Resampling.NEAREST)
    pixels = list(image.getdata())
    width, height = image.size
    block_image = ""
    for i in range(len(pixels)):
        block_image += colour_map[pixels[i]]
        if (i + 1) % width == 0:
            block_image += "\n "
    return block_image
