# Sample Corpus

These files are short synthetic texts written for the demo. They are not the historical corpus used in the paper.

The three files are intentionally parallel. Each contains short passages corresponding to the anchor themes in `data/anchors/berlin_liberty_anchor_pairs.csv`: bondage, coercion, authority, departure, trial, law, covenant, moral order, false collective will, agency, future promise, and collective self-rule. Each theme appears in more than one passage so the demo plots contain enough points to form visible clouds.

The purpose is not to prove clustering quality. In the unguided embedding baseline, points tend to reflect genre and surface wording. In the anchor-guided metaphor projection, points may mix across source labels because passages from different genres can occupy similar positions in the curated metaphor space.

Use them to verify that the code runs. For research analysis, supply your own local `.txt` files through a corpus manifest.
