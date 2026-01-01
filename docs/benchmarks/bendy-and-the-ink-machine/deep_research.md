# Bendy and the Ink Machine: Competitive Analysis for Shahnameh Development

A **5-day side project by 2 people** became one of the most successful indie horror franchises of the 2010s, selling **over 2 million copies** with estimated gross revenue of **$7.9 million**. However, the developers explicitly stated they will **never use episodic release again**—offering critical lessons for your Shahnameh project.

## The 5-day prototype that launched a franchise

Bendy and the Ink Machine began when artist theMeatly (Paul Crawford) wondered "what would it look like to walk in a 3D world made of sketches?" While building the environment, he realized it felt creepy and needed a monster. The character name "Bendy" came from a typo—saving the file as "bendy.blend" in Blender. Programmer Mike Desjardins (Mike Mood) joined after seeing the concept, cleaned up theMeatly's non-functional code, and they released Chapter 1 for free on Game Jolt on February 10, 2017.

Within days, the game went viral. YouTubers like Markiplier and Jacksepticeye featured it, DAGames' fan song "Build Our Machine" accumulated **200+ million views**, and Steam Greenlight approved the game in just 4 days. By end of 2017, downloads reached **750,000**. The team grew from 2 to 6 people for Chapter 3, then to **25+ full-time employees** by 2019 after acquiring their former employer, Karman Interactive.

| Metric | Result |
|--------|--------|
| Steam rating | 88% positive (30,500+ reviews) |
| Metacritic | 63-70 (mixed-average) |
| Reddit community | 48,300+ members |
| Total playtime | ~4-7 hours |
| Dev timeline | 20 months (5 chapters) |
| Estimated revenue | $7.9M gross / $2.3M net |

## Episode release timeline reveals critical pacing

The gap between chapters stretched progressively longer as scope expanded:

| Chapter | Release Date | Gap | Dev Time | Team |
|---------|--------------|-----|----------|------|
| Ch. 1: Moving Pictures | Feb 10, 2017 | — | 5 days | 2 people |
| Ch. 2: The Old Song | Apr 18, 2017 | 67 days | 6 weeks | 2-4 people |
| Ch. 3: Rise and Fall | Sep 28, 2017 | 163 days | 4 months | 6 people |
| Ch. 4: Colossal Wonders | Apr 30, 2018 | 214 days | 7 months | 15+ people |
| Ch. 5: The Last Reel | Oct 26, 2018 | 179 days | 6 months | 15+ contractors |

Mike Mood described Chapter 3 development as **"TORTURE"** because he had to create a development framework mid-production—something that didn't exist for Chapters 1-2. The game never had a complete design document; only Chapters 4-5 received formal gameplay write-ups.

## Pricing model rewarded early adopters brilliantly

The financial structure created sustainable revenue while building loyalty:

- **Chapter 1**: Free (acted as demo/hook)
- **Chapters 2-4**: $5.99 each 
- **Chapter 5**: Free for existing owners
- **Complete Edition**: $19.99

Mike Mood's philosophy: **"I don't believe in selling something that doesn't exist yet"**—explaining why they avoided season passes. This built trust but meant each chapter had to succeed independently. His wife Jillian suggested the pivotal reframe: calling the demo a "chapter" instead, which enabled the episodic model.

Each chapter averaged **10-90 minutes** of content, with Chapter 1 at 10-30 minutes (introductory) and Chapters 3-4 at 60-90 minutes. Total completion without collectibles runs approximately 4 hours.

## What kept players engaged between 7-month gaps

The team deployed multiple retention strategies that your 2-person team could replicate:

**Fan art contests before each chapter** with winners featured in-game—by Chapter 2's release, fan art was abundant online. **Letter-by-letter Twitter reveals** created daily engagement: before Chapter 4, letters spelled "JOURNEY DEEPER & FEAR THE RIDE." **Animated shorts** like "Tombstone Picnic" and "Haunted Hijinx" maintained presence between releases.

Most critically, **each chapter release included free remasters of all previous chapters**. The Chapter 4 release overhauled Chapters 1-3 with improved lighting, new rooms, streamlined fetch quests, and enhanced audio. This rewarded existing players while improving the experience for new ones.

The Halloween 2017 **Hello Neighbor crossover** replaced the Ink Demon with Hello Neighbor's antagonist for one week—creating urgency and renewed interest without new content.

## Community feedback visibly shaped development

Documented changes based on player input include:

- **Bendy's model evolution**: From "bird poop" torso-only to the final inky skeletal figure with animated drip effects
- **Chapter 3 fetch quest reduction**: Extensively criticized, then streamlined for subsequent chapters
- **Save point systems added**: TimeKeeper save points introduced after players reported lost progress
- **Chapter 4 puzzle focus**: Added problem-solving and boss fights, removing unpopular maze exploration

The Reddit community's **100+ threads complaining about the ending** forced moderators to address it—the time loop conclusion proved divisive, with comparisons to "Last Jedi discourse."

## What players loved reveals your success formula

Steam's 88% positive rating came from:

1. **Unique visual aesthetic**: The 1930s rubber hose cartoon style—inspired by Fleischer Studios' Betty Boop and early Disney—was universally praised as "beautiful" and "stunning"
2. **Atmospheric horror over jump scares**: Sepia tones, abandoned studio setting, "ocean of endless ink" created effective dread
3. **Compelling lore via audio logs**: BioShock-style environmental storytelling captivated players
4. **Accessible horror**: Called "entry-level horror that's not too hard or scary"—perfect for younger audiences and casual players
5. **Fan music integration**: Including fan songs in credits created passionate community ownership

## Player criticisms identify pitfalls to avoid

Consistent negative themes across reviews:

- **Fetch quest gameplay** particularly in Chapters 1 and 3—"forcing the player to collect items in a maze of corridors is frustrating"
- **Clunky combat**: Hit detection "unpredictable in a mechanical sense"
- **Story felt improvised**: Episodic development showed seams; chapters inconsistent in quality
- **Bendy felt "toothless"**: The main villain appeared infrequently and AI would "forget" players in hiding spots
- **Disappointing ending**: Time loop conclusion sparked massive debate
- **Horror veterans found it tame**: Unfavorable comparisons to Amnesia, Outlast, Layers of Fear

The gap between **88% Steam approval** and **63-70 Metacritic** scores reveals a significant player-critic disconnect—the game succeeded through community passion rather than mechanical excellence.

## YouTube was the entire marketing strategy

The game had **zero paid marketing budget**. Success came entirely from organic viral spread:

- **Markiplier's Chapter 1 playthrough**: 3+ million views
- **Jacksepticeye**: 1.9+ million views, then was cast as voice actor for Shawn Flynn in Chapter 3
- **DAGames' "Build Our Machine"**: 200+ million YouTube views
- **1.5+ million fan-made videos** by end of 2017

The developers cast Jacksepticeye specifically for marketing synergy—he received an exclusive "Jacksepticeye Edition" before Chapter 5's public release, guaranteeing coverage to his millions of subscribers.

TV Tropes documented this as a "Colbert Bump": the game skyrocketed when Markiplier's Let's Play and DAGames' music video released within a week of each other.

## Unity and Blender powered the entire production

**Technical stack:**
- **Engine**: Unity3D (Mike's specialty from selling Unity Asset Store textures)
- **3D Modeling**: Blender (character name came from "bendy.blend" typo)
- **Art**: theMeatly handled all art direction; simple rubber hose style reduced modeling complexity
- **Audio**: theMeatly composed the 19-track soundtrack; voice acting through audio logs avoided lip-sync animation costs

The 1930s rubber hose aesthetic was chosen strategically: round shapes, jointless limbs, and simple expressions meant **faster modeling and fewer animations**. The monochromatic sepia palette reduced texture complexity. Characters were highly merchandisable—Bendy's face became instantly recognizable.

**Mike's hiring principle**: "Go out and find people to take care of things you aren't good at and focus on what you're good at. You can't wear all the hats." They hired lawyers and accountants before making profit.

## Developer postmortems warn against episodic repetition

From multiple interviews, the developers stated explicitly:

> "Bendy and the Ink Machine has never had a full game design document or any structure to it, only base narrative and minor gameplay write-ups for each chapter."

> "Our next project will be more structured, and we won't be killing ourselves with timelines; it will be done when it's done."

The sequel, **Bendy and the Dark Revival** (2022), released as a complete game with all chapters included—the developers explicitly announced they would not repeat the episodic format.

**What they'd do differently:**
- Create a proper game design document from start
- Avoid self-imposed deadline crunch
- Hire specialists earlier to free creative time
- Build development framework before production, not during Chapter 3

## Applying these lessons to Shahnameh development

**What's directly transferable to your 2-person team:**

1. **Free first episode as hook**: Your Persian mythology aesthetic is distinctive—a free 30-minute introduction could drive organic discovery
2. **YouTube-optimized design**: Dramatic moments, distinctive visuals, and lore for theory-crafting drove BATIM's viral spread without marketing budget
3. **Simple, stylized art**: The rubber hose aesthetic reduced modeling complexity while creating iconic imagery—Persian miniature painting could serve the same function
4. **Audio log storytelling**: Environmental narrative is cheaper than cutscenes and creates mystery for player theory-crafting
5. **Fan art contests**: Create community ownership; winning art featured in-game builds invested audience
6. **Chapter remasters with each release**: Improves total experience while rewarding early adopters

**Critical differences to plan for:**

1. **Create your design document now**: BATIM's lack of documentation caused "chaotic" development and "torture" during Chapter 3
2. **Build your development framework first**: Don't create tools mid-production like they did
3. **Plan for 5-7 month gaps**: Their 2-month Chapter 2 gap was unsustainable; expect longer development cycles
4. **Chapter 3 is the danger zone**: This is where scope explodes and frameworks break—plan accordingly
5. **Episodic fatigue is real**: Even successful developers won't repeat this model; consider hybrid approaches (2-3 episodes maximum, or complete game with staggered marketing)

**Your advantages over BATIM's starting position:**

- You're starting with a plan (they had none)
- AI-assisted development tools didn't exist in 2017
- Persian mythology is an untapped aesthetic (BATIM succeeded partly from timing—their style felt new)
- You can learn from their documented mistakes

**Realistic expectations:**

BATIM's success was described by Mike Mood as an **"accidental success"** and **"fluke release."** The viral YouTube explosion was not planned or predictable. Your baseline should expect modest success with the possibility of breakthrough—not breakthrough as the expectation. The team's growth from 2 to 25 employees happened over two years of proven demand, not immediately.