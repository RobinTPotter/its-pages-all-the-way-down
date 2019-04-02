This is a svg file containing a script to create pages of uno cards

loading in chrome will default to page 0

to preview cards visit file:///d:\xxxx\xxxxxxxx\unfinished-games\svg\uno_cards.svg?page=3

it's not pretty but works. 


workflow was to print from chrome but it pre-renders the pattern and looks terrible (not much better, with print to pdf).

using command line can dump dom to output, (put on a delay with python because I though there
was another problem... left it in here because thought it was quite clever actually)

"C:\Program Files (x86)\Google\Chrome\Application\chrome" --headless --disable-gpu --enable-logging --dump-dom file:///d:\xxx\xxx\unfinished-games\svg\uno_cards.svg?page=1 | python -c "import sys;import time;time.sleep(2);print(sys.stdin.read())" > "d:\xxx\xxx\unfinished-games\svg\test_poo1.svg"

originally was copy the dom from chrome console and pasteing to a file.
used inkscape to dump file to png be like:

```
seq 0 10 | while read o; do echo $i; inkscape -z -f uno$i.svg --export-png=uno$i.png -C --export-dpi=360; done
```

also originally had to adjust svg because inkscape doesn't respect align-baseline. but turns out will do dominant-baseline instead...

altered it now works, also a couple of minor tweaks to remove the main script node on completion. 
inkscape needs to be better then .91 because of dominant-baseline thing wasn't in 91 either..

in the upside tried out snaps in ubuntu ..