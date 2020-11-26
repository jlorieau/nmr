#!/bin/csh

nmrPipe -in test.fid \
| nmrPipe  -fn SOL                                    \
| nmrPipe  -fn SP -off 0.4 -end 0.98 -pow 1 -c 0.5    \
| nmrPipe  -fn ZF -size 4096                               \
| nmrPipe  -fn FT                                     \
| nmrPipe  -fn EXT -x1 11.5ppm -xn 6.5ppm -sw -verb   \
| nmrPipe  -fn PS -p0 200.4 -p1 162. -di             \
#| nmrPipe  -fn PS -p0 0.0 -p1 0.0 -di             \
| nmrPipe  -fn POLY -ord 2         \
| nmrPipe  -fn TP                                     \
| nmrPipe  -fn SP -off 0.4 -end 0.98 -pow 1 -c 0.5    \
| nmrPipe  -fn ZF -size 2048                               \
| nmrPipe  -fn FT                 \
| nmrPipe  -fn PS -p0 -90. -p1 0.0                 \
| nmrPipe  -fn PS -p0 -4.8 -p1 12.0  -di                \
#| nmrPipe  -fn PS -p0 0. -p1 0.0 -di                 \
| nmrPipe  -fn POLY -auto -ord 0                      \
#| nmrPipe -fn EXT -x1 132ppm -xn 104ppm -sw \
| nmrPipe  -fn TP                                     \
| nmrPipe  -fn POLY -auto -ord 2                      \
   -verb -ov -out trosy-fb.ft2

exit 0

      Delay: 0   point    P1 =   0   FID: Scale -c 0.5

      Delay: 1/2 point    P1 = 180   FID: Scale -c 1.0
                                     Spectrum: Folded peaks have opposite sign

      Delay: 1   point    P1 = 360   FID: Scale -c 1.0
                                    Spectrum: Use "POLY -auto -ord 0"



