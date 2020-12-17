# Welcome to MkDocs 

### A guide for using MkDocs with GitHub Pages.

For full documentation visit [mkdocs.org](https://www.mkdocs.org) and [github pages](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages).

## Package Install
All the contents of this website are edited with markdown format. The markdown files are then converted to static html pages via `Mkdocs` package. 

These commands will install the python dependencies onto a python environment. It is recommended that an anaconda or miniconda environment is used to easily edit markdown files using a code editor. 

```
pip install mkdocs
pip install pymdown-extensions
```

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Create GitHub Pages

#### Create new repo

Create on [Github](https://github.com/kj2431/useful_code/)

Then use GitHub Desktop or Terminal `git clone url` in desired folder

#### Initial Commit

```
cd useful_code

mkdocs new .
echo 'theme: readthedocs' >> mkdocs.yml

mkdocs serve
```

preview on http://127.0.0.1:8000


#### Deploying on GitHub Pages

```
echo 'site/' >>.gitignore
git add .
git commit -a -m 'first commit'
git push origin master

mkdocs gh-deploy
```

This should take a few minutes before the website is available.

Check [https://kj2431.github.io/useful_code/](https://kj2431.github.io/useful_code/)

If not available, then do the following:

1. Delete gh-pages branch
2. Make sure github pages source is none in the repo settings
3. Update mkdocs to latest version
4. Use `mkdocs gh-deploy` command once again
5. In a few minutes check if website exists; if not, delete repo and try again. 


## Tutorial for editing content

### Contribute Content
Write your contents in markdown format and save them in `/docs` folder, with file extention **.md**

### Organize Pages
Specify your content in `mkdocs.yml`, section `nav` as follows:
```
site_name: SITE_NAME
theme: readthedocs

TOPIC:
    - todo I: todo_I.md
    - todo II: todo_II.md
```
in which `TOPIC` will be top level folder, and `todo I` and `todo II` will be the second level pages


### Raise Pull Request
After the content editting is finished, remember to raise pull request for content merging especially if this is collaborative work.

### Markdown Format Specification
https://guides.github.com/features/mastering-markdown/


## Updating webpage 

* Organize all markdown files within the `docs` folder.
* Edit website navigation map by editing the `nav` section in `mkdocs.yml` as shown above.
* Verify rendering effect:    
  On your desktop computer, navigate to the root folder of this repo, type `mkdocs serve` in command line; this will start a website server locally on `127.0.0.1:8000`. Check to make sure the HTML page is rendered properly, and there are no formatting issues. Please note that when embedding an outside HTML file onto the markdown page, it must also follow HTTPS standards.
  
* Officially publish to Github pages    
  Type `mkdocs gh-deploy` in command line.
  
