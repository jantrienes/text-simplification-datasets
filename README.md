# Text Simplification Datasets

## Datasets

| Author | Name | Lang | Domain | Kind | Level | Instances | Refs. | Link |
|-|-|-|-|-|-|-|-|-|
| [Zhu et al. (2010)](https://aclanthology.org/C10-1152) | PWKP | EN | Wikipedia | Comparable | Sent | 108,016 paired sentences extracted from 65,133 articles. | 1 | [Link](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2447) |
| [Coster and Kauchak (2011)](https://aclanthology.org/P11-2117) | C&K1 | EN | Wikipedia | Comparable | Sent | 137,000 paired sentences from 10,588 articles. | 1 | [Link](https://cs.pomona.edu/~dkauchak/simplification/) |
| [Kauchak (2013)](https://aclanthology.org/P13-1151) | C&K-2 | EN | Wikipedia | Comparable | Sent | 167,000 paired sentences. | 1 | [Link](https://cs.pomona.edu/~dkauchak/simplification/) |
| [Hwang et al. (2015)](https://aclanthology.org/N15-1022/) | EW-SEW | EN | Wikipedia | Comparable | Sent | 150,000 full and 130,000 partial matches | 1 | n/a (Raw dataset no longer available. Pre-processed version available [here](https://github.com/senisioi/NeuralTextSimplification)) |
| [Kajiwara and Komachi (2016)](https://aclanthology.org/C16-1109) | sscorpus | EN | Wikipedia | Comparable | Sent | 492,993 aligned sentences from 126K article pairs. | 1 | [Link](https://github.com/tmu-nlp/sscorpus) |
| [Xu et al. (2016)](https://doi.org/10.1162/tacl_a_00107) | TurkCorpus | EN | Wikipedia | Parallel | Sent | 2350 sentences (2000 dev, 350 test) | 8 | [Link](https://github.com/cocoxu/simplification/) |
| [Zhang and Lapata (2017)](https://doi.org/10.18653/v1/d17-1062) | WikiLarge | EN | Wikipedia | Comparable | Sent | 296,402 sentence pairs (WikiLarge) | 1 | [Link](https://github.com/XingxingZhang/dress) |
| [Zhang and Lapata (2017)](https://doi.org/10.18653/v1/d17-1062) | WikiSmall | EN | Wikipedia | Comparable | Sent | 89,042 sentence pairs | 1 | [Link](https://github.com/XingxingZhang/dress) |
| [Botha et al. (2018)](https://aclanthology.org/D18-1080/) | WikiSplit | EN | Wikipedia | Parallel | Sent | 1 million sentences | 1 | [Link](https://github.com/google-research-datasets/wiki-split) |
| [Sulem et al. (2018)](https://doi.org/10.18653/v1/D18-1081) | Hsplit | EN | Wikipedia | Parallel | Sent | 350 sentences (test set of turk corpus) | 2 | [Link](https://github.com/eliorsulem/HSplit-corpus) |
| [Alva-Manchego et al. (2020)](https://doi.org/10.18653/v1/2020.acl-main.424) | ASSET | EN | Wikipedia | Parallel | Sent | 2350 sentences (2000 train, 350 test) | 10 | [Link](https://github.com/facebookresearch/asset) |
| [Jiang et al. (2020)](https://doi.org/10.18653/v1/2020.acl-main.709) | Wiki-AUTO | EN | Wikipedia | Comparable | Sent | 488,332 train sentences from 138,095 article pairs (2019/09 dump). | 1 | [Link](https://github.com/chaojiang06/wiki-auto) (Part of [GEM](https://gem-benchmark.com/data_cards/Wiki-Auto)) |
| [Aumiller and Gertz (2022)](https://aclanthology.org/2022.lrec-1.288/) | Klexikon | DE | Wikipedia | Comparable | Doc | 2898 article pairs | 1 | [Link](https://github.com/dennlinger/klexikon) |
| [Klerke and Søgaard (2012)](https://aclanthology.org/L12-1113/) | Dsim | DA | News | Parallel | Doc | 3,701 articles with 48,186 aligned sentences | 1 | n/a |
| [Xu et al. (2015)](https://doi.org/10.1162/tacl_a_00139) | Newsela | EN | News | Parallel | Doc | 1130 articles (original); 1911 articles (v2016-01-29); at 5 levels | 1 | [Link](https://newsela.com/data/) |
| [Xu et al. (2015)](https://doi.org/10.1162/tacl_a_00139) | Newsela-ES | ES | News | Parallel | Doc | 243 articles (v2016-01-29) at 5 levels | 1 | [Link](https://newsela.com/data/) |
| [Vajjala and Lucic (2018)](https://doi.org/10.18653/v1/w18-0535) | OneStopEnglish | EN | News | Parallel | Doc | 189 articles at three levels. Automatic sentence alignment: 1.6K ELE-INT, 2.1K ELE-ADV, 3.1K INT-ADV. | 1 | [Link](https://zenodo.org/record/1219041) |
| [Jiang et al. (2020)](https://doi.org/10.18653/v1/2020.acl-main.709) | Newsela-AUTO | EN | News | Parallel | Sent | 666,645 sentence pairs from 1932 articles at 5 levels | 1 | [Link](https://github.com/chaojiang06/wiki-auto) |
| [Rios et al. (2021)](https://doi.org/10.18653/v1/2021.newsum-1.16) | 20 minutes | DE | News | Parallel | Doc | 18,305 articles with simplified summaries. | 1 | [Link](https://github.com/ZurichNLP/20Minuten) |
| [Hauser et al. (2022)](https://aclanthology.org/2022.readi-1.4) | SNIML | DE, EN, FI, FR, IT, SV | News | Simplified only | Doc | 13,447 documents | n/a | [Link](https://pub.cl.uzh.ch/projects/sniml/en/read/) |
| [Klaper et al. (2013)](http://www.aclweb.org/anthology/W13-2902) | SimpleGerman | DE | Web | Comparable | Sent | 7000 sentences from 256 articles. 78% of sentences have an alignment | 1 | n/a (Available on request) |
| [Scarton et al. (2018)](https://aclanthology.org/L18-1685/) | SimPA | EN | Web | Parallel | Sent | 1100 sentences | 3 (lexical); 1 (syntactic) | [Link](https://github.com/SIMPATICOProject/simpa) |
| [Battisti et al. (2020)](https://aclanthology.org/2020.lrec-1.404) | SimpleGerman V2.0 | DE | Web | Comparable | Doc | 5461 simple, unaligned documents and 378 aligned (complex-simple) documents (6217 docs in total). The document-aligned portion has 17,121 complex sentences and 21,072 simple sentences. No statistics on the sentence-alignments are reported. | 1 | n/a ([Scraping code](https://zenodo.org/record/4507047)) |
| [Toborek et al. (2022)](https://arxiv.org/abs/2209.01106) | Simple German V3.0 | DE | Web | Comparable | Doc | 708 documents | 1 | n/a ([Scraping code](https://github.com/buschmo/Simple-German-Corpus)) |
| [Ganitkevitch et al. (2013)](https://aclanthology.org/N13-1092/) | PPDB | EN | Mixed | Comparable | Sent | 221 million sentences | 1 | [Link](http://paraphrase.org) |
| [Pavlick and Callison-Burch (2016)](https://doi.org/10.18653/v1/p16-2024) | Simple-PPDB | EN | Mixed | Comparable | Sent | 4.5 million sentences | 1 | [Link](https://www.seas.upenn.edu/~nlp/resources/simple-ppdb.tgz) |
| [Narayan et al. (2017)](https://doi.org/10.18653/v1/d17-1064) | WebSplit | EN | Mixed | Comparable | Sent | 1 million sentences | 1 | [Link](https://github.com/shashiongithub/Split-and-Rephrase) |
| [Dmitrieva and Tiedemann (2021)](https://aclanthology.org/2021.bsnlp-1.8) | RuAdapt | RU | Books | Parallel | Doc | 457 documents | | [Link](https://github.com/Digital-Pushkin-Lab/RuAdapt) |
| [Taylor et al. (2022)](https://aclanthology.org/2022.coling-1.566/) | PSAT | EN | Education | Parallel | Doc | 112 documents, with total of 1883 aligned sentences | 1 | [Link](https://zenodo.org/record/7065615) |
| [Grabar and Cardon (2019)](https://aclanthology.org/W18-7002/) | CLEAR | FR | Medical | Comparable | Doc | 16190 documents | 1 | [Link](http://natalia.grabar.free.fr/resources.php) |
| [van den Bercken et al. (2019)](https://doi.org/10.1145/3308558.3313630) | myTomorrows-Wiki | EN | Medical | Comparable | Sent | 5415 (manually aligned); 3797 (automatically aligned) | 1 | [Link](https://github.com/myTomorrows-research/public/tree/5b054a88746b7d4422732e2fd3ee6a77a8a53918/WWW2019) |
| [Cao et al. (2020)](https://doi.org/10.18653/v1/2020.acl-main.100) | MSD-Manuals | EN | Medical | Comparable | Sent | 2551 linked paragraphs (professionals <-> laymen) with average of 10.4 and 11.3 sentences each. From a random sample of 1000 paragraphs, medical experts extracted 930 aligned sentences with equivalent meaning. | 1 | [Link](https://srhthu.github.io/expertise-style-transfer/#introduction) |
| [Li et al. (2020)](https://doi.org/10.18653/v1/2020.findings-emnlp.251) | PharmMT | EN | Medical | Parallel | Sent | 380,000K aligned sentences. | 1 | n/a |
| [Van et al. (2020)](https://doi.org/10.18653/v1/2020.coling-main.122) | AutoMeTS | EN | Medical | Comparable | Sent | 3300 aligned sentences | 1 | [Link](https://github.com/vanh17/MedTextSimplifier/tree/master/data_processing/data) |
| [Devaraj et al. (2021)](https://aclanthology.org/2021.naacl-main.395) | Cochrane | EN | Medical | Comparable | Par | 4459 paragraph pairs (<1024 tokens) | 1 | [Link](https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts) |
| [Campillos-Llanos et al. (2022)](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6439) | CLARA-MeD | ES | Medical | Comparable | Doc | | | [Link](https://digital.csic.es/handle/10261/269887) |
| [Goldsack et al. (2022)](https://aclanthology.org/2022.emnlp-main.724/) | BioLaySumm | EN | Medical | Parallel | Doc | 32353 document-plain abstract pairs | 1 | [Link](https://github.com/TGoldsack1/Corpora_for_Lay_Summarisation) |
| [Guo et al. (2022)](https://arxiv.org/abs/2211.03818) | CELLS | EN | Medical | Comparable | Par | 63000 | 1 | [Link](https://github.com/linguisticanomalies/pls_retrieval) |
| [Attal et al. (2023)](https://www.nature.com/articles/s41597-022-01920-3) | PLABA | EN | Medical | Parallel | Doc | 750 documents with 7643 sentence pairs | 1 | [Link](https://osf.io/rnpmf/) |
| [Luo et al. (2022)](https://aclanthology.org/2022.coling-1.313) | MedLane | EN | Clinical | Parallel | Sent | 12,801/1,015/1,016 train/valid/test sentences (avg. 20/24 tokens in source/target) | 1 | [Link](https://github.com/machinelearning4health/MedLane) |
| [Moramarco et al. (2022)](https://arxiv.org/abs/2112.12672) | MTSamples | EN | Clinical | Parallel | Sent | 1250 sentence pairs. | 1 | [Link](https://github.com/babylonhealth/laymaker) |
| [Trienes et al. (2022)](https://aclanthology.org/2022.tsar-1.3/) | SimplePatho | DE | Clinical | Parallel | Doc | 851 documents | 1 | n/a |
| [Chamovitz and Abend (2022)](https://aclanthology.org/2022.conll-1.17/) | FestAbility | EN | Talks | Parallel | Sent | 321 sentence pairs | 1 | [Link](https://github.com/eytan-c/CognitiveSimplification) |

## Contributing

## Acknowledgements
