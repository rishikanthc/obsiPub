import fire

from obsipub import md


def main():
    fire.Fire()


def to_html():
    fpath = "/Users/rishi/Code/cookiejar/obsipub/md/wezterm.md"

    obj = md.parse_md_file(fpath)

    if obj is not None:
        print(obj["front_matter"])
        print(obj["html_content"])

    else:
        raise ValueError("Failed")
