# Sample Corpus

These files are short synthetic texts written for the demo. They are not the historical corpus used in the paper.

The narrative, philosophical, and civic files are intentionally parallel. Each contains short passages corresponding to the anchor themes in `data/anchors/berlin_liberty_anchor_pairs.csv`: bondage, coercion, authority, departure, trial, law, covenant, moral order, false collective will, agency, future promise, and collective self-rule. Each theme appears in more than one passage so the demo plots contain enough points to form visible clouds.

The red-herring file is intentionally unrelated to the Exodus/liberty anchor themes, but it is written in a more stylized civic/narrative register than a neutral technical log. This makes it a stronger control case: the unguided embedding baseline may respond to shared rhetorical texture, while the anchor-guided projection should remain focused on the curated metaphor themes.

The purpose is not to prove clustering quality. In the unguided embedding baseline, points tend to reflect genre and surface wording. In the anchor-guided metaphor projection, related passages may mix across source labels because different genres can occupy similar positions in the curated metaphor space. The red-herring passages are included as a visible sensitivity check, not as a guaranteed out-of-distribution detector.

Use them to verify that the code runs. For research analysis, supply your own local `.txt` files through a corpus manifest.
