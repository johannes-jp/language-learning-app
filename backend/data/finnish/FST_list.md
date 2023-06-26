# gpt 4 translated
! Parts of speech
[Ln]  ! noun
[Lee] ! proper noun - first name
[Les] ! proper noun - surname
[Lep] ! proper noun - place name
[Lem] ! proper noun - other proper noun
[Ll]  ! adjective
[Lnl] ! name_adjective
[Lt]  ! verb
[Lh]  ! interjection
[Lp]  ! prefix
[La]  ! abbreviation
[Ls]  ! participle
[Lc]  ! conjunction
[Lu]  ! numeral
[Lur] ! numeral (Roman)
[Lr]  ! positional word
[Ld]  ! relational word
[Lk]  ! negation word

! Vowel harmony
[Va]
[Vä]
[Vaä]

! String parameters
[Xp]  ! basic form
[Xj]  ! basic form of derivative
[Xr]  ! structure
[Xs]  ! sourceid
[X]   ! end character of parameter

! Cases
[Sn]   ! nominative
[Sg]   ! genitive
[Sp]   ! partitive
[Ses]  ! essive
[Str]  ! translative
[Sine] ! inessive
[Sela] ! elative
[Sill] ! illative
[Sade] ! adessive
[Sabl] ! ablative
[Sall] ! allative
[Sab]  ! abessive
[Sko]  ! comitative
[Sin]  ! instructive
[Ssti] ! narrative form
[Sak]  ! accusative

! Numbers
[Ny]  ! singular
[Nm]  ! plural

! Possessive suffixes
[O1y] ! 1st person singular
[O2y] ! 2nd person singular
[O1m] ! 1st person plural
[O2m] ! 2nd person plural
[O3]  ! 3rd person singular/plural

! Comparative forms
[Cc] ! comparative
[Cs] ! superlative

! Enclitics
[Fkin] ! -kin
[Fkaan] ! -kaan
[Fko] ! question particle ko/kö

! Moods
[Tn1] ! 1st infinitive
[Tn2] ! 2nd infinitive
[Tn3] ! 3rd infinitive
[Tn4] ! 4th infinitive
[Tn5] ! 5th infinitive
[Tt]  ! indicative
[Te]  ! conditional
[Tk]  ! imperative
[Tm]  ! potential

[Rv]  ! -vA
[Ra]  ! -tAvA
[Ru]  ! -Ut
[Rt]  ! -ttU
[Rm]  ! -mA
[Re]  ! -mAtOn

[P1]  ! 1st person
[P2]  ! 2nd person
[P3]  ! 3rd person
[P4]  ! 4th person

[Ap]  ! present tense
[Ai]  ! past tense

[Et]  ! true
[Ef]  ! false
[Eb]  ! both

[Dg]  ! derived from a proper noun to a common noun
[De]  ! the prefix of the proper noun should be capitalized

! Additional flags
[Ips] ! place name inflects in the inner locative cases
[Ipu] ! place name inflects in the outer locative cases
[Isf] ! loan word quote
[Icu] ! can only continue as a compound word with a hyphen
[Ica] ! allows the absence of a hyphen despite the [Icu] flag at the previous border (but not later)
[Ivj] ! freely combinable compound word suffix
[Ion] ! the name of an organization can be written with a capital letter
[Ira] ! Verb chain: requires an A-infinitive
[Irm] ! Verb chain: requires an MA-infinitive

! Boundary markers
[Bc]  ! boundary produced by guessing between parts of a compound word
[Bh]  ! hyphen with vowel condition
[Bm]  ! known morpheme boundary

! Replaceable characters
[[L]] ! repetition of the previous character
[[IE]] ! preceding i-letter is changed to an e-letter
[[HV]] ! Add h to old inflections, e.g. valo(h)on; a -> aha etc.

! Diacritics
@P.EI_YKS.ON@ @D.EI_YKS@ @C.EI_YKS@ ! Singular forms are not allowed

@P.VAIN_YM3.ON@ @D.VAIN_YM3@ ! Person: only 3rd of singular or plural allowed

@D.YS_ALKANUT@ @R.YS_ALKANUT@ @P.YS_ALKANUT.ON@ ! Compound word has begun
@P.YS_EI_JATKOA.ON@ @D.YS_EI_JATKOA@ @C.YS_EI_JATKOA@ ! Compound word cannot be continued
@P.YS_JATKETTAVA.ON@ @D.YS_JATKETTAVA@ @C.YS_JATKETTAVA@ ! Compound word must be continued
@P.YS_EI_GENETIIVIALKUA.ON@ @D.YS_EI_GENETIIVIALKUA@ ! Genitive form of the first part of a compound word is not allowed

! Continuation (e.g. verb) is only allowed when derived as a noun
@D.JOHDETTAVA_NIMISANAKSI@ @P.JOHDETTAVA_NIMISANAKSI.ON@ @C.JOHDETTAVA_NIMISANAKSI@

! Continuation (e.g. verb) is only allowed when derived as an adjective
@D.JOHDETTAVA_LAATUSANAKSI@ @P.JOHDETTAVA_LAATUSANAKSI.ON@ @C.JOHDETTAVA_LAATUSANAKSI@

! Word (nimi_laatusana) must be interpreted only in its noun sense
@P.VAIN_NIMISANA.ON@ @R.VAIN_NIMISANA@ @D.VAIN_NIMISANA@ @C.VAIN_NIMISANA@

! Derivation of the word as a noun is forbidden
@P.EI_NIMISANAJOHDOSTA.ON@ @D.EI_NIMISANAJOHDOSTA@

# gpt 3.5 translated
! Deriving the word as a name-qualityword is prohibited
@P.EI_NIMI_LAATUSANAJOHDOSTA.ON@ @D.EI_NIMI_LAATUSANAJOHDOSTA@

! The word is a monolithic verb
@P.YKSITEKIJÄINEN.ON@ @D.YKSITEKIJÄINEN@

! inen-derivative is always allowed
@P.INEN_SALLITTU.ON@ @R.INEN_SALLITTU@ @C.INEN_SALLITTU@ @D.INEN_SALLITTU@

! inen-derivative is always prohibited
@P.INEN_KIELLETTY.ON@ @D.INEN_KIELLETTY@ @C.INEN_KIELLETTY@

! not from mAinen-derivative
@P.EI_MAINEN.ON@ @D.EI_MAINEN@

! inen-derivative is required
@P.INEN_VAADITTU.ON@ @D.INEN_VAADITTU@ @C.INEN_VAADITTU@ @R.INEN_VAADITTU@

! Word ending with lAinen (currently only as a noun)
@P.LAINEN.ON@ @R.LAINEN@

! lAinen-derivative is required
@P.LAINEN_VAADITTU.ON@ @D.LAINEN_VAADITTU@ @C.LAINEN_VAADITTU@

! not from lAinen-derivative
@P.EI_LAINEN.ON@ @D.EI_LAINEN@

! Front/back vowel forms allowed
@P.V_SALLITTU.E@ @P.V_SALLITTU.T@ @R.V_SALLITTU.E@ @R.V_SALLITTU.T@ @C.V_SALLITTU@

! Comparative forms are not allowed
@P.EI_VERTM.ON@ @D.EI_VERTM@ @C.EI_VERTM@

! Place name suffix required
@P.PAIKANNIMEN_JL.ON@ @C.PAIKANNIMEN_JL@ @D.PAIKANNIMEN_JL@

! Inflection restriction of numerals
@U.LS.SNNY@ @U.LS.SGNY@ @U.LS.SPNY@ @U.LS.STRNY@ @U.LS.SESNY@ @U.LS.SINENY@ @U.LS.SELANY@ @U.LS.SILLNY@
@U.LS.SADENY@ @U.LS.SABLNY@ @U.LS.SALLNY@ @U.LS.SABNY@
@U.LS.SNNM@ @U.LS.SGNM@ @U.LS.SPNM@ @U.LS.STRNM@ @U.LS.SESNM@ @U.LS.SINENM@ @U.LS.SELANM@ @U.LS.SILLNM@
@U.LS.SADENM@ @U.LS.SABLNM@ @U.LS.SALLNM@ @U.LS.SABNM@ @U.LS.SINNM@ @U.LS.SKONM@ @U.LS.SSTINY@

LEXICON Root
Sanasto	;
-[Bc]@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	Sanasto_ee	;
-[Bc]@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	Sanasto_em	;
-[Bc]@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	Sanasto_ep	;
-[Bc]@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	Sanasto_es	;
-[Bc]@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	Sanasto_a	;
-[Bc]@P.YS_ALKANUT.ON@@P.INEN_SALLITTU.ON@:-@P.YS_ALKANUT.ON@@P.INEN_SALLITTU.ON@	Sanasto_nimisanat	;
-[Bc]@P.YS_ALKANUT.ON@@P.JOHDETTAVA_NIMISANAKSI.ON@@P.INEN_SALLITTU.ON@:-@P.YS_ALKANUT.ON@@P.JOHDETTAVA_NIMISANAKSI.ON@@P.INEN_SALLITTU.ON@	Sanasto_t	;
-[Bc]@P.YS_ALKANUT.ON@@P.INEN_SALLITTU.ON@:-@P.YS_ALKANUT.ON@@P.INEN_SALLITTU.ON@	Sanasto_l	;
LukusananAlku	;
-[Bc]@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	LukusananAlku	;
-@P.YS_ALKANUT.ON@:-@P.YS_ALKANUT.ON@	LukusananErikoisjälkiliite	;
Asemosana	;
Suhdesana	;
Kieltosana	;

LEXICON Sanasto
Sanasto_ee	;
Sanasto_em	;
Sanasto_ep	;
Sanasto_es	;
Sanasto_h	;
Sanasto_l	;
Sanasto_n	;
Sanasto_nl	;
Sanasto_t	;
Sanasto_p	;
Sanasto_a	;
Sanasto_s	;
Sanasto_c	;

LEXICON Sanasto_ee
Joukahainen_ee	;
Poikkeavat_ee	;

LEXICON Sanasto_em
Joukahainen_em	;
Poikkeavat_em	;

LEXICON Sanasto_ep
Joukahainen_ep	;
Poikkeavat_ep	;

LEXICON Sanasto_es
Joukahainen_es	;
Poikkeavat_es	;

LEXICON Sanasto_h
Joukahainen_h	;

LEXICON Sanasto_l
Joukahainen_l	;
Poikkeavat_l	;

LEXICON Sanasto_n
Joukahainen_n	;
Poikkeavat_n	;

LEXICON Sanasto_nl
Joukahainen_nl	;
Poikkeavat_nl	;

LEXICON Sanasto_t
Joukahainen_t	;
Poikkeavat_t	;

LEXICON Sanasto_p
Joukahainen_p	;

LEXICON Sanasto_a
Joukahainen_a	;
Poikkeavat_a	;

LEXICON Sanasto_s
Joukahainen_s	;
Poikkeavat_s	;

LEXICON Sanasto_c
Joukahainen_c	;

LEXICON Sanasto_laatusanat
Sanasto_l	;
Sanasto_nl	;

LEXICON Sanasto_nimisanat
Sanasto_n	;
@P.EI_VERTM.ON@@P.VAIN_NIMISANA.ON@:@P.EI_VERTM.ON@@P.VAIN_NIMISANA.ON@	Sanasto_nl	;
@P.JOHDETTAVA_NIMISANAKSI.ON@:@P.JOHDETTAVA_NIMISANAKSI.ON@	Sanasto_p	;

LEXICON Sanasto_nimisanat_ja_nl_vertailumuodot
Sanasto_n	;
Sanasto_nl	;
@P.JOHDETTAVA_NIMISANAKSI.ON@:@P.JOHDETTAVA_NIMISANAKSI.ON@	Sanasto_p	;

LEXICON Sanasto_nimisana_yhdyssanana_perusosana
Sanasto_nimisanat	;
Ys_perusosa_seikkasanasta	;

LEXICON Sanasto_nimisana_yhdyssanana_perusosana_ja_nl_vertailumuodot
Sanasto_nimisanat_ja_nl_vertailumuodot	;
Ys_perusosa_seikkasanasta	;

LEXICON Yleisnimet
Sanasto_l	;
Sanasto_nl	;
Sanasto_n	;

LEXICON Erisnimet
Sanasto_ee	;
Sanasto_em	;
Sanasto_ep	;
Sanasto_es	;