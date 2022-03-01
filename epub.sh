toolboxPath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
[[ $readerPath ]] || {
    echo "Set a environmental variable \"readerPath\" to continue..."
    exit
}
[[ -x $toolboxPath/docpub ]] || {
    echo "Docpub is not executable, try \"chmod +x $toolboxPath/docpub\" and continue..."
    exit
}
cd "$readerPath"

processPDF() {
    echo "Processing book $2..."
    docker run -ti --rm -v `pwd`:/temp dodeeric/pdf2epubex pdf2epubEX $1
    [[ ! -e 'mybook.pdf' ]] || rm mybook.pdf
    for outputFile in *.epub
    do
        [[ -f "$outputFile" ]] || continue
        mv $outputFile 'toMerge.epub'
    done
    $toolboxPath/docpub -f epub -o . "$1" --fname 'index.epub'
    python3 $toolboxPath/merge.py 'toMerge.epub' 'index.epub' "$2"
    mv $1 '../PDF Archives'
    mv "$2.epub" '..'
}

for file in *.pdf
do
    [[ -f "$file" ]] || continue
    processPDF $file "${file%.pdf}"
done
