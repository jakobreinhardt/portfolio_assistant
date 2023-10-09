### Table of Contents

1. [Project Description](#description)
2. [Installation](#installation)
3. [File Descriptions](#files)
4. [Credits](#credits)


## Project Description <a name="description"></a>

The motivation behind this project is to have a program that can be used to compare fundamentals for different assets. Furthermore, github actions functionality runs scheduled pipelines for the lengthy process of metrics retrieval.

-------------

## Installation <a name="installation"></a>

Use Python versions 3.10.8 or higher

These additional packages are needed:

- yahoofinancials: https://pypi.org/project/yahoofinancials/

-------------
## File Descriptions <a name="files"></a>

- main.py : CLI program that offers the full range of functions. The user can manually navigate through single asset to multiple asset and full portfolio analysis.

- ciscript.py : Executes the metrics retrieval for full portfolio and is executed in CI pipeline.

- functions.py : This module includes the custom functions.

- classes.py : Module that includes classes such as the parent Asset class. Currently unused.

- trials.py : Is a file of testcode that you do not need to bother with.

- /data : Includes data of stocks either as input to or output of the pipelines.

- /.github/workflows/actions.yml : CI/CD file to run a pipeline that retrieves metrics for all assets.

- environment.yml : Environment info to execute the full range of functions locally.

- requirements.txt : Package requirements for github workflow.
-------------

## Credits <a name="credits"></a>

Resources and APIs that helped me in the creation of the project:

- https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4

- https://www.openfigi.com/api

- https://money.stackexchange.com/questions/2940/how-to-map-stock-ticker-symbols-to-isin-international-securities-identification
