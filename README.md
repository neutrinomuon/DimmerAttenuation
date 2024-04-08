# DimmerAttenuation
## Attenuation laws legacy software written in Fortran 2003+

**Author:** Jean Gomes

**Contact:**  
- Jean Gomes: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com)

last stable version: 0.0.1

<hr>

## About
DimmerAttenuation is a software program designed for absorption (ATTENUATION) in the UV/optical region with legacy Fortran 2003+ routines.

<hr>

<img src="https://skillicons.dev/icons?i=python,fortran,c,numpy&theme=light"><br>
<img src="https://img.shields.io/pypi/pyversions/DimmerAttenuation"><img src="https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/license.svg">

<hr>


## RESUME
<div align="left">
<img src="https://github.com/neutrinomuon/DimmerAttenuation/blob/main/figures/DimmerAttenuation.png" width="120">
</div>

<div align="center">
<img src="https://github.com/neutrinomuon/DimmerAttenuation/blob/main/figures/Reddening_Laws.png?raw=true" width="100%">
</div>


### Overview:

DimmerAttenuation is a flexible Python library tailored for utilizing legacy
Fortran 2003+ routines. These routines enable the correction of observed
spectra or emission lines through attenuation laws. Additionally,
DimmerAttenuation facilitates the application of attenuation to hypothetical
spectra, such as models. The code assumes a uniform dust screen model for the
dust absoprtion.

### Key Features:

Apply attenuation or correct attenuation of spectra or lines.

### Getting Started:

--------------------------------------------------------------------<br>
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)<br>

<hr>

#### <b>INSTALLATION</b>

You can easily install <a href=https://pypi.org/project/DimmerAttenuation/>DimmerAttenuation</a> by using pip - <a href='https://pypi.org/'>PyPI - The Python Package Index</a>:
<pre>
<code>
pip install DimmerAttenuation
</code>
</pre>
or by using a generated conda repository <a href='https://anaconda.org/neutrinomuon/DimmerAttenuation'>https://anaconda.org/neutrinomuon/DimmerAttenuation</a>:

[![badgetanaconda](https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/version.svg)](https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/version.svg)
[![badgetreleasedate](https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/latest_release_date.svg)](https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/latest_release_date.svg)
[![badgetplatforms](https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/platforms.svg
)](https://anaconda.org/neutrinomuon/DimmerAttenuation/badges/platforms.svg)
<pre>
<code>
conda install -c neutrinomuon DimmerAttenuation
</code>
</pre>
OBS.: Linux, OS-X ad Windows pre-compilations available in conda.

You can also clone the repository and install by yourself in your machine:
<pre>
<code>
git clone https://github.com/neutrinomuon/DimmerAttenuation
python setup.py install
</code>
</pre>

<hr>

#### <b>STRUCTURE</b>
<pre>
#################################################
workspace
├── .github
│   └── workflows
│       └── main.yml
├── .git
│   ├── shallow
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │       ├── pack-2948cd2dc148d43ec66c32e5f915f18a91249ec8.pack
│   │       ├── pack-2948cd2dc148d43ec66c32e5f915f18a91249ec8.rev
│   │       └── pack-2948cd2dc148d43ec66c32e5f915f18a91249ec8.idx
│   ├── hooks
│   │   ├── pre-receive.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── update.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── post-update.sample
│   │   ├── push-to-checkout.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-rebase.sample
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-push.sample
│   │   └── sendemail-validate.sample
│   ├── FETCH_HEAD
│   ├── info
│   │   └── exclude
│   ├── index
│   ├── branches
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   └── main
│   │       └── remotes
│   │           └── origin
│   │               └── main
│   ├── HEAD
│   ├── config
│   ├── refs
│   │   ├── tags
│   │   ├── heads
│   │   │   └── main
│   │   └── remotes
│   │       └── origin
│   │           └── main
│   └── description
├── README_setup.txt
├── version.txt
├── tree.out
├── showdown.min.js
├── dimmerattenuation.egg-info
│   ├── top_level.txt
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── PKG-INFO
├── README.md
├── tutorial
│   ├── .ipynb_checkpoints
│   │   ├── Untitled-checkpoint.ipynb
│   │   ├── Attenuation-checkpoint.ipynb
│   │   └── Untitled1-checkpoint.ipynb
│   ├── .jupyter_ystore.db
│   └── Attenuation.ipynb
├── setup.py
├── index.html
├── dist
│   └── dimmerattenuation-0.0.1.tar.gz
├── build
│   ├── lib.linux-x86_64-cpython-310
│   │   └── dimmerattenuation
│   │       ├── Reddening.py
│   │       ├── flib.cpython-310-x86_64-linux-gnu.so
│   │       └── __init__.py
│   ├── temp.linux-x86_64-cpython-310
│   │   ├── dimmerattenuation
│   │   │   └── moddatatype.mod
│   │   ├── ccompiler_opt_cache_ext.py
│   │   ├── build
│   │   │   └── src.linux-x86_64-3.10
│   │   │       ├── dimmerattenuation
│   │   │       │   ├── flib-f2pywrappers2.o
│   │   │       │   ├── flibmodule.o
│   │   │       │   ├── flib-f2pywrappers.o
│   │   │       │   └── flibmodule.o.d
│   │   │       └── build
│   │   │           └── src.linux-x86_64-3.10
│   │   │               └── dimmerattenuation
│   │   │                   ├── fortranobject.o
│   │   │                   └── fortranobject.o.d
│   │   ├── __pycache__
│   │   │   └── ccompiler_opt_cache_ext.cpython-310.pyc
│   │   └── src
│   │       └── fortran
│   │           └── Reddening
│   │               ├── CL_R_LawOPT.o
│   │               ├── O_Donnell94.o
│   │               ├── CAF__LawOPT.o
│   │               ├── J13__LawOPT.o
│   │               ├── S79__LawOPT.o
│   │               ├── Leitherer02.o
│   │               ├── CALR_LawOPT.o
│   │               ├── SPLINE1DArr.o
│   │               ├── DataTypes.o
│   │               ├── CCMR_LawOPT.o
│   │               └── H83gaLawOPT.o
│   └── src.linux-x86_64-3.10
│       ├── numpy
│       │   └── distutils
│       │       └── include
│       │           └── npy_cpu_dispatch_config.h
│       ├── dimmerattenuation
│       │   ├── flibmodule.c
│       │   ├── flib-f2pywrappers.f
│       │   └── flib-f2pywrappers2.f90
│       └── build
│           └── src.linux-x86_64-3.10
│               └── dimmerattenuation
│                   ├── fortranobject.h
│                   └── fortranobject.c
├── src
│   ├── fortran
│   │   └── Reddening
│   │       ├── Reddening_Laws.png
│   │       ├── CALR_LawOPT.cpython-39-darwin.so
│   │       ├── Leitherer02.cpython-39-darwin.so
│   │       ├── README.txt
│   │       ├── Reddening.py
│   │       ├── CAF__LawOPT.cpython-39-darwin.so
│   │       ├── SPLINE1DArr.compile
│   │       ├── S79__LawOPT.cpython-39-darwin.so
│   │       ├── SPLINE1DArr.f90
│   │       ├── H83gaLawOPT.f90
│   │       ├── CCMR_LawOPT.cpython-39-darwin.so
│   │       ├── Reddening_M1processor.compile
│   │       ├── O_Donnell94.cpython-39-darwin.so
│   │       ├── SPLINE1DArr.cpython-39-darwin.so
│   │       ├── README.md
│   │       ├── S79__LawOPT.f90
│   │       ├── Leitherer02.f90
│   │       ├── CALR_LawOPT.f90
│   │       ├── CL_R_LawOPT.cpython-39-darwin.so
│   │       ├── CAF__LawOPT.f90
│   │       ├── Reddening_M1processor.compile~
│   │       ├── CCMR_LawOPT.f90
│   │       ├── H83gaLawOPT.cpython-39-darwin.so
│   │       ├── CL_R_LawOPT.f90
│   │       ├── __pycache__
│   │       │   └── Reddening.cpython-39.pyc
│   │       ├── O_Donnell94.f90
│   │       ├── SPLINE1DArr_M1processor.compile
│   │       ├── Reddening.compile
│   │       ├── J13__LawOPT.f90
│   │       ├── J13__LawOPT.cpython-39-darwin.so
│   │       └── DataTypes.f90
│   └── python
│       ├── Reddening.py
│       └── __init__.py
└── figures
    ├── Reddening_Laws.png
    └── DimmerAttenuation.png

52 directories (0 symlink), 112 files (0 symlink)
#################################################
Generated: treehue_colored @2024 - © Jean Gomes -
#################################################
</pre>

<hr>

### Contributor

- Jean Gomes (Software Developer, Advisor): Jean is primarily responsible for
  the software development and implementation of DimmerAttenuation.

<table>

<tr><td align='center'><img width=50 src="https://github.com/neutrinomuon/PyDust/blob/main/figures/logs.jpg?raw=true"></td><td>LOGS</td></tr>

<tr><td>03/27/2024</td>

<td>J.G. submitted the routines to GitHub platform</td></tr>

</table>

<hr>

#### <b>LICENSE</b>

This software is provided "AS IS" (see DISCLAIMER below). Permission to use,
for non-commercial purposes is granted. Permission to modify for personal or
internal use is granted, provided this copyright and disclaimer are included
in ALL copies of the software. All other rights are reserved. In particular,
redistribution of the code is not allowed without explicit permission by the
author.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
