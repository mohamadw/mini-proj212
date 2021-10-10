# Name violations in Palestine
# Part 1 :
## downloader.py : 
goes through 120,000 files in the "State Archives" and claims only The "Government Names Committee" starting from the year 1948 
## output :
 Archives folder that contain:
1. Attachment : Contains only the visible files.
2. DataAnalysis : Contains information analysis for all files:
    - png.DocSource: A diagram describing the documentation sources of files that found.
    - Status & Types.png: A diagram depicting what percentage of the files are visible or partially exposed or hidden.
    - Table.docx : every line describes a file and contains 5 fields : file name, material period from,
Material period up to, exposure status and file type.
   
3. MetaData: This contains the JSON files that describe all the files.

# part 2 :

After running the code from the first part, we went through the collection of downloaded files and selected
(File number to quote: ISA-PMO-GovNamesCommittee-000dgna)
 which We read it using Transkribus, and extracted from it the original Arabic names.
 The following is the link to the case in question:
https://www.archives.gov.il/archives/Archive/0b07170680020246/File/0b0717068080987a.

From this file we get 1823 places in southern Palestine.The output in files:
- Map names list.xlsx
- Names list 1.xlsx
- Names list 2.xlsx

# Transktibus 
is a software that reads documents with an accuracy of about 90%, and turns them over
For digital text. The mistakes can be corrected manually.
