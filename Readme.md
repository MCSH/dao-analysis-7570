# Blockchain Data Analytics (7570)

The content of this repository is broken into different sections.

## writing

This includes the writing report of MakerDAO. We introduce you the relationships behind MakerDAO protocol, the effects beyond Bitcoin and Ethereum, and the analysis in this project.

## Resources (res)

This includes files generated by the code for the presentation and reports.

## Downloader (down)

This includes scripts developed by (sharm76) to gather transaction data from Etherscan

## Analytics (src)

This includes the analytical proces used to extract statistics and graphs from the data

* acts.py: Gathers data from mkr based on the Ethereum data
* mkr_concat: Concats the data into csv for easier analysis
* mkr_vis: Generate visualizations used in presentation and documents

**WARNING**: Running these scripts takes a lot of time and bandwith, and requires a lot of disk space. Please run with cautious

## Data (data)

This includes the data used in the processing algorithm.

There might be manual interventions required on the data, since its been developed by multiple parties and partially processed data has been 

**Due to size limitations imposed by Github, this folder has been replaced with a sample data, contact me if you need the full data**

the ByteCodeDecompiled are the byte codes of the smart contracts, the accounts are samples of what actions of an account look like and cdp is the account summary. Keep in mind that to keep things small we have shared only a sample of what this data looks like.
