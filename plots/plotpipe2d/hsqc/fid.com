#!/bin/csh

bruk2pipe -in ./ser \
  -bad 0.0 -aswap -DMX -decim 1672 -dspfvs 20 -grpdly 67.9892272949219  \
  -xN              2048  -yN               640  \
  -xT              1024  -yT               320  \
  -xMODE            DQD  -yMODE  Echo-AntiEcho  \
  -xSW        11961.722  -ySW         2941.176  \
  -xOBS         900.274  -yOBS          91.234  \
  -xCAR           4.706  -yCAR         119.039  \
  -xLAB              HN  -yLAB             15N  \
  -ndim               2  -aq2D          States  \
  -out ./test.fid -verb -ov

sleep 5
