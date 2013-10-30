# HUsyntactic

Author		:	Minh-Hoang, Nguyen

Email		: 	hoangnm[dot]53[at]gmail[dot]com

Description	:
			A syntactic analyzer uses CYK algorithm and 
			Earley algorithm


##HOW TO USE?

You can use command:
```
$ python HUsyntactic.py -a [c|e] -g grammarFile -l lexiconFile -s sentenceFile -o outFile
	
	-a : type of algorithm.
		c for cyk
		e for earley
	-g : name of file contains grammar rules
	-l : name of file contains lexcicon rules
	-s : name of file contains sentences
	-o : name of output file
```


###Example:
```
$ pwd
HUsyntactic/src
$ python HUsyntactic.py -a c 
                        -g data/ckyData/GRAMMAR.IN 
                        -l data/ckyData/LEXICON.IN 
                        -s data/ckyData/SENTENCES.IN -o data/ckyData/OUTFILE.OUT

```

##DOCUMENTATION
Please see HUsyntactic.pdf ( It's in Vietnamese! )

##LICENSE
  All HUsyntactic source files are made available under the terms of the
  GNU Affero General Public License (AGPL).  See GNU-AGPL-3.0 files for
  details.
