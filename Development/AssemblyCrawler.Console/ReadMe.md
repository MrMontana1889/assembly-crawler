# How to generate python stub (*.pyi) file 

There are two ways to generate stub files.

1. With .config file, and
2. Without .config file

## Generate *.pyi files using .config file

This approach provides the best options as the config file gives greater flexibility.
Steps:

* Create a config file.
* Feed the config file to the `assembly-crawler`
	* Using Visutal Studio: Modify the 'launchSettings.json' and debug using Visutal Sudio.
	* Using Command Line: `AsseblyCrawler.Console.exe -c "Path\To\ConfigFile.config"`


## Generate *.pyi files from command line

This approach is nice to build the confidence and later build a config file.

* `AsseblyCrawler.Console.exe -a "Path\To\Assembly.dll" -x "Patah\To\The\DocString.xml" -o "Path\Where\Output\Will\Be\Generated\"`
* In absense of xml doc-string give an empty path, `-a "..." -x "" -o "..."`

