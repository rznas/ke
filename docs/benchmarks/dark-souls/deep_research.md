# Dark Souls Competitive Benchmark: A Blueprint for Shahnameh

**A 2-person indie team can absolutely create a souls-like game**, but the path requires strategic constraints, not scaled-down imitation. Dark Souls (2011) achieved legendary status with ~195 credited contributors over 2.5 years, yet its core design philosophy—deliberate combat, environmental storytelling, and interconnected worlds—has been successfully replicated by teams as small as two people. Salt and Sanctuary, created entirely by a husband-and-wife duo, proves the formula scales down effectively. For Shahnameh: Legends of Persia, the key insight is this: Dark Souls' most beloved elements (combat weight, cryptic lore, world interconnectivity) are actually **cheaper to produce** than mainstream alternatives like cutscenes and tutorials.

---

## FromSoftware's resources and commercial performance

Dark Souls launched September 22, 2011 in Japan after approximately **2.5 years of development** beginning June 2009. The credited team of ~195 people included third-party developers, localization, and publishing support—the core FromSoftware team was likely **70-80 developers**. Director Hidetaka Miyazaki has stated that three years represents his ideal development cycle, providing "enough room for implementing new and innovative ideas" while maintaining focus.

The game runs on FromSoftware's proprietary **"Dantelion" engine**, not Sony's PhyreEngine as commonly misattributed. This in-house technology evolved from Demon's Souls and would power every subsequent FromSoftware title through Sekiro. The engine used Havok middleware for physics but handled rendering, animation, and game systems internally.

Commercial performance exceeded expectations for what was considered a niche "hard game." Dark Souls 1 sold **2.37 million copies by April 2013**, with the full Dark Souls series reaching **~40 million units by 2024**. The game received an **89/100 on Metacritic** (PS3/Xbox 360) with 97% positive critic reviews and 84% positive user scores. The original development budget was never disclosed, though industry estimates range from $5-20 million—notably modest compared to contemporary Western AAA titles.

Recognition came immediately and has only grown: Edge Magazine named it the **#1 greatest videogame ever** in 2015, and the Golden Joystick Awards crowned it the **Ultimate Game of All Time** in 2021. On Steam, Dark Souls Remastered maintains a 92% positive rating from over 141,000 reviews, with **3,000-4,300 concurrent players** still active 13+ years after release.

---

## How stamina and animation commitment create tension

Dark Souls' combat feels fundamentally different from other action RPGs because it operates on a principle of **animation priority**—once an attack begins, the animation must complete before any other action can execute. This creates what players describe as "weight" but is technically an enforced vulnerability window. The three-phase attack structure (anticipation → active frames → recovery) means every swing is a calculated decision, not a reaction.

The **stamina system** unifies all combat decisions into a single resource pool. Maximum stamina caps at 160 points (at 40 Endurance) with a base regeneration of 45 points per second. Critically, after full depletion, there's a **0.70-second delay** before regeneration begins. Every action—attacking, rolling, blocking, parrying—draws from this same pool, forcing players to constantly ask: "Can I still dodge after this attack?" This interconnected resource management distinguishes souls-like combat from button-mashing alternatives.

Equipment load creates meaningful build decisions through roll quality thresholds. Below 25% equip load enables fast rolls with quick recovery. The 26-50% range produces medium rolls. Above 50% creates the nearly unusable "fat roll" with extended vulnerability. All roll types provide **11 invincibility frames**, but faster rolls return to neutral sooner—the difference isn't protection duration but recovery speed.

Boss design follows a progressive curriculum structure. The Asylum Demon teaches patience and environmental awareness. Gargoyles introduce multi-target management. Quelaag demands pattern recognition. **Ornstein & Smough** serves as the mid-game examination combining every previous lesson. Miyazaki's philosophy emphasizes "tough but fair"—enemies have readable wind-ups (typically 340+ milliseconds), and every death should teach players what they did wrong.

---

## Environmental storytelling replaces expensive cutscenes

Miyazaki's approach to narrative emerged from his childhood experience reading English fantasy gamebooks without full comprehension. Unable to understand every word, he used imagination to fill gaps—this became Dark Souls' core storytelling philosophy. As he explained in interviews: "I try to make a game that has beautiful open spaces, gaps, room for players to enjoy it in ways that were not authored."

**Item descriptions** carry the lore burden instead of cinematics. Finding a sword on a corpse provides both a functional reward and a tragic mini-story about the "once-noble knight now hideously transformed" into the boss you just defeated with their own weapon. This technique costs virtually nothing—text is the cheapest game asset—while creating deeply engaged communities of lore-hunters who discuss theories and interpretations.

Cutscenes in Dark Souls are **nearly nonexistent** by deliberate design. The opening cinematic establishes cosmic backstory (Age of Fire, Lord Souls) as necessary world foundation. Boss introductions last mere seconds, serving as gameplay warnings rather than story dumps. Instead of showing a cutscene about an ancient battle, the game lets players deduce history by observing devastated battlefields, positioned corpses, and contextual item placement.

The interconnected world design creates spatial mastery without fast travel. Firelink Shrine functions as a central hub connecting Undead Burg, New Londo Ruins, and the Catacombs. Shortcuts—kicked-down ladders, one-way doors, hidden elevators—loop areas back to safe points, transforming linear paths into circular mastery. As the design analysis notes: "a path that could be reached in a straight line is forcibly made into a circle." This technique makes smaller worlds feel larger while reducing backtracking frustration.

---

## What players love and what frustrates them

Steam reviews reveal consistent praise patterns: **level design** universally described as "masterclass," **atmosphere** creating immersive dark fantasy, and the **sense of accomplishment** from overcoming challenges. One reviewer captured the community sentiment: "Every time I died, I felt like it was my fault." This perceived fairness—despite extreme difficulty—defines the souls-like appeal.

The criticisms are equally consistent. **Late-game areas** (Lost Izalith, Tomb of Giants) feel rushed and incomplete compared to early brilliance. The **Bed of Chaos** boss is universally condemned as poorly designed, relying on RNG-dependent platforming rather than combat skill. The original **PC port** locked resolution at 1024x720 with 30 FPS caps, requiring the fan-made DSfix mod to become playable—producer Takeshi Miyazoe admitted the port was rushed.

What keeps players returning for 13+ years includes **build variety** (STR, DEX, INT, FAI combinations), **New Game+ scaling** through NG+7, and **challenge runs**. The speedrunning community remains active with 1,948 submitted runs from 723 unique players. Soul Level 1 runs, no-hit attempts, and weapon-restricted playthroughs extend replayability indefinitely.

Community health indicators are exceptional: r/darksouls remains active for discussions, "Return to Lordran" events draw thousands of players, and meme culture ("Praise the Sun," "Don't Give Up, Skeleton") demonstrates cultural penetration. Academic research from CHI 2025 found Dark Souls actually helps players cope with depression through cultivating resilience, triggering existential reflections, and enabling supportive online communities.

---

## Design analysis videos that informed this study

**"The World Design of Dark Souls" (Game Maker's Toolkit)** provides the definitive level design breakdown. Mark Brown analyzes how visual landmarks visible from multiple areas create spatial awareness, how shortcuts function as meaningful rewards, and how vertical stacking creates depth without additional content. The key insight: every location should be visible from at least one other location to reinforce world cohesion on tight budgets.

**"Strategic Design Or: Why Dark Souls is the Ikea of Games" (GDC 2017)** by Justin Fischer applies business strategy frameworks to explain Dark Souls' success. The crucial lesson: competitive advantage comes from what you DON'T do. Dark Souls deliberately excluded cutting-edge graphics, tutorials, and accessibility features to concentrate resources on atmosphere and challenge. "Activity fit" matters—every design element reinforces every other element.

**Illusory Wall's "Dark Souls Dissected" series** reverse-engineers obscure mechanics including matchmaking ranges, humanity drops, and NPC spawn conditions. The takeaway for indie developers: hidden mechanics create mystery and community. Undocumented systems gave players reasons to experiment and share discoveries, extending engagement without additional content.

The **Dark Souls Design Works interview** reveals Miyazaki's collaborative art direction method. He provided artists with simple "image words" as starting points, letting them interpret freely before refining results together. When an artist submitted an undead dragon "swarming with maggots," Miyazaki rejected it: "Don't rely on the gross factor... Can't you instead try to convey the deep sorrow of a magnificent beast doomed to a slow and possibly endless descent into ruin?" This philosophy—**dignified tragedy over shock**—permeates all visual design.

---

## What 2-person teams have actually achieved

**Salt and Sanctuary** stands as the definitive proof case. Created entirely by James and Michelle Silva (Ska Studios), this 2D souls-like includes **600+ weapons and items**, full stamina-based combat, interconnected metroidvania structure, and multiple character builds—all from a two-person team over approximately three years. If Shahnameh's team seeks validation that their scope is achievable, Salt and Sanctuary provides it.

**Hollow Knight** began with three core developers (Ari Gibson, William Pellen, Jack Vine) on a $57,000 AUD Kickstarter budget. It sold over **15 million copies** by making smart scope decisions: 2D metroidvania structure eliminates 3D complexity, limited dialogue reduces voice acting costs, and environmental storytelling conveys depth cheaply. The game proves that souls-like difficulty and atmosphere translate perfectly to 2D.

**Mortal Shell** demonstrates what a slightly larger indie team (15 people average) can achieve with AAA veterans. Their key constraint decision: only **4 "shells"** (body types) instead of hundreds of armor combinations. This limitation became a unique feature rather than a shortcoming. The team "doubled down on strengths," focusing on atmosphere and visuals within ruthlessly constrained scope—4 areas, 8 bosses, no multiplayer.

**TUNIC** (solo developer Andrew Shouldice, 7 years) shows how isometric 3D with stylized art direction can hide limitations while adding unique hooks. Its hidden instruction manual and puzzle integration created distinction beyond "another souls-like."

### What's realistically achievable for Shahnameh

Based on indie precedents, a 2-person team working 3-5 years can create:

- **2D or isometric perspective** (not full 3D open world)
- **5-10 hours of content** with high replay value
- **8-15 unique enemy types** (quality over quantity)
- **4-8 boss encounters** with learnable patterns
- **3-5 distinct areas** with interconnected shortcuts
- **Single weapon type or simplified combat system** (Sekiro model)
- **Environmental storytelling** with minimal voice acting
- **No multiplayer** (adds massive complexity)

---

## Specific lessons for Shahnameh's Persian mythology setting

### Combat design achievable with free tools

The souls-like combat "feel" requires three core systems implementable in any engine: **animation commitment** (attacks complete before new inputs register), **stamina management** (unified resource pool for offense and defense), and **invincibility frames on dodges** (brief windows of immunity during roll animations). These are code implementations, not asset requirements.

**Godot 4** provides a zero-royalty engine option with excellent 2D and capable 3D. **Blender** handles all modeling, rigging, and animation needs—Blender Studio's "Dogwalk" project demonstrates seamless Godot integration. For concept art, **Stable Diffusion** running locally can generate Persian-inspired architectural references, costume designs, and creature concepts for refinement. **AudioCraft** and **LMMS** cover placeholder and final audio needs.

The single-weapon model used by Sekiro and Titan Souls reduces animation workload dramatically. For Shahnameh, a signature Persian weapon (shamshir sword, sagaris axe, or mace-and-chain) could anchor combat, with depth coming from technique variety rather than weapon variety.

### Persian epic integration through environmental storytelling

The Shahnameh's episodic structure of heroic tales naturally fits Dark Souls' fragmented lore approach. Rather than lengthy cutscenes explaining Rostam's seven labours or the tragedy of Sohrab, these stories can be conveyed through:

- **Item descriptions** on weapons and armor referencing legendary figures
- **Environmental setpieces** showing aftermath of mythological events
- **Corpse positioning** telling tragic mini-narratives
- **Architectural ruins** implying fallen civilizations (Zal's fortress, Afrasiyab's kingdom)

The cryptic, player-interpreted nature of Dark Souls lore actually suits Persian mythology's poetic ambiguity. Miyazaki's "narrative gaps" philosophy—deliberately incomplete storytelling requiring player interpretation—mirrors how mythology traditionally operates through symbolic resonance rather than explicit explanation.

### Boss design patterns for Persian heroes and demons

Dark Souls bosses follow a curriculum structure applicable to Shahnameh. Early bosses teach fundamental skills (blocking, timing, pattern recognition). Mid-game bosses combine multiple mechanics. Late-game encounters demand mastery.

For Persian mythology, consider:
- **Teaching boss**: A basic div (demon) with telegraphed attacks
- **Combination boss**: Ahriman's servants requiring multi-target awareness
- **Mastery examination**: A legendary hero (corrupted Esfandiyar, fallen Afrasiyab) combining all previous lessons

Each boss should have **5+ randomly-sequenced attacks** to prevent memorization of fixed patterns while maintaining readable wind-ups for fair difficulty.

### Episodic structure advantages

Dark Souls' weakest sections (Lost Izalith, Crystal Cave) suffered from development time constraints. An **episodic release model** for Shahnameh could actually improve quality by allowing focused development on each segment. Each episode could feature:

- One Persian tale adapted (Rostam and Sohrab, Bizhan and Manijeh, Zal and Rudabeh)
- 2-3 hours of content
- 2-3 boss encounters
- Interconnected level design within the episode
- Persistent character progression across episodes

This model matches the Shahnameh's anthology structure while managing scope for a small team.

---

## Strategic design philosophy to adopt

### Embrace constraints as features

Dark Souls succeeded through strategic trade-offs, not superior execution across all dimensions. Sparse tutorials, limited music, cryptic storytelling, and no difficulty options were deliberate choices that concentrated resources. As the GDC analysis notes: "Don't try to appeal to everyone—serving a specific niche excellently creates devoted fans."

For Shahnameh, identify what you're NOT building: no multiplayer, no complex character customization, no voice acting for most content, no day/night cycles, no procedural generation. Each eliminated feature frees resources for core excellence.

### Every design element must reinforce every other element

Dark Souls' "activity fit" means difficulty supports cryptic storytelling (players earn understanding through struggle), which supports exploration (discovering lore requires investigating), which supports combat (encounters guard discoveries). No element exists in isolation.

For Shahnameh, consider: How does Persian mythology's fatalistic philosophy reinforce challenging gameplay? How does the episodic structure affect progression systems? How does environmental storytelling serve both lore and level design?

### Find your unique hook

Every successful indie souls-like has one distinctive element beyond "Dark Souls but indie":

- Hollow Knight: Bug world, metroidvania progression
- Salt and Sanctuary: 2D with full RPG depth
- TUNIC: Hidden manual, puzzle integration
- Another Crab's Treasure: Comedy shell system
- Mortal Shell: Body-possession mechanic

For Shahnameh, the Persian mythology setting itself provides distinction, but consider what mechanical hook makes it MORE than "Dark Souls with Persian aesthetics." Perhaps the legendary farr (divine glory) of Persian kings could function as a unique resource system, or the dualistic Zoroastrian cosmology could create light/dark combat mechanics.

---

## Technical feasibility summary

| Aspect | Dark Souls Approach | Shahnameh Recommendation |
|--------|---------------------|-------------------------|
| Engine | Proprietary Dantelion | Godot 4 (free, no royalties) |
| Team Size | ~70-80 core devs | 2 developers + contract audio |
| Timeline | 2.5 years | 3-5 years (episodic releases) |
| Art Direction | Dark medieval 3D | 2D/isometric stylized (reduces workload) |
| Combat | Complex builds, many weapons | Single weapon, technique depth |
| World Structure | Interconnected open world | Episodic interconnected levels |
| Storytelling | Items, environment | Same (ideal for small teams) |
| Multiplayer | Invasions, co-op, messages | None (massive scope reduction) |
| Voice Acting | Minimal, cryptic NPCs | Minimal or AI-assisted placeholder |

---

## Conclusion: The achievable path forward

Dark Souls' greatest design innovations—animation commitment, stamina management, environmental storytelling, interconnected shortcuts, and "tough but fair" difficulty—are **implementation patterns, not budget requirements**. A 2-person team with 3-5 years and free tools can absolutely create a compelling souls-like experience, as proven by Salt and Sanctuary, Hollow Knight, and TUNIC.

The critical success factor is **ruthless scope constraint combined with a unique hook**. Shahnameh's Persian mythology setting provides cultural distinction unavailable to Western-developed souls-likes. The episodic structure offers natural scope management. Environmental storytelling suits mythological ambiguity perfectly. AI-assisted development tools (Blender, Stable Diffusion, AudioCraft) reduce asset creation burden.

What Shahnameh should NOT attempt: full 3D open world, complex build systems, multiplayer, extensive voice acting, or matching Dark Souls' content volume. What it SHOULD pursue: distinctive Persian aesthetic, weighty combat with limited but deep weapon options, cryptic lore delivery through items and environments, and interconnected level design within each episode.

Dark Souls proves that constraint breeds creativity. The game's most beloved elements emerged from limitations, not resources. For Shahnameh, the path forward is clear: embrace what a 2-person team can do excellently rather than imitating what a 195-person team achieved at scale.