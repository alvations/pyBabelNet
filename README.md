pyBabelNet
==========

for BabelNet v2.5


It looks harder than I thought, so here's some more recon work on BabelNet2.5:
 - BabelNet2.5 Lucene's indice needs to be upgraded before using it with pylucene or newer java lucene versions (see `upbabel.sh`
 - One would need Luke to inspect the indices before knowing what the API is doing, see http://stackoverflow.com/questions/12951549/how-to-run-lukelucene-tool




`upbabel.sh`:

```
for d in /home/alvas/BabelNet-2.5/*; do
	java -cp lucene-core-4.10.2.jar org.apache.lucene.index.IndexUpgrader $d
done
```
