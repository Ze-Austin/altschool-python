# Hi there! :new_moon_with_face:

This is a repository containing all notes and files created while learning to work with Python (Flask) at [AltSchool Africa](https://altschoolafrica.com/schools/engineering).

**Please don't send pull requests**

**Caveat:** I use a MacBook, so the notes and files about installation and features might differ from what would apply to your computer. Trust [LMS](https://thealtschool.com/courses/backend-engineering-second-semesterpython), [Live Classes](https://youtube.com/playlist?list=PLTTmsZetDiwy6U7BZsTi17HkFFApgr9iZ) and [Google](https://google.com) for a better-tailored experience.

If you like this structure and want to use it for your own notes or just go through for tips and practice, follow these steps: 

1. Fork the original repo on GitHub
2. In your terminal, cd into the folder you use for AltSchool or Programming on your computer:  
    eg: `cd ~/AltSchool`
3. Clone the repo from your personal GitHub into the folder:  
    `git clone https://github.com/YourGitHubUsername/altschool-python`
4. Feel free to rename the cloned folder. This is entirely optional:  
    `mv altschool-python Python`
5. CD into the cloned folder:  
    `cd altschool-python` (or `cd Python` if renamed)
6. Add an upstream, which links to the original GitHub repo:  
    `git remote add upstream https://github.com/Ze-Austin/altschool-python`
7. Create and move into a new branch (preferably using your name or GitHub username for this repo):  
    `git checkout -b YourName`
8. Open the folder in your IDE to make your own notes and play with code files. Try it. Break it. Fix it. Repeat. To open the current folder in VSCode from the terminal:  
    `code .`
    - If this doesn't work, [google "add code to PATH"](https://www.google.com/search?q=add+code+to+path&oq=add+code+to+path)
9. When you're done for the session:
    - Stage your changes on git by adding them:  
        `git add .` or `git add file.name`
    - Then commit the staged changes:  
        `git commit -m 'message here'`
    - Alternatively, you can add and commit at once:  
        `git commit -am 'message here'`
10. Push the changes to *your branch*:  
    `git push origin branchname`
11. This is when you'll usually create a pull request on GitHub, but please don't. There's no point in merging everyone's personal notes
12. Get my weekly updates by pulling from the upstream:  
    `git pull upstream main`
13. Every time you want to work on this repo, ensure that you've checked out into your branch to freely make/edit your notes without affecting others:  
    `git checkout branchname`

**Timeline:** I usually update my branch (main) with notes and files from the week's LMS content by Wednesday evening. Caleb's folder (and any other Flask tutor's) will be updated when they drop files on Slack.

**Bonus:** There's a Git Cheat Sheet file in here. It helps with reminders and explanations of Git commands in the Terminal. Further explanation can be found online.

## Thanks for dropping by. Have fun! :snake:
