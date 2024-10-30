# Git Commands Cheat Sheet

A collection of commonly used Git commands for setting up, managing, and collaborating on GitHub repositories.

---

## 📁 Setting Up & Configuration

### `git config`
Configure Git settings, such as user name and email.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"


---

## 🔄 Basic Commands

### `git init`
Initialize a new Git repository in the current directory.

```bash
git init
```

### `git clone`
Clone a repository from GitHub to your local machine.

```bash
git clone https://github.com/username/repository.git
```

### `git status`
Show the status of changes in the working directory and staging area.

```bash
git status
```

---

## 📝 Staging and Committing

### `git add`
Add changes in files to the staging area. Use `.` to add all files.

```bash
git add <file>
git add .
```

### `git commit`
Commit changes in the staging area with a message describing the update.

```bash
git commit -m "Commit message"
```

### `git commit --amend`
Modify the last commit message or add changes to the last commit.

```bash
git commit --amend -m "Updated commit message"
```

---

## 🌿 Branching

### `git branch`
List, create, rename, or delete branches.

```bash
git branch           # Lists all branches
git branch new-branch # Creates a new branch
```

### `git checkout`
Switch branches or restore files. Use `-b` to create a new branch and switch to it.

```bash
git checkout new-branch     # Switch to 'new-branch'
git checkout -b new-branch  # Create and switch to 'new-branch'
```

### `git switch`
A newer command to switch branches.

```bash
git switch new-branch
git switch -c new-branch # Create and switch to 'new-branch'
```

---

## 🔄 Merging and Rebasing

### `git merge`
Merge another branch into the current branch.

```bash
git merge branch-to-merge
```

### `git rebase`
Move or combine commits from one branch onto another.

```bash
git rebase main
```

---

## 🔗 Synchronizing with GitHub

### `git remote`
Manage connections to remote repositories.

```bash
git remote add origin https://github.com/username/repository.git
```

### `git push`
Send commits to a remote repository. Use `-u` to set the upstream for the branch.

```bash
git push origin main
git push -u origin new-branch
```

### `git pull`
Fetch and merge changes from a remote branch into the current branch.

```bash
git pull origin main
```

### `git fetch`
Download changes from a remote repository without merging.

```bash
git fetch origin
```

---

## ❌ Undoing Changes

### `git reset`
Move the current branch to a different commit.

```bash
git reset <commit>           # Reset to a specific commit
git reset --hard <commit>    # Discard all changes after the commit
git reset --soft <commit>    # Keep changes staged
```

### `git revert`
Create a new commit that undoes the changes of a specific commit.

```bash
git revert <commit>
```

### `git restore`
Restore files to their previous state.

```bash
git restore <file>          # Discard changes in the working directory
git restore --staged <file> # Unstage changes
```

---

## 📜 Logs and History

### `git log`
Show the commit history with details about each commit.

```bash
git log
git log --oneline
```

### `git diff`
Compare changes between commits, branches, or working states.

```bash
git diff                    # Show changes in the working directory
git diff --staged           # Show changes in the staging area
git diff main new-branch    # Compare two branches
```

---

## 🔧 Advanced Commands

### `git stash`
Temporarily save changes that aren’t ready to commit.

```bash
git stash           # Stash uncommitted changes
git stash apply     # Reapply stashed changes
git stash drop      # Discard the latest stash
```

### `git tag`
Mark a specific commit with a tag, often used for versioning.

```bash
git tag v1.0.0          # Tag the current commit with a version
git push origin v1.0.0  # Push the tag to the remote
```

---

## 🤝 Collaboration & Review

### `git cherry-pick`
Apply a specific commit from one branch to another.

```bash
git cherry-pick <commit-hash>
```

### `git blame`
Show who last modified each line of a file.

```bash
git blame <file>
```

---

This cheat she et covers essential Git commands for setting up repositories, managing branches, synchronizing with GitHub, and collaborating effectively.
```
