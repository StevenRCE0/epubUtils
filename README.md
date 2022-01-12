# epubUtils
This is a rough tool helping me converting all sorts of PDFs to EPUBs. 

## Usage
Firstly, find a proper location for all the stuff, and structure the directories like this:

> *somewhere*<br>
> ├── PDF Archives<br>
> └── Pending

Then add the root directory to environmental variable $readerPath, like:

    export readerPath=somewhere
    
Finally, put your PDFs under "Pending" folder, and run:
    
    ./epub.sh

## Dependencies
This program needs python3 and Docker to run.  
Thanks for [pdf2epubEX](https://github.com/dodeeric/pdf2epubEX) for most of the jobs, and PDFTron for the handy docpub utility generating index file. 
