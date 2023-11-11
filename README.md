<a name="readme-top"></a>

# m6A-RNA-Modification-Prediction :dna:

**Table of contents:**
- [About The Project](#about-the-project)
- [Installation](#installation)
  - [a) Create an isolated environment](#a-create-an-isolated-environment)
  - [b) Setup a sync copy of the project repository](#b-setup-a-sync-copy-of-the-project-repository)
  - [c) Run the test script](#c-run-the-test-script)



## About The Project :page_with_curl:

m6A represents a chemical modification that can occur in RNA molecules, impacting their chemical and physical attributes, especially in the context of 5-mer nucleotides. This modification has been associated with the onset of cancer, highlighting its potential as a diagnostic tool for detecting cancer in its early stages. The project leverages data from Nanopore Sequencing, a technology capturing characteristic changes in current, known as RNA-Seq signals, and measuring dwelling time (signal length) as RNA molecules traverse the nanopore. The primary objective of this project is to employ advanced machine learning techniques to accurately predict and identify m6A modifications.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Installation :desktop_computer:

To get a copy up and running on your AWS Ubuntu machine follow these simple steps (We encourage you to use an instance with robust CPU settings)


### a) Create an isolated environment

Change directory into /ProjectStorage

```
$ cd ~/studies/ProjectStorage/
```

Download Miniconda Installer

```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
```

Run Miniconda Installer

```
$ bash miniconda.sh -b -p $HOME/miniconda
```

Set up conda command in the current shell session

```
$ source $HOME/miniconda/etc/profile.d/conda.sh
```

Initialize Conda

```
$ conda init
```

Activate conda commands in the current terminal session

```
$ source ~/.bashrc
```

Create a virtual environment (You can replace myenv with any name you prefer)

```
$ conda create --name myenv python=3.8
```

Activate the virtual environment

```
$ conda activate myenv
```
### b) Setup a sync copy of the project repository

Clone the current repo

```
$ git clone https://github.com/bce99/m6A-RNA-Modification-Prediction.git
```

Change directory into the project folder

```
$ cd m6A-RNA-Modification-Prediction/
```

Install the required packages

```
$ pip install -r requirements.txt
```
### c) Run the test script

Test run the project (This may take some time depending on your CPU)

```
$ python run_test.py
```

After this you will see a new file 'Test_Data2_Result.csv' appearing in your current directory. This is the successfully generated test run prediction.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


