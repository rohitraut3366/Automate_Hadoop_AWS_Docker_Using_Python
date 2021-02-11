    import os
    # release branch /master branch /basa branch
def github():
    while True:
        print("""
            Enter 0: To check status of repository
            Enter 1: Initialize the git Repository
            Enter 2: Track the file. ADD in Statging Area
            Enter 3: Commit the Changes
            Enter 4: Get Time Line : versio [ reference ] Log
            Enter 5: Check Logs
            Enter 6: RollBack/Rollout the Version
            Enter 7: Show Branch
            Enter 8: Create Branch and Switch to new Branch
            Enter 9: Create New Branch
            Enter 10: To merge Branch
            Enter 11: To set Upstream Branch
            Enter 12: Add remote repository
            Enter 13: To push and Pull
            Enter 14: To see remote repository in verbose mode
            Enter 15: To fetch from remote repository
            Enter 16: Show Data at point in time
            Enter 17: To show Diff between two commits
            Enter 18: Discard the changes in file
            Enter 19: To see author and tree imformation about commit
            Enter 20: Clone repository
            Enter 21: merge final version of branch [merge(squash)]
            Enter 22: Rebase the branch
           ##n## Enter 23: Do the cherry-pick[get certain point-in-time backup data]
        """)
        Directory = input("Enter Repository[ Directory ] location: ")
        os.chdir(Directory)
        choice = input("Enter your choice: ")
        if choice == '0':
            os.system("git status")
        elif choice == '1':
            os.system("git init")
        elif choice == '2':
            add_option = input("Enter 1 : Add Spcecific File" 
                            "Enter 2 : Track All file") 
            if add_option == '1':
                os.system("git add .")
            elif add_option == '2':
                fileName= input("Enter File Name: ")
                os.system(f"git add {fileName}")
        elif choice == '3':
            commit_message = input()
            os.system(f"git commit -m {commit_message} .")
        elif choice == '4':
            branch = input("Enter branch name: ")
            os.system(f'git reflog {branch}')
        elif choice == '5':
            branch = input("Enter branch name: ")
            os.system(f'git log {branch}')
        elif choice == '6':
            commit_id = input("Enter commit Id: ")
            os.system(f"git reset {commit_id}")
            os.system("git checkout .")
        elif choice == '7':
            os.system("git branch -a")
        elif choice == '8':
            new_branch = input("Enter new branch name: ")
            os.system(f"git checkout -b {new_branch}")
        elif choice == '9':
            new_branch = input("Enter new branch name: ")
            os.system(f"git branch {new_branch}")
        elif choice == '10':
            Branch = input("Enter branch Name:")
            is_upstream = input(f"{branch} is upstream branch [y/n]: ")
            if is_upstream == 'n':
                os.system(f"git merge {Branch}")
            elif is_upstream == 'y':
                os.system(f'git pull')
            else:
                print('wrong choice')
        elif choice == '11':
            Branch = input("Enter branch Name:")
            os.system(f'git branch --set-upstream-to={Branch}')
        elif choice == '12':
            github_repo_url = input("Enter github repository url: ")
            repository_name = input("Enter local Reference Name for repository: ")
            os.system(f"git remote add {repository_name} {github_repo_url}")
        elif choice == '13':
            pull_push_choice = input('Enter pull/push: ')
            local_branch = input("Enter local branch name: ")
            remote_branch = input("Enter remote branch name: ")
            if pull_push_choice.lower() == 'pull':
                os.system(f"git pull {local_branch} {remote_branch}")
            elif pull_push_choice.lower() == 'push':
                os.system(f"git push {local_branch} {remote_branch}")
            else:
                print("wrong choice")
        elif choice == '14':
            os.system("git remote -v")
        elif choice == '15':
            remote_resitory = input("Enter remote repository name: ")
            local_branch = input("Enter local branch")
            os.system(f"git fetch {origin} {master}")
        elif choice == '16':
            commit_id = input("Enter commit Id: ")
            os.system(f"git show {commit_id}")
        elif choice == '17':
            commit_id_from_ref = input("Enter ref commit Id: ")
            commit_id_to_ref = input("Enter to compare commit Id: ")
            os.system(f"git diff {commit_id_from_ref} {commit_id_to_ref}")
        elif choice == '18':
            file = input("Enter file name: ")
            os.system(f"git restore {file}")
        elif choice == '19':
            commit_id = input("Enter commit Id: ")
            os.system(f"git cat-file -p {commit_id}")
        elif choice == '20':
            repository = input('Enter Repository url: ')
            os.system(f"git clone {repository}")
        elif choice == '21':
            Branch = input("merge to master branch name: ")
            os.system("git switch master")
            os.system(f"git merge --squash {Branch}")
        elif choice == '22':
            rebase_branch = input("Enter the branch that you want to rebase")
            os.system(f"git checkout {rebase_branch}")
            os.system("git rebase master")
        elif choice == '23':
            os.system()

