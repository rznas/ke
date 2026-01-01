# A Plague Tale: Innocence — Competitive Analysis for Shahnameh Development

**A 40-person French studio achieved AAA-quality narrative adventure with a medieval sibling story, selling over 1 million copies. Here's what a 2-person team can learn from their decisions, shortcuts, and innovations.**

A Plague Tale: Innocence represents the gold standard for what a small-to-mid-sized team can accomplish with focused scope and strong narrative vision. Asobo Studio's debut original IP earned a **93% positive Steam rating** and **81-83 Metacritic score** despite acknowledged gameplay limitations—proving that emotional storytelling can compensate for mechanical simplicity. For Shahnameh's development, this offers both inspiration and practical boundaries: their character-first philosophy is adoptable, while their 5,000-rat technical showcase required proprietary engine modifications beyond indie reach.

---

## Development facts reveal efficient scope management

Asobo Studio completed A Plague Tale: Innocence with approximately **40 developers over 2+ years** (announced January 2017, released May 14, 2019). The team included only **15-20 artists** and **3 audio staff**. No official budget was disclosed, though the game is consistently described as a "modest AA production."

| Metric | Data |
|--------|------|
| Team size | ~40 people |
| Development time | 2+ years |
| Character artists | 2 |
| Audio team | 3 |
| Game length | 10-15 hours |
| Chapters | 17 |
| Engine | Proprietary (Zouna/ACE) |
| Publisher | Focus Home Interactive |

**Sales performance** exceeded expectations: over **1 million copies** by July 2020, with Steam revenue estimates reaching $128 million. The game launched at $45 across PC, PS4, and Xbox One simultaneously, later expanding to PS5, Xbox Series X|S, and Nintendo Switch (cloud version) in July 2021.

**Award recognition** included the 2019 Steam Award for Outstanding Story-Rich Game, BAFTA nomination for Technical Achievement, The Game Awards nomination for Best Narrative, and six Pégases Awards (French Academy) including Best French Video Game.

---

## Player reception validates narrative-over-mechanics strategy

Steam reviews paint a clear picture: **93% positive from 56,000+ reviews**, with story and atmosphere praised universally while gameplay mechanics received mixed-to-negative feedback. This pattern offers critical strategic insight for Shahnameh.

### What players consistently praised

**Character relationships dominated positive feedback.** Players described watching Amicia and Hugo's bond develop as "genuinely moving," with many reporting they "felt something close to a sibling bond" and grew nervous sending Hugo through crawlspaces. Charlotte McBurney's portrayal of Amicia earned comparisons to Ellie from The Last of Us.

**Visual quality exceeded expectations.** Reviews repeatedly called the medieval French setting "visually breathtaking" and a "genuine work of art," noting it punched far above AA weight class. The rat swarms were described as both "jaw-dropping spectacle" and "appropriately creepy."

**The unique historical setting resonated strongly.** Players praised Asobo for "daring to be different" with a bleak European backdrop seldom explored in games, with battlefield sequences featuring rat swarms bursting from corpses "etching themselves into memory."

### What players consistently criticized

**Limited replayability was the primary complaint.** Linear story with one ending, no side quests, no branching paths—players acknowledged this weakness but forgave it due to narrative quality. Many recommended waiting for sales due to the 10-15 hour length.

**Puzzles drew criticism for being too simple.** Reviews noted solutions were "rarely requiring more than a passing glance to understand," with companions spoiling answers within a minute if players hesitated.

**Late-game difficulty spikes frustrated players.** The cart sequence and final boss were universally criticized as "some of the worst gameplay" and "truly garbage," with complaints about jarring departure from the otherwise gentle difficulty curve. One player noted: "Those final chapters thoroughly soured my experience."

**Stealth mechanics were described as "clunky" and "boring."** Enemy AI earned particular criticism for "worst peripheral vision ever seen in the middle ages" and forgetting disturbances "mere seconds" after investigating.

### Key insight for Shahnameh

Reddit discussions consistently describe A Plague Tale as a "home-cooked meal in a sea of processed food"—players valued the focused, polished 12-hour experience over bloated open-world alternatives. The **93% positive rating despite frequent mechanical criticism** proves that emotional narrative investment trumps gameplay perfection in this genre.

---

## Gameplay mechanics prioritized atmosphere over depth

### Stealth design kept simple intentionally

Amicia is vulnerable by design—15 years old, unable to wield swords, dying in one hit. Stealth mechanics include crouch movement, tall grass/cover hiding, distraction throws, and six unlockable ammunition types (rocks, Ignifer fire, Somnum sleep, Devorantis helmet-corrosion, Luminosa rat-flash, Extinguis torch-extinguisher).

**What worked:** Generous detection systems allowed recovery from mistakes. Hugo's panic mechanic (alerting guards if Amicia ventures too far) added emotional tension without frustration. The dual-threat system—balancing rat avoidance against soldier avoidance—created unique environmental puzzles.

**What didn't work:** Enemy patrol patterns were predictable and exploitable. Investigation behavior was inconsistent—guards returned to routes "mere seconds" after disturbances. Late-game forced combat sections felt weaker than stealth-focused chapters.

### Companion AI succeeded through simplicity

Hugo's implementation proves that effective companion AI requires minimal complexity. He follows automatically, mirrors Amicia's crouch state, waits when commanded, and interacts with objects (crawling through small holes, pulling levers). Critically, **Hugo never breaks stealth or wanders into danger on his own.**

Players compared Hugo favorably to Elizabeth from BioShock Infinite—supportive rather than burdensome. The physical hand-holding mechanic created protective feelings, and his panic mechanic made players feel responsible without constant babysitting.

**Feasibility for 2-person team:** Hugo's command system is achievable. Original designs included complex orders ("Do this, go here, grab that") but Asobo cut these because they felt unorganic. The simplified follow/stay/interact system proved more emotionally resonant and far easier to implement.

### Rat mechanics defined the experience

The signature 5,000-rat swarms used a **four-layer LOD system**: fully animated rats near the player, progressively simplified models at distance, with farthest rats rendered as static meshes. The secret was **flow field pathfinding**—an algorithm from 1991's Micro Machines where each rat makes one key decision (direction) based on environment, seeking humans while avoiding light.

Gameplay interactions included manipulating braziers, carrying torches through swarm-filled areas, extinguishing enemy torches to feed soldiers to rats, and using Odoris ammunition to lure swarms to specific locations.

**For Shahnameh:** The rat system required proprietary engine modifications and significant technical investment. However, the **light/dark binary mechanic** (safe in light, death in darkness) is universally readable and implementable at smaller scale—consider Persian mythology equivalents (shadow djinn, cave-dwelling divs).

---

## Narrative approach prioritized character consistency

### Story structure across 17 linear chapters

Development began with character relationships before any other element—including the rats. Narrative Director Sebastien Renard stated: "Work on your characters. It really starts with the characters, and then it's a matter of respecting them enough to never break their character."

**Critical example:** Early drafts had Hugo speaking about meta-story elements ("Why am I here?"). This was cut because "that's not a five-year-old boy. A five-year-old would talk about what he's seeing—frogs, birds." The team replaced this with Hugo running around playing with frogs, showing age-appropriate behavior.

The flower collectible system exemplified this philosophy. Initially dismissed as "too cheesy," the team reconsidered: "When you go in the forest with a child, they often collect flowers and give it back to you." Hugo placing flowers in Amicia's hair—which she wears throughout the game—became one of the most emotionally resonant mechanics.

### Pacing decisions cut gameplay for narrative flow

Game Director Kevin Choteau revealed that gameplay difficulty was **actively reduced** during development because challenging puzzles "destroyed the pacing and the whole thing of this road trip." Each chapter pushes plot forward—no side quests, no frivolous missions, just story.

**Key quote:** "It's better to convey emotion when you're playing it than when you cannot control it fully." The team added more interactive story moments after finding that "everything was going through cinematics. It's not as good as doing true-to-gameplay."

### Historical setting required local research

Art Director Olivier Ponsonnet drew inspiration from **local medieval vestiges in southwest France**, including the Great Bell of Bordeaux. The team visited actual French medieval villages to study layouts. Being based in Bordeaux provided direct access to reference architecture—a resource advantage they leveraged extensively.

Visual inspiration came from Polish painter **Zdzisław Beksiński** for the "felted, foggy, deeply dark" aesthetic, and the 2015 film MacBeth for mist techniques that compose scenes like illustrations while personifying the plague "as if the air was dense, impure, and corrupted by disease."

**For Shahnameh:** Persian architecture, miniature painting traditions, and regional landscapes offer equivalent local research opportunities. The lesson is leveraging authentic cultural reference rather than generic fantasy aesthetics.

---

## Technical decisions maximized limited resources

### Custom engine enabled unique features

Asobo's proprietary Zouna engine (also called ACE) originated from Kalisto Entertainment in the 1990s. The key advantage: **direct communication with technical director** without external dependencies.

Creative Director David Dedeine explained: "We can directly talk with the technical director to request things. For example, the rats. Without the opportunity to modify the engine directly, dedicated to this game, we wouldn't have moved forward as fast."

**For Shahnameh:** While custom engine development is impractical for a 2-person team, the lesson is **deep mastery of your chosen engine** (Unity/Godot) rather than fighting generic solutions. Consider whether AI-assisted development might substitute for some proprietary advantages.

### Visual quality came from strategic focus

The team achieved AAA-quality visuals through:

- **Photogrammetry and Megascans** for environmental textures
- **Aggressive LOD systems** (especially for rats)
- **Mist/fog** to hide distant detail reduction and mask LOD transitions
- **Linear camera angles** allowing controlled scene composition
- **Color coding**: warm colors (yellow torches) for safety, cool colors (blue moonlight) for atmosphere
- **Focus on cutscene quality**—where players look most critically

**Only 2 character artists** created the entire cast using Substance 3D Painter, demonstrating that focused investment in key areas matters more than broad coverage.

### Audio team of 3 achieved memorable soundscape

Composer Olivier Derivière used **medieval instruments** (lute, hurdy-gurdy, viola da gamba, nyckelharpa) with minimalistic scoring. The key philosophy from Audio Director Aurélien Piters: "The more I work in sound design the more I realize that less is more. Most of the time, I find myself lowering this fader and that fader."

Strategic silence made musical moments more impactful—for much of gameplay, no music plays. Audio cues guide player understanding without being explicit.

**For Shahnameh:** This approach is highly adoptable. Persian traditional instruments (tar, setar, kamancheh, tombak) offer equivalent period authenticity. Restraint in scoring—using music only at key emotional moments—is achievable regardless of team size.

---

## Development process survived a critical crisis

### The "mock review" disaster reshaped the game

Two years into development, external evaluators predicted **55-60% review scores**. Game Director Kevin Choteau described the moment: "The game was a mess. It was awful in terms of gameplay, of story, of everything—nothing was holding together, nothing was quite right. It was a huge punch in our face."

This triggered a drastic response: **replaying the entire game and redoing most work**—rewriting dialogue, plot developments, and reworking gameplay. Publisher Focus granted an **additional 9 months** after this crisis.

**Lesson for Shahnameh:** External validation earlier prevents catastrophic late-stage rewrites. Even informal playtesting with honest feedback is essential—don't wait until near completion to discover fundamental problems.

### Smart cuts preserved scope

The team built "reserved moments" into the story that could be removed without destroying the whole. **A full chapter was cut** from the final game. Hugo's originally complex command system was simplified when organic implementation proved impossible.

Choteau's advice: "You need to be prepared for the worst. At some point when we were writing the story we reserved moments that we knew could be removed."

### Tool iteration required painful pauses

During vertical slice development, the team realized their terrain tool couldn't create organic medieval ground (not paved streets). They made the decision to **pause and rebuild the tool entirely**. "When we came back, it was just perfect because the tool we have is prevalent and has saved a lot of time."

**For Shahnameh:** Early tool/pipeline investment pays dividends—don't fight inadequate workflows through brute force.

---

## GDC talks and videos provide direct developer insights

### Highest-value developer resources

| Resource | Speaker | Key Value |
|----------|---------|-----------|
| "A Plague Tale Audio Design: Not Only Squeaks" (GDC 2020) | Aurélien Piters | Sound design on small budget, "less is more" philosophy |
| "The Level Design Evolution of A Plague Tale" (GDC) | Laura Mas Maury | Breaking linearity in narrative games, player agency in constrained story |
| "How To Make AAA-Looking Games with 20 Artists" (GDC 2023) | Greg Binetruy | Art pipeline efficiency, organic prop/level creation |
| Joseph Anderson's Critique (YouTube, 43 min) | Independent | Critical gameplay analysis, where scripting breaks immersion |
| Digital Foundry Tech Analysis | DF Team | Custom engine achievements, LOD optimization strategies |

The GDC audio talk is **essential viewing**—Piters directly addresses achieving AAA-quality sound with limited resources and small team constraints.

---

## Actionable lessons for a 2-person team

### What Shahnameh can realistically adopt

**Character-first development philosophy.** Start with Shahnameh characters' fears, desires, and obstacles. Let story emerge from character consistency rather than plot requirements. This requires writing discipline, not team size.

**Linear narrative focus.** A Plague Tale proved focused 10-15 hour experiences can achieve critical and commercial success. For episodic Shahnameh, 2-3 hour episodes with tight pacing are more achievable than sprawling open content.

**Simple companion mechanics.** If Shahnameh includes companions, implement follow/stay/interact commands only. Avoid complex order systems—Asobo tried and cut them. The emotional bond comes from narrative context, not mechanical depth.

**Light/dark binary mechanics.** The rat system's core concept—safe in light, death in darkness—is universally readable. Persian mythology offers equivalents: shadow creatures, fire-fearing divs, cave-dwelling demons. Implement the principle without the 5,000-entity rendering.

**One signature mechanic executed well.** Rats defined A Plague Tale despite simple stealth/puzzles. Identify Shahnameh's equivalent—perhaps divs, perhaps a mythological creature system—and invest development time there rather than spreading thin.

**Environmental storytelling through cultural authenticity.** Asobo's Bordeaux location provided medieval architecture reference. Persian miniatures, architectural traditions, and regional landscapes offer Shahnameh equivalent authenticity without requiring expensive research trips.

**Restraint in audio design.** Strategic silence makes music impactful. Persian instruments during key emotional moments, environmental ambience otherwise. A 3-person team achieved A Plague Tale's memorable soundtrack.

### What requires larger resources and should be avoided

**Proprietary engine modifications.** The rat rendering system required direct technical director access and custom solutions. Work within your chosen engine's strengths rather than fighting fundamental limitations.

**Full voice acting for children.** Charlotte McBurney and Logan Hannan delivered praised performances, but child actors require specific casting, direction, and legal considerations. Consider alternative approaches—silent protagonists, adult narrators, limited voiced moments.

**Multiple companion types with unique abilities.** A Plague Tale added companions (Rodric, Melie, Lucas) who each required unique AI behaviors. For a 2-person team, focus on one well-executed relationship rather than ensemble cast.

**Photogrammetry-quality environmental textures.** Asobo used Megascans/Quixel extensively. For Shahnameh, AI-generated textures and stylized art direction may achieve distinctiveness more efficiently than photorealism.

**5,000-entity rendering systems.** The rat LOD optimization required significant engineering. Consider stylized representation of swarms rather than individual entity rendering.

---

## Relevance to Shahnameh: Legends of Persia

### Historical/cultural setting approach

Asobo's treatment of medieval France—researching local architecture, incorporating historical anecdotes, balancing accuracy with creative liberty—directly applies to Persian mythology adaptation. The Shahnameh epic offers rich narrative material: the tragedy of Rostam and Sohrab, the demon-fighting heroes, the political intrigue of ancient courts.

**Key parallel:** A Plague Tale gradually introduced supernatural elements while starting "as grounded as possible." Shahnameh could similarly ground players in historical Persia before revealing mythological creatures, letting the divs and simorgh feel earned rather than arbitrary.

### Episodic structure opportunity

Though A Plague Tale wasn't episodic, its **17 discrete chapters of 15-60 minutes** suggest natural episode boundaries. Shahnameh's legendary tales are inherently episodic—Seven Labors of Rostam, the story of Zal and Rudabeh, the tragedy of Siavash—each could function as standalone episodes while building larger narrative.

### Development efficiency lessons

A 2-person team with AI-assisted development cannot replicate a 40-person studio's output—but can replicate their **philosophy**:

- Story-first design where everything serves narrative
- Linear progression reducing content creation burden
- One signature mechanic (not multiple half-executed systems)
- Strategic scope cuts planned from the beginning
- External validation earlier rather than later
- Tool/pipeline investment before production

A Plague Tale's **1+ million sales** and **93% positive reception** came from emotional resonance, not mechanical innovation. Shahnameh can achieve equivalent impact through Persian mythology's inherent dramatic power—the parent-child tragedies, the heroic sacrifices, the moral complexity—executed with narrative discipline rather than technical scale.

---

## Conclusion: What matters most

A Plague Tale: Innocence succeeded because players **felt something**—nervousness sending Hugo through dangers, satisfaction protecting the siblings, grief at the game's darker moments. Every praised element traces back to emotional investment; every criticism involves mechanics players tolerated because they cared about the characters.

For Shahnameh, the actionable insight is clear: **invest development time in making players care about your characters and world**. Persian mythology offers narrative material as compelling as medieval France's plague—legends of tragic heroes, cosmic struggles between good and evil, family bonds tested by fate. 

A 2-person team cannot build 5,000 rats. But they can build one relationship worth protecting, one world worth exploring, one story worth telling. That's what sold a million copies of A Plague Tale—and it requires writing discipline and creative vision, not a 40-person team.