# Example repository (Python)

This git repository is a minimal example to show how to structure a Python
package, how to use document function to visulize your prelimilary results 
and how to use GitHub Actions to automatically run tests and build
documentation for your software.

A well structured python project contains the following:
```bash
\docs               # the directory to generate the documents
\scripts            # your scripts to do processing or ploting.
\src                # the codes you wanna make as your own package. 
\test               # the codes to test the functions in `src`
.gitignore          # tell git changes of what files are not tracked.
environment.yml     # the files contain the environment configrations
LICENSE             # license file (MIT)
README.md           # this file
requirements.txt    # the packages required to install your own package.
setup.py            # to install your own package
```


## Step 1: create the environment


Create a new environment with all dependencies and make it the active environment
> change the files here to have the proper name, and include all the packages your 
project needed. 
```sh
conda env create -f environment.yml
conda activate python_example   # the name in the file
```
> In VS code, the environment for the scripts can be changed by type `shift+command+p`,
> and type `Python: select interpreter`. The environment for the jupyter notebook can
> be changed with the 'phone' button on the right upper.
Inspect information about the environment and list all installed packages
```sh
conda info
conda list
```

## Step 2: make your own code in `\src` as package

Making the frequently used codes as package. In this example, `data_generator.py` and 
`md_generator.py` are made as the source code, by including a file `__init__.py` in the 
same directory and run the following bash in the root directory. `-e` make the source 
code editable. 
```sh
python3 -m pip install -e .
```

## Step 3: run tests

'No test no code', simple example should be checked in `\test` directory. 
Run the test suite
```sh
pytest .
```

## Step 4: run your script in `\scripts`
In the example, two files are included. `make_plot.py` generate the example plots. which
saves the plots under the `docs\source\plots'. 
```bash
cd scripts
python make_plot.py
```

`generate_md.py` generate the markdown file with python, inclxuding the plots just created
in the last step into a markdown note. The markdown files can also be hand made by creating 
the new file ending with `.md`. In order to convert the markdown files into html, all
markdown files neeed to be under the `\docs` directory. 
```bash
python generate_md.py
```

## Step 5: build documentation

Auto-generate documentation. 
`conf.py` already incldued the necessary extentions to convert markdown files into html files. 
`index.rst` files should be changed to include all the markdown files that you wanna convert 
into html files. 
```sh
cd docs/
make html
```
The generated HTML files are stored in ` docs/build/html`.

## Step 6: upload html and build webpage

Two ways to build your webpage with your prelimilary results.

**The first way** is to use `GitHub Page`. This project include a [ci.yml](https://github.com/liuquan18/html_example/blob/393fdd8b83b339c7f0ea48b9a4388d8efb2678b2/.github/workflows/ci.yml#L1) to aumatically
build the webpage. When commits are pushed or merged to the remote repository, a new version of
the documentation is build and published on
[GitHub pages](https://liuquan18.github.io/html_example/).

**The second way** for the DKRZ users, who has the swift account on levante. the following bash files named as `upload_html.sh` could be included in the `docs` directory
```bash
#!/bin/bash
# activate environment
conda activate TelSeason
module load py-python-swiftclient

# go to 
cd /docs
# upload
swift upload python_example build # change the name of the container here
```
then run the script on levante to upload the html files onto swift. 
```bash
cd docs
./upload_html.sh
```
You can use swiftbrowser to check the files. To make the html as a webpage, the container need be chaged into a public. then the webpage is built [here](https://swift.dkrz.de/v1/dkrz_e2efc288-3ba0-499b-9bd8-d1a2580fd987/python_example/build/html/index.html) 
> Note that the link the different from just copying the link from swift_browser. Update the link above 
with the correct URL when you set the container on swift as public. 
---

Further information
* [Setuptools - library to facilitate packaging Python projects](https://setuptools.pypa.io)
* [Sphinx - Python documentation generator](https://sphinx-doc.org)
* [pytest - A full-featured Python testing framewor](https://docs.pytest.org)
* [GitHub Actions - automate your software workflows](https://github.com/features/actions)
* [GitHub Pages - Host web sites directly from your repository](https://pages.github.com)
* [DKRZ swift object storage](https://docs.dkrz.de/doc/datastorage/swift/index.html)
