# Elden Ring competitive analysis for Shahnameh: Legends of Persia

FromSoftware achieved the seemingly impossible: a **200-person team** created a 96 Metacritic masterpiece with **30+ million sales**, proving that focused design philosophy trumps raw resources. For a 2-person team building an episodic action-adventure based on Persian mythology, the critical insight is this: Elden Ring's most praised elements—environmental storytelling, commitment-based combat, and player-driven discovery—scale down remarkably well, while its weaknesses (boss repetition, performance issues, scope bloat) stem from overextension that smaller teams can strategically avoid.

The analysis below distills actionable patterns from FromSoftware's approach, separating what requires massive resources from what a lean, AI-assisted development process can realistically achieve.

## The scale gap: 200 developers versus 2

Elden Ring's development required **200-230 developers at peak** working for approximately **5 years** with an estimated **$100-200 million budget**. FromSoftware employed a co-director system with Hidetaka Miyazaki sharing responsibilities with Yui Tanimura, enabling parallel development streams. The team outsourced art assets to studios like Lakshya Digital while maintaining core design in-house.

Despite this, FromSoftware operates lean by AAA standards—Ubisoft uses 2,000+ developers for Assassin's Creed titles. Miyazaki himself stated that Elden Ring represents "the limit" of FromSoftware's scope, acknowledging that "room for failure isn't tolerated as much as I think it was in the past."

| Metric | Elden Ring | Shahnameh Implication |
|--------|------------|----------------------|
| Team size | 200-230 | Focus on 1% of scope, 100% of polish |
| Budget | $100-200M estimated | AI tools and free engines democratize quality |
| Dev time | 5 years | Episodic format enables iterative releases |
| Engine | Proprietary (15+ years iteration) | Unreal/Godot with marketplace assets |
| Content volume | 100+ hours, 238 bosses | 3-5 hours per episode, 5-8 unique bosses total |

The core lesson: FromSoftware's **proprietary engine** represents 15 years of accumulated iteration—an asset impossible to replicate. However, modern tools like Unreal Engine 5, AI-assisted animation, and procedural generation close significant gaps for focused experiences.

## What players actually praise: lessons in design values

Steam's **94% positive rating** (1.1 million reviews) reveals what players genuinely value—and much of it requires design discipline rather than massive resources.

**Complete product philosophy** dominates praise. Players repeatedly cite Elden Ring as a benchmark for value: "First game in a long time where you get exactly what you paid for...no microtransactions, no battle pass, just a massive playground." For an indie team, this translates to: deliver a polished, complete episodic experience rather than a sprawling incomplete one. Players will forgive smaller scope; they won't forgive feeling nickeled-and-dimed.

**Discovery-driven exploration** generates the strongest emotional responses. Comparisons to Breath of the Wild's sense of wonder appear constantly. The design principle: reward curiosity without signposting everything. A single well-hidden cave with meaningful loot creates more player satisfaction than ten marked waypoints. This approach is actually **cheaper** than comprehensive map markers and quest tracking systems.

**Difficulty through design, not menus** resolves the accessibility debate elegantly. Spirit Ashes summons, open-world leveling, and cooperative play let players self-regulate challenge without explicit difficulty settings. For Shahnameh, consider similar tools—AI companions, optional side content for overleveling, or tiered encounters—that give players agency without fragmenting the community into "easy mode" and "real game" camps.

**Environmental storytelling** receives near-universal acclaim while requiring primarily design skill rather than expensive assets. Item descriptions, corpse placement, architectural decay, and visual symbols tell stories economically. A collapsed bridge with a sword lodged in stone conveys narrative without voice acting, mo-cap, or branching dialogue trees.

## Critical weaknesses to avoid: where scale hurt quality

Elden Ring's weaknesses almost universally stem from scope overextension—exactly what a small team can sidestep.

**Boss repetition** is the most consistent criticism. With 238 total bosses (only ~104 unique designs), players encounter the same Erdtree Avatars and Ulcerated Tree Spirits across dozens of dungeons. Community consensus: "The boss reuse is insane. The thrill of encountering bosses is gone after the first third of the game." For Shahnameh, **fewer unique bosses will create stronger impressions than many repeated ones**. Five genuinely distinct encounters based on Shahnameh heroes/demons will outperform twenty recycled designs.

**Mini-dungeon repetition** follows the same pattern. Catacombs and caves follow identical templates with predictable "a gate has opened somewhere" puzzles. Mark Brown (Game Maker's Toolkit) specifically criticizes how this "undermines the sense of mystery over time." An episodic structure naturally avoids this—each episode can feature distinct dungeon design without needing procedural templates to fill a massive map.

**Performance issues** nearly killed launch reception. Despite 96 Metacritic, early Steam reviews were "Mixed" due to stuttering and optimization problems. Players wrote: "Elden Ring? More like stutter-ing." For a small team, **stability is non-negotiable**—players forgive limited scope before they forgive crashes and frame drops. Test relentlessly on minimum-spec hardware.

**Obtuse quest design** frustrates accessibility advocates. No quest log, NPCs who move unpredictably, and easily-broken questlines require players to maintain external notes or consult wikis. While hardcore players appreciate this, many cite it as needlessly punishing. For Shahnameh, consider a minimal journal system that records NPC names and last known locations without explicit waypoints—preserving mystery while reducing frustration.

## Combat systems: what scales and what doesn't

Elden Ring's combat succeeds through **animation commitment**—the intentional inability to cancel attacks mid-swing. This forces prediction over reaction, creating meaningful decisions. Implementing this principle costs nothing; it's purely design philosophy.

### Scalable combat elements for a 2-person team

**Stamina management** is fundamentally a resource bar with regeneration rules. Attacks, dodges, and blocks consume stamina; running empty creates vulnerability windows. This creates tension through simple math, not complex AI. A small team can implement this system with straightforward programming.

**I-frame dodging** provides skill expression through invincibility frames during rolls. Elden Ring uses ~13 frames of invincibility at the roll's start. The principle—brief invulnerability windows requiring timing precision—requires tuning, not massive development resources.

**Stance breaking** creates satisfying combat feedback. Heavy attacks fill an invisible bar; when it breaks, enemies stagger for critical hits. This rewards aggressive play and creates momentum shifts. Implementation requires tracking a hidden value and triggering a stagger animation—achievable for any team.

**Guard counters** (block, then heavy attack) reward defensive play without complex parry timing. This mechanical addition significantly expanded viable playstyles in Elden Ring and requires minimal implementation complexity.

### Complex systems requiring large teams

**Ashes of War modular system** features 116 unique abilities with FP costs, scaling calculations, and weapon compatibility matrices. Each ability requires unique animations, VFX, balance passes, and integration testing. This represents hundreds of developer hours.

**Spirit Ashes AI companions** involve 84 different summons with pathfinding, attack patterns, scaling, and boss aggro management. Creating believable, helpful AI companions that don't trivialize or frustrate encounters requires extensive iteration.

**Boss AI with variable timing** represents Elden Ring's most sophisticated system. Late-game bosses use input reading (detecting player healing and punishing), delayed attacks to bait early dodges, and multi-phase transitions with distinct movesets. Joseph Anderson's analysis shows bosses like Malenia have "extremely long combos with few punish windows"—tuning this balance consumed significant development resources.

**Mounted combat** requires separate movement systems, attack animations, Torrent's AI, arena restrictions, and special traversal (spirit springs, double jump). This adds significant complexity for what is ultimately a complementary system.

## World-building patterns applicable to Persian mythology

FromSoftware's collaboration with George R.R. Martin offers a directly applicable model. Martin wrote **foundational mythology as backstory**, not in-game narrative. He created heroic characters and historical events; FromSoftware then "broke" these heroes into corrupted boss encounters.

### The foundation-first approach

For Shahnameh, this suggests writing comprehensive Persian mythological backstory before any gameplay narrative. The Pishdadian and Kayanian dynasties provide rich pre-game history. Heroes like Rostam, Siavash, and Sohrab can be established as legendary figures whose corrupted or tragic states players encounter in-game. Miyazaki described using Martin's work "like a dungeon master's handbook"—comprehensive reference material that informs all subsequent design decisions.

### Fragmented lore delivery

Elden Ring distributes narrative across item descriptions, environmental details, and cryptic NPC dialogue. Radahn's entire backstory—learning gravity magic specifically to continue riding his beloved horse—is revealed through spell descriptions and remembrance text, never stated directly.

For Shahnameh, this approach is ideal. Fragment the epic across dozens of items: a sword description mentioning "the son who fought his father unknowing" gradually reveals Rostam and Sohrab's tragedy. Persian poetry excerpts as NPC dialogue create atmosphere while conveying narrative fragments. This method is **more economical** than fully-voiced, branching narratives while delivering comparable storytelling satisfaction.

### Environmental storytelling with Persian aesthetics

Each Elden Ring region reflects its ruler's story—Caelid's rot shows Malenia's devastation. Apply this principle with Persian architectural vocabulary: Persepolis-style columns in decay, Zoroastrian fire temples corrupted by Ahriman's influence, the Faravahar symbol appearing throughout as environmental marker.

The Erdtree serves as Elden Ring's constant visual anchor, visible from anywhere outdoors. For Shahnameh, consider an equivalent landmark—perhaps Mount Damavand (where Zahhak is imprisoned) or a corrupted fire temple representing Zoroastrian struggle.

### Mythological layering technique

Elden Ring blends Celtic, Norse, Arthurian, and Japanese influences without explicitly identifying sources. The giant bear enemy could reference Celtic Artio, Greek Artemis, or Tolkien's Beorn—FromSoftware never confirms. This deliberate ambiguity invites player interpretation and community theory-crafting.

Shahnameh can layer Persian mythology (primary), Zoroastrian cosmology (Ahura Mazda vs. Ahriman), Mesopotamian influences, and Islamic mysticism without over-explanation. Let scholars debate sources while players experience cohesive fantasy.

## Scope management: FromSoftware's smart decisions

Elden Ring's scope statistics reveal intentional constraints alongside ambition.

**Content metrics:**
- Main story: 44-55 hours
- Completionist: 100-130 hours  
- Map size: ~79 km² (comparable to GTA V)
- Legacy dungeons: 6 major Souls-style areas
- Total bosses: 238 (11-17 mandatory)
- Weapons: 308 base game

The critical insight: **90% of content is optional**. Players can complete Elden Ring fighting only 11-17 bosses. This means FromSoftware front-loaded their best work for the critical path while filling optional content with more repetitive but still serviceable encounters.

### Episodic structure advantages for Shahnameh

An episodic format offers scope advantages Elden Ring lacked:

**Focused polish per episode.** Rather than spreading 200 developers across 100+ hours, concentrate all effort on 3-5 hours of exceptional content. Each episode can receive the attention FromSoftware gives legacy dungeons rather than procedural catacombs.

**Iterative feedback loops.** FromSoftware's November 2021 network test provided crucial feedback: "Things developers take for granted...stuff that users found difficult to figure out." Episodic releases enable continuous refinement between installments.

**Manageable combat encounters.** Instead of 238 bosses requiring massive repetition, budget 5-8 unique bosses per episode based on Shahnameh characters. Rostam, the White Div, Zahhak—each deserves distinctive design rather than palette-swapped variants.

**Progressive complexity.** Early episodes can establish core mechanics; later episodes introduce advanced systems. This mirrors how Elden Ring introduces guard counters, Ashes of War, and spirit summons gradually rather than overwhelming players at start.

## YouTube analysis insights: what design experts observe

Three high-quality analysis videos provide additional perspective:

**Game Maker's Toolkit** (Mark Brown) examines world design, noting how environmental landmarks replace UI markers: "The Erdtree functions as a constant reference point—players always know where they are relative to it." For Shahnameh, establish equivalent visual anchors early.

**Joseph Anderson** (1h 39m deep dive) analyzes combat tuning, concluding late-game bosses "push against the limits of established combat mechanics" with input reading and minimal punish windows. His criticism: the game's best moments come from fair, readable patterns—not artificial difficulty through long combo strings.

**NakeyJakey** traces FromSoftware's philosophy: "merciless, uncompromising gameplay-first design with little hand-holding can also still be a massive success." The key word is "gameplay-first"—narrative, graphics, and scope serve combat satisfaction, not the reverse.

## Actionable recommendations for a 2-person team

### Directly adaptable patterns

**Animation commitment combat.** Implement stamina management, I-frame dodging, and stance breaking. These systems create Souls-like feel through design rules, not massive animation libraries. A single weapon class with 4-5 attack animations (light, heavy, charged, jumping, rolling) provides sufficient variety for an episode.

**Environmental narrative delivery.** Write comprehensive Shahnameh backstory first. Fragment across item descriptions, environmental details, and cryptic NPC dialogue. This approach costs design time, not development resources.

**Player-controlled difficulty.** Include summoning mechanics, optional content for overleveling, or difficulty-adjacent options (AI companions, consumable buffs) rather than menu sliders. Players appreciate agency over explicit difficulty settings.

**Discovery-focused design.** Hide meaningful content off critical paths. Reward exploration without requiring it. A single well-designed optional area with unique boss creates more player satisfaction than extensive mandatory content.

**Visual anchoring.** Establish a constant landmark visible throughout episodes—Mount Damavand, a corrupted fire temple, or celestial phenomenon—that orients players and provides identity.

### Patterns requiring significant adaptation

**Boss variety through narrative rather than mechanics.** Where FromSoftware creates 100+ unique boss designs, Shahnameh should create 5-8 bosses with rich narrative context. Each boss representing a Shahnameh figure deserves unique dialogue, arena design, and story integration that compensates for mechanical limitations.

**Vertical slice polish over horizontal scope.** Rather than repeating content to fill massive maps, create smaller environments with exceptional density. Every room should contain discoverable narrative or meaningful encounters.

**AI-assisted asset creation.** Use procedural generation, AI upscaling, and marketplace assets strategically. FromSoftware's proprietary engine represents 15 years of iteration—modern tools can compress this advantage significantly for focused scope.

### Patterns to explicitly avoid

**Do not attempt open world.** Elden Ring's map required 200 developers and still suffered from repetition criticism. Linear or hub-based structure enables quality control at small scale.

**Do not create dozens of similar dungeons.** Elden Ring's catacombs are its weakest content. Create fewer, more distinct environments.

**Do not implement complex weapon modularity.** Ashes of War's 116 abilities represent massive scope. Select 5-8 weapon arts that complement Persian mythology themes and polish thoroughly.

**Do not sacrifice performance for visuals.** Elden Ring's launch stuttering generated Mixed Steam reviews despite critical acclaim. Stable 30+ fps on modest hardware trumps graphical fidelity.

## Conclusion: leveraging asymmetric advantages

Elden Ring's 96 Metacritic score comes from **design philosophy execution**, not resource abundance. The most praised elements—discovery, environmental storytelling, commitment-based combat, respect for player intelligence—scale down effectively. The most criticized elements—repetition, performance issues, scope bloat—stem from overextension that episodic structure naturally avoids.

For Shahnameh: Legends of Persia, the competitive advantage lies in **focus**. A 2-person team cannot compete on content volume but can compete on polish density, narrative authenticity, and design coherence. Persian mythology offers distinctive theming that no AAA studio is currently exploring; AI-assisted development compresses traditional asset creation timelines; episodic format enables iterative refinement based on player feedback.

The FromSoftware formula worth replicating: create an experience where players feel respected, challenged fairly, and rewarded for curiosity. This requires design discipline and player empathy—resources that don't scale with team size.