#! /bin/bash
# works on MacOS - not sure if entr is available on other OSes
ls sphinx/index-template.md \
   sphinx/custom.css \
   sphinx/conf.py \
   subjects/*/*.md | entr -pr make index html
