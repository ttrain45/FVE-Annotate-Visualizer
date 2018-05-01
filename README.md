# FVE-Annotate-Visualizer
A visualization tool written for Fast Virome Explorer Annotate

# Requirements
- Python 2.7
- Pandas
- Matplotlib
- Tkinter

# Running FVE-Annotate-Visualizer
After installing all the requiremnts running this program is simple. Simply run the command
```bash
$ pathToPython2.7/python.exe pathToVisualizer/FVE-Annotate-Visualizer.py
```
Once the visualizer has loaded it wil ask for a file location. This location should be where you had the output of FVE-Annotate save to. More specifically the folder where your scaffold files are located.

+-- desired folder

  +-- scaffold-0

    +-- blastp-output.txt

    +-- gens.coords.gbk

    +-- scaffold-0.fasta

    +-- scaffold-0.fasta.fai

    +-- scaffold-0-proteins.faa

  +-- scaffold-1...

