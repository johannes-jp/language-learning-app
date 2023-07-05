# language-learning-app

**Spaced repetition and linguistic databases integrated with chat gpt for language learning**


# Concepts

Language is deceptively nondeterministic, because we don't define it before we communicate with it. You use a word when you have a sense of how to use it; linguists even use the term 'sense' to denote an attributed meaning. There are so many senses and so many contexts that comprehensive lexicons put a lot of effort into the philosophy of how to define, connect, and curate meaningful relationships.

It's an interesting data problem - WordNet's model is to deeply focus on interlinking the English lexicon through synsets (sets of cognitive synonyms - stuff that aught to be related), while the semantic web model (used by Wikidata and BabelNet, see [schema.org](schema.org)) is a bit more taxonomic, defining entities with a depth of abstract properties that inherently transcends language barriers. That's an infinite data task with a learning curve, but user contributions are persistent, and transfer learning from resources like WordNet can bootstrap the process.

It's worth noting that smaller languages face compounding disadvantages in meeting such a data demand, especially as AI becomes exponentially better at augmenting tasks in more popular languages. They need more structured data and more native engagement not only to preserve their own language over time, but to teach it to large language models like chatGPT so it can serve their native speakers.


# Learning

I would guess that a lot of language learners don't care about most of this, but maybe they should. Some teachers are adamant about prioritizing sentence learning over vocabulary so these synsets are learned implicitly. With partial understanding, the student comes up with their own theories for a thing's meaning and usage, and they find out if they're right or wrong with new input. They learn what a thing *is* and *isn't*, which is great for retention, but more importantly they get to find it out for themselves, which is self-motivating.

A learning system that encourages this fuzzy process is important, but the student still needs the tools to seamlessly track progress and get answers with some granularity. Doing that *without* disrupting the fuzzy learning is a tricky user experience problem, both programatically and psychologically, but I'm at least confident in saying that those same tools can accommodate vocab and make sentence learning accessible for brand-new students too.

If synset analytics can be the basis for an effective learning system, and if there's compelling evidence of its benefits, teachers have an incentive to integrate synsets into their own lesson plans. In an open data ecosystem, this will progressively improve WordNets in more languages, providing more powerful tools for teachers. 


# The App

This system should embody the open data philosophy and enable contributions to public lexicons, but its focus is on the user who is here for personal enrichment, hopefully with some social features at their disposal. Self-interest will drive more engagement, leading to more data volume that tangentially enriches preservation efforts and AI training at a larger scale. 

Functionally, since we care about a language item's relationships and not its definitions, a graph db will store these connections and serve visual, learning-focused queries when an item is clicked/tapped. This granularity might serve incomplete, excessive, or useless content, so **relevance** is critical to scoping content branches (no one says "wherefore", don't display it), and letting users define **synsets** ensures the gaps can be filled through combined effort. 

On that note, the system will attempt to estimate relevance and capture synsets itself from external data, but this will always be insufficient. User-generated lists and lesson plans that can define their own priority and include additional context are core functions, which, along with user study habits, will help the system establish more characteristic and relevant data. Tools that query and display lexicographical data should be very configurable, sometimes to expose important information and sometimes to hide it, allowing the student to infer and explore. 

In a mature app with more users, teachers and experts could charge for access to their lesson plans, which could also facilitate grant money going to creators of important content that otherwise wouldn't have enough students to financially support their efforts.

But at the end of the day, a big group of engaged users can do amazing things, and they might be a crucial part of generating content and linking concepts within and across languages, spoken and signed, to help protect those under threat of extinction. Couldn't such content come from Facebook, Reddit, etc.? It already does to an extent, but it's raw data that takes expertise to access and process. Instead, it may be possible to create a community that structures its data just enough to make it immediately valuable for language processing, bridging the gap between natural engagement and academic rigor.

What about chatGPT? I'll integrate that pretty early on for conversations, and I plan to pass graph db queries to it which will open up immense possibilities. I'd rather ideate and experiment then; to focus on them right now would ignore the reality that there are too many people in other languages who it can't help yet, hence an early focus on more explicit tools. 


# The Real App

These are the goals. This space will start with what I'm learning, Finnish and Icelandic, and be geared around words & sentences where I can refine the "content branch" process. But over time, I would like to establish an incentive system that motivates a community to learn, engage, link, and preserve. Time to build.
