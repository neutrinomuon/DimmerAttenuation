There are different ways of compiling throught a mac M1 processor. In my computer it only works if I set the path and install gcc, gfortran through macports.

EXAMPLE of how to compile:

CFLAGS="-I/Library/Developer/CommandLineTools/SDKs/MacOSX12.3.sdk/usr/include" f2py --opt='-O0' -c DataTypes.f90 CAF__LawOPT.f90 -m CAF__LawOPT
