**Task:** Assign the appropriate `c_kinrel` value to each kinship relationship from the input file.

**Reference Data:**
- **kinship_codes_utf8.json:** Contains mappings where c_kinrel_chn provides the Chinese description of kinship relationships.
- **KINSHIP CODE RULES:** Defines additional guidelines for assigning `c_kinrel` values.

**Instructions:**
1. Use `kinship_codes_utf8.json` to find the most accurate `c_kinrel` for each kinship relationship in the input file.
2. If an exact match is unavailable, derive a suitable `c_kinrel` based on patterns and logic from **KINSHIP CODE RULES** and existing cases in **KINSHIP CODES JSON**.
3. Output a table with two columns:
   - **Column 1:** Kinship relationship from the input file.
   - **Column 2:** Assigned `c_kinrel`.

**KINSHIP CODE RULES:**

The building-block relations for Kinship are the 10 basic categories:  

	e 	Ego (the person whose kinship is being explored)
	F 	Father
	M	Mother
	B	Brother
	Z	Sister
	S	Son
	D	Daughter
	H	Husband
	W	Wife
	C	Concubine

There are also variations on the nature of the relationship, as well as additional types of notation to represent types of kinship relations beyond the nuclear family:

+	Older  (e.g. older brother B+, 兄)
-	Younger (e.g. younger sister Z­， 妹)
*	Adopted heir (as in S*, adopted son)
°	Adopted
!	Bastard
^	Step- (as in S^ step-son)
½	half- (as in Z½ , half-sister)
~	Nominal (as in M~ , legitimate wife as nominal mother to children of concubine)
%	Promised husband or wife (marriage not completed at time of record)
y	Youngest (e.g., Sy is the youngest known son)
1, 2, 3…	Numbers distinguish sequence (e.g., S1, S2 for first and second sons; W1, W2 for the first and the successor wives)
n	precise generation unknown
G-#, G+#	lineal ancestor (–) or descendant (+) of #th generation
G-n, G+n, Gn	lineal kin of an unknown earlier generation (G-n), or unknown later generation (G+n), or unknown generation (Gn)
G-#B, BG+#	a brother of a lineal ancestor of # generation; a brother’s lineal descendant of # generation
K, K-#, K+#, Kn	Lineage kin, of the same, earlier (–), later (+) or unknown (n) generation. CBDB uses “lineage kin” for cases where kinship is attested but the exact relationship is not known. Lineage kin are presumably not lineal (direct descent) kin. 
K–, K+	Lineage kin of the same generation, younger (-) or elder (+). 
P, P-#, P+#, Pn	Kin related via father’s sisters or mother’s siblings, of the same, earlier (–), later (+) or unknown (n) generation.  Signified by the term biao (表) in Chinese. (CBDB uses these codes only when the exact relationship is not known).
P–, P+	Kin related via father's sisters or mother's siblings, of the same generation, younger (-) or elder (+).
A	Affine/Affinal kin, kin by marriage

The codes for the types of relationships are in the table KINSHIP_CODES.  Although CBDB records all the many variations of kinship, searches for kinship networks in CBDB use an important set of four metrics for kinship distance to simplify the vast proliferation of terms.  Each code KINSHIP_CODES table has values for 

up, i.e., ancestor generation: father = 1, grandfather = 2, and so on 
down, i.e., descendent generation: son = 1, grandson = 2, etc. 
collateral relation: brother = 1, brother’s wife’s sister” =2.... 
marriage relation: wife = 1, wife’s father’s wife = 2, and so on.  