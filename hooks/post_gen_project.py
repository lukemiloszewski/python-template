import subprocess

if __name__ == "__main__":
    if "{{ cookiecutter.init_git_repo }}" == "yes":
        subprocess.call(['git', 'init', '-b', 'main'])
