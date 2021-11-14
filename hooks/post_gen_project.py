import subprocess

if __name__ == "__main__":
    if "{{ cookiecutter.init_git_repo }}" == "yes":
        subprocess.call(['git', 'init', '--branch', 'main'])
        subprocess.call(['git', 'add', '--all'])
        subprocess.call(['git', 'commit', '--message', "🎉 Initial commit"])
