# language-learning-app

**Spaced repetition and linguistic databases integrated with chat gpt for language learning**


# Concepts

Language is deceptively nondeterministic, because we don't define it before we communicate with it. You use a word when you have a sense of how to use it; linguists even use the term 'sense' to denote an attributed meaning. There are so many senses and so many contexts that comprehensive lexicons put a lot of effort into the philosophy of how to define, connect, and curate meaningful relationships.

It's an interesting data problem - WordNet's model is to deeply focus on interlinking the English lexicon through synsets (sets of cognitive synonyms - stuff that aught to be related), while models like Wikidata and BabelNet abstract these relationships enough to bridge languages without an intermediary like English. That's an infinite data task, but user contributions and transfer learning from resources like WordNet can bootstrap the process.

It's worth noting that smaller languages face compounding disadvantages in meeting such a data demand, especially as AI becomes exponentially better at augmenting tasks in more popular languages. They need better synsets and more native engagement not only to preserve their own language over time, but to teach it to large language models like chatGPT so it can serve their native speakers.


# Learning

I would guess that a lot of language learners don't care about most of this, but maybe they should. Some teachers are adamant about prioritizing sentence learning over vocabulary so these synsets are learned implicitly. With partial understanding, the student comes up with their own theories for linguistic meaning and usage, which is incredible for retention (even if they're wrong).

This fuzzy process should be rewarded, but the student still needs the means to track, self-correct, and access learning seamlessly and with some granularity. Doing that **without** disrupting the fuzzy learning is a tricky user experience problem, both programatically and psychologically, but I'm at least confident in saying that those same granular tools can accommodate vocab and make sentence learning accessible for brand-new students too.

If there's compelling evidence of the learning benefits of applied synset analytics, teachers have an incentive to develop or refine WordNets in their language too. It's also worth exploring other syntactically rich study items like mnemonics, especially with a community that can experiment, iterate, and make it fun.


# The App

This tool should reflect the open data philosophy and enable contributions to public lexicons, but its focus is on the user who is here for personal enrichment, hopefully with some social features at their disposal. Self-interest will drive more engagement, leading to more data volume and synsets that tangentially enrich preservation efforts and AI training at a larger scale.

Functionally, since we care about a language item's relationships and not its definitions, a graph db will store these connections and serve visual, learning-focused queries when an item is clicked/tapped. This granularity can serve overloading or useless content, so a **relevance** filter is critical to sizing and scoping content branches (no one says "wherefore", don't display it).

On that note, the system will attempt to estimate relevance itself from external data, but this will always be insufficient. User-generated lists that define their own priority are a key part of the user experience, which, along with user study habits, will help the system establish more characteristic relevance data. List building tools should be extensible to full lesson plans, and with highly configurable component-level queries, should enable students and teachers to create a tailored learning experience.

In a mature app with more users, experts could charge for their lessons and donate the naturally manifesting synsets to help support WordNet-style development in more languages. This payment system could also facilitate grant money going to creators of important content that otherwise wouldn't have enough students to financially support their efforts.

But at the end of the day, a big group of engaged users can do amazing things, and they might be a crucial part of generating content and linking concepts within and across languages, spoken and signed, to help protect those under threat of extinction. Could such content come from Facebook, Reddit, etc.? Sure, but they don't bake synset functions into their forums, databases, and brand culture to linguistically ground-truth their content, nor would they as an organization have the traction to galvanize a community toward preservation efforts.

What about chatGPT? I'll integrate that pretty early on for conversations, and I plan to pass graph db queries to it which will open up immense possibilities. I'd rather ideate and experiment then; to focus on them right now would detract from the reality that there are too many people in other languages who it can't help yet.


# The Real App

These are the goals. This space will start with what I'm learning, Finnish and Icelandic, and be geared around words & sentences where I can refine the "content branch" process. But over time, I would like to establish an incentive system that motivates a community to learn, engage, link, and preserve. Time to build.
