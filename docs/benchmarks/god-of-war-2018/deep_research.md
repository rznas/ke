# God of War (2018): Competitive Analysis for Shahnameh Development

God of War (2018) represents the gold standard for mythology-based action-adventure games, achieving a **94 Metacritic score** and selling **23+ million copies** through masterful combat design, authentic Norse mythology integration, and emotionally resonant father-son storytelling. For a 2-person team developing Shahnameh: Legends of Persia, this analysis extracts the achievable design principles from the AAA spectacle—particularly the Leviathan Axe's satisfying "game feel" built through layered feedback systems, the Mimir-style lore delivery through companion dialogue, and the focused scope decisions that prioritized depth over breadth.

---

## Game overview and development context

Santa Monica Studio developed God of War (2018) over approximately **5 years** (June 2013 – April 2018) with an estimated **200-300+ developers** and a budget likely between **$44-100 million** (neither officially confirmed by Sony). The game runs on Santa Monica's proprietary engine—not Unreal or Decima as sometimes misreported—with Havok physics middleware.

Director Cory Barlog pitched the Norse mythology reboot after returning to the studio in 2013, facing significant internal resistance. Forty percent of the team initially disagreed with his revolutionary "one-shot camera" approach, with some calling it "crazy" and "impossible." The team had previously considered Egyptian and Mayan mythologies before settling on Norse for its geographic isolation from Greece and the creative flexibility afforded by sparse source material.

| Metric | Confirmed Data |
|--------|---------------|
| Metacritic (PS4) | 94/100 (118 reviews) |
| User Score | 9.0/10 (29,372 ratings) |
| Total Sales | 23 million (November 2022) |
| Development Time | ~5 years |
| Engine | Proprietary (Santa Monica Studio) |
| Awards | GOTY at The Game Awards, BAFTA, DICE, GDC, SXSW |

---

## Core relevance to Shahnameh development

God of War's success offers three directly transferable lessons for Persian mythology adaptation. First, the game proves that **lesser-known mythological figures can become compelling characters** through creative interpretation—Baldur had virtually no personality in the Eddas but became the game's most memorable antagonist. Shahnameh's supporting characters similarly offer creative freedom.

Second, the **Mimir companion model** demonstrates how mythology can be delivered organically. Mimir provides nearly **an hour of optional lore** during boat travel without breaking gameplay flow—a pattern achievable with AI voice synthesis tools. Third, the studio's decision to portray Thor and Odin as villains (deliberately countering Marvel's characterization) shows that **mythological authenticity can differentiate from mainstream depictions** rather than competing with them.

The combat system's satisfying "game feel" was built through **layered feedback systems** (rumble, sound, animation timing, camera shake) that are individually achievable with modern tools, even if the overall polish required years of AAA iteration.

---

## What players loved and criticized

### Reception highlights

Player praise consistently centered on three elements: the **Kratos-Atreus father-son relationship** ("you can clearly feel that 'dad & son' vibes"), the **Leviathan Axe throw-and-recall mechanic** ("Nothing beats the feeling of throwing the Leviathan Axe for the first time"), and **Mimir's mythology delivery** ("I loved the sheer amount of lore... told through Mimir"). The PC port achieved **97% positive Steam reviews**, with players praising technical optimization and calling it "the best version of a fantastic game."

The single-shot camera innovation received significant praise from critics (92% of professional reviews) for its cinematic immersion, though some players found the **restricted field of view** frustrating in combat: "The moment enemies get anywhere but directly in front of you you're basically helpless."

### Critical complaints

The most consistent criticism across Reddit, Metacritic, and review sites was **repetitive enemy variety**—particularly the overuse of trolls as mini-bosses. Kotaku noted: "Over the course of God of War I fought these trolls so many times that I genuinely became angry about it." With only **~23 enemy types** across 20+ hours, players noticed the repetition despite visual variations.

Other complaints included the **"hallway feel" of level design** lacking verticality from previous games, **grindy optional content** (Muspelheim and Niflheim described as "slogs"), and **RPG elements feeling tacked-on** ("pointless and completely out of place"). The close camera requiring threat indicators for off-screen enemies divided players between those who appreciated the intimacy and those who found it limiting.

---

## Combat system mechanics deep dive

### The Leviathan Axe satisfaction formula

Lead System Designer Vince Napoli documented how the axe's satisfying feel came from **layered feedback systems**, not individual features. The throw-and-recall mechanic combines:

- **Three separate controller rumbles**: triggering, flight, and catch
- **Sound dynamically tied to rotation speed**: audio changes as the axe spins
- **Spatial audio**: sound emitter attached to the axe so players hear it approach in surround sound
- **Camera shake on catch**: adds weight to the return
- **"Axe wiggle"**: 0.1-second programmatic wiggle before extraction from surfaces (originally longer, reduced after playtests showed it felt like input delay)
- **Return path using curved arc**: not a straight line, with tight-angle auto-seeking

The team hard-capped return time at **1.5 seconds** regardless of distance—speed automatically increases for distant throws to maintain responsiveness. This specific technical decision is directly replicable for Shahnameh's weapons.

### Combat feel balance

God of War achieves a **"weighty AND responsive"** feel by using:

- **Generous input buffering**: pressing attack queues the next action, making combat feel fluid rather than demanding frame-perfect timing (contrasting with Sekiro's minimal buffering)
- **Hit stop technique**: on hit, both Kratos and target freeze on the first frame for a short duration, creating sensation of resistance
- **Different animations for hits vs. misses**: follow-through animation changes when contact is made
- **Attack commitment once initiated**: cannot steer attack away from target, but sidesteps maintain combo sequences while rolling resets them

### Boss and enemy design patterns

The Baldur fights teach mechanics through attack telegraph colors: **no indicator** (blockable), **yellow ring** (parryable), **red ring** (unblockable/must dodge). This visual language system is scalable to indie development and critical for teaching players combat depth without tutorials.

The game's **major design failure** was repetitive mini-bosses—trolls used approximately **10 times** with similar three-move patterns and only elemental palette swaps. This demonstrates that even AAA teams struggle with enemy variety at scale. For Shahnameh's episodic scope, **fewer, more distinctive boss encounters** will serve better than repetitive mini-bosses.

---

## Norse mythology handling: lessons for Persian adaptation

### Research and authenticity approach

Santa Monica Studio relied heavily on the **Poetic Edda and Prose Edda** as primary sources, with Barlog stating they "used the actual Edda's as the inspiration and launching-off point." No named cultural consultants were found in public documentation, though composer Bear McCreary was specifically brought in to discuss "folk music, mythology, Nordic ethnic instruments."

The team recognized that Norse sources were **sparse compared to Greek mythology**, which allowed creative freedom: "90% of sources are the Poetic Edda or the Prose Edda." Scholar Jackson Crawford (University of Colorado Boulder) observed that this sparseness meant "the seams are a lot more visible... they interpret it as less of something that belonged to a different culture, and more of a story they can interpret on their own."

### Balancing authenticity with entertainment

The game made **deliberate departures** from mythology for narrative purposes:

- **Baldur transformed** from "beautiful, popular, then dead" (with virtually no personality in sources) into a bitter, obsessive antagonist unable to feel due to his mother's protective spell
- **Thor and Odin portrayed as villains** deliberately to counter Marvel's heroic depictions: "I can sit here and say, 'Hey, these guys aren't charming heroes'" (Barlog)
- **Mimir reimagined** as a Celtic faerie named "Puck" (confirmed in Ragnarök) who traveled to Norse realms—blending mythologies to show interconnected pantheons
- **Loki/Atreus twist** created intentional timeline paradox with Jörmungandr (resolved via time travel)

### Mythology-to-gameplay integration

The **Jötnar Shrines** (11 collectibles telling giant stories) and **39 Lore Markers** with translatable Elder Futhark runes made mythology exploration rewarding without interrupting gameplay. Tyr's Temple contains artifacts from **multiple pantheons** (Celtic, Egyptian, Greek symbols) hinting at interconnected mythological worlds—a framework applicable to Shahnameh connecting Persian mythology to broader ancient Near Eastern traditions.

For Shahnameh, this suggests: use the Shahnameh as primary source material but recognize where the epic leaves gaps that invite creative interpretation. The success came from **respecting source material while making it their own**—not Hollywood-ifying mythology into "emotionless, culturally inaccurate CGI."

---

## Narrative design and the single-shot camera

### Why the one-shot camera worked

Camera Director Dori Arzi explained the technique's purpose: "Create deeper immersion in the story and promote stronger empathy towards the characters by making the viewer feel like they are literally taking the journey with our heroes." The camera functioned as "an additional character" shot documentary-style.

This required **invention of new production rules**—writers couldn't use "cut to" in scripts, and transitions required close collaboration between writers and camera direction. Barlog admitted the team used only **6-8 technical "tricks"** throughout the game, with everything else being "an absurd amount of planning."

For a 2-person team, the lesson isn't to replicate the one-shot approach but to understand that **bold creative constraints can differentiate a project** when executed with commitment. Episodic structure actually offers natural "cut points" between episodes that AAA continuous experiences lack.

### Father-son dynamic development

The Kratos-Atreus relationship was directly inspired by Barlog's own fatherhood. Early development made Kratos "too mean"—testers called it a "child-abuse simulator." Overcorrection made him "too nice, calm, and relaxed"—compared to Qui-Gon Jinn. Finding the balance became their "Rosetta Stone" for the rest of development.

The dialogue line "Father doesn't like people either" was pulled directly from Barlog's wife introducing him to strangers. This authenticity from personal experience elevated the narrative beyond typical video game writing. For Shahnameh, **grounding mythological characters in relatable human dynamics** (family honor, generational expectations, father-son conflict in Persian culture) could achieve similar resonance.

---

## Art direction and technical approach

The game shifted from Greek mythology's sun-baked marble to Norse settings: dense forests, snowy mountains, mystical caves. Art Director Raf Grassetti established a **"grounded, realistic style set in an environment that feels like a real place but with fantastical elements."**

An early development crisis occurred when the team realized "the game is all gray and brown"—adding blue became "a big deal" after initial resistance. Each realm received a **distinct visual identity**: Alfheim's ethereal light, Helheim's cold blues, Muspelheim's fire tones.

The team used **Physical-Based Rendering (PBR)** for the first time in the franchise, requiring "very accurate lighting to make characters look right." This is now standard in free engines like Unreal and Unity, making the core rendering approach accessible to indie teams through modern tools.

For asset efficiency, the Lake of Nine hub design used a **water-lowering mechanic** that recontextualized the same areas multiple times—a smart scope decision that maximized content from limited geometry. This approach of **revealing new content through environmental changes** rather than building entirely new areas is directly applicable to episodic development.

---

## Audio design principles

Sound played a critical role in the Leviathan Axe's satisfaction. Kratos's axe sounds combine "**brute force slam with lots of low end effort that ends with a high frequency slash**"—not just a slicing sound, but a weighted thud and crack. Sound was **dynamically tied to the axe rotation speed**, changing as the weapon spins through the air.

The spatial audio system attached a sound emitter directly to the axe, allowing players to hear it approach in surround sound before the controller rumble signaled the catch. This multi-sensory feedback layering is achievable with AI audio tools like **AudioCraft** for sound generation and **Wwise/FMOD** (with free indie licenses) for implementation.

---

## Development insights and scope management

### What they cut

Understanding scope decisions reveals where AAA teams prioritize:

- **Swimming** replaced with boat traversal
- **Free jumping** restricted to designated areas only
- **Instant-death platforming** cut due to camera proximity
- **Multiplayer** (present in previous game) eliminated for single-player focus
- **110 minutes of story content** for "Atreus Jerk Mode" compressed significantly
- **No demo** released because it would have delayed the game by months
- **No DLC**—Barlog pitched an expansion but it was "too ambitious" (would have warranted standalone release)

### Game content volume

| Content Type | Volume |
|--------------|--------|
| Main Story | 20-21 hours |
| Main + Extras | 32-33 hours |
| Completionist | 50-53 hours |
| Playable Realms | 6 of 9 |
| Unique Boss Encounters | ~8 main story |
| Valkyries (Optional) | 9 |
| Enemy Types | ~23 |

The **previous God of War games averaged 10-12 hours**—the 2018 entry essentially doubled content while the team grew from ~60 people to 200-300+.

### Production efficiency techniques

One revealing example: to solve armor clipping in a canoe-pulling cutscene, the team created **four different ropes** with unique joints, meshes, and heights, with the game selecting the appropriate one based on equipped armor. This brute-force approach illustrates that "sometimes it was faster to do something brute force than through 'clever' optimizations."

The side quest system used **four-tiered content structure**: Brok/Sindri quests (dungeons), wayward spirits (ghosts), treasure maps/artifacts, and milestones (Odin's ravens). This hierarchy allowed scaling effort to content importance.

---

## Key YouTube videos and GDC resources

### Priority 1: "Raising Kratos" Documentary
**Channel**: PlayStation (Official) | **Duration**: 2 hours | **URL**: youtube.com/watch?v=lJZWKBDXXFY

This free documentary chronicles the full 5-year development with candid footage of motion capture, team meetings, E3 reveal stress, and Barlog's emotional reaction to review scores. Essential viewing for understanding the human cost and creative process of AAA development.

### Priority 2: "Evolving Combat in God of War" (GDC 2019)
**Presenter**: Mihir Sheth (Lead Combat Designer) | **Duration**: ~60 min

Technical deep-dive into how the close camera changed combat design. Covers enemy AI aggression scoring, threat indicators for off-screen enemies, and preserving combat "tenets" during innovation. Most actionable for Shahnameh's combat system.

**Key insight**: The team spent **3 years iterating** on combat systems—their solution for off-screen threats (audio cues, threat indicators, Atreus calling out positions) is directly applicable to any close-camera action game.

### Priority 3: "Reinventing God of War" (GDC 2019)
**Presenter**: Cory Barlog (Creative Director) | **Duration**: ~60 min

High-level creative direction talk on pitching major changes, managing team doubt, and balancing fan expectations with innovation. Valuable for understanding how to make bold creative decisions stick.

### Priority 4: "Recalling the Leviathan Axe" (Game Developer article)
**Author**: Santa Monica Studio Designer | **Format**: Written technical breakdown

Extremely detailed breakdown of animation timing, rumble patterns, sound design, and iteration process for the axe mechanics. Most implementable resource for weapon feel design.

### Priority 5: "Taking an Axe to God of War Gameplay" (GDC 2019)
**Presenter**: Jason McDonald (Design Director) | **Duration**: ~60 min

Companion to the combat talk focusing on preserving franchise "feel" while changing weapons, enemies, and camera. Pairs with Mihir Sheth's talk for complete combat design picture.

---

## Key takeaways for Shahnameh development

### What's achievable with AI-assisted 2-person development

**Combat feel principles**: The Leviathan Axe's satisfaction comes from **layered feedback systems** individually achievable with modern tools:
- Rumble patterns through standard game engine APIs
- Dynamic audio through AudioCraft-generated sounds implemented in Wwise/FMOD
- Hit stop/hitlag through simple frame freezing (1-2 frames on hit)
- Animation polish through Blender with AI-assisted motion generation
- Visual effects through Stable Diffusion-generated sprites/textures refined in engine

**Mythology integration**: The Mimir model (companion providing optional lore during travel) is achievable with AI voice synthesis. Recording Persian mythology stories as optional dialogue during traversal requires writing effort but minimal technical complexity.

**Scope management**: God of War's ~23 enemy types across 20+ hours was criticized for repetition. An episodic game can succeed with **5-8 distinctive enemies per episode** if each has unique patterns and visual identity.

**Color-coded attack telegraphs**: The yellow/red ring system for parryable vs. unblockable attacks is simple to implement and solves combat readability across all skill levels.

### What requires AAA budget—avoid attempting

- **One-shot camera** throughout (requires massive animation/cinematics investment)
- **Full motion capture** with professional actors
- **Orchestral score** at Bear McCreary's scale (though AI composition can achieve acceptable results)
- **~23+ enemy types** without feeling repetitive (focus on fewer, more polished encounters)
- **20+ hour narrative campaign** (episodic 2-4 hour episodes better suit limited resources)
- **Nine distinct realms** with unique visual identities (focus on 2-3 deeply realized Persian locations)

### Specific design patterns for Shahnameh

1. **Create a "Mimir" equivalent**: A wise companion (poet, Zoroastrian priest, or spirit guide) who provides Shahnameh lore during exploration. AI voice tools make this achievable.

2. **Use mythological gaps creatively**: Lesser-known figures in the Shahnameh offer the same creative freedom Santa Monica found with Baldur. Develop distinctive characterizations that respect sources while filling narrative gaps.

3. **Design 3-4 distinctive boss encounters per episode**: Quality over quantity. Each boss should teach mechanics through color-coded telegraphs and have memorable attack patterns.

4. **Layer weapon feedback**: Even basic weapons can feel satisfying through rumble timing, sound design, hit stop, and animation transitions. This requires iteration, not budget.

5. **Build modular environments**: Lake of Nine's water-lowering approach recontextualized areas. For episodic content, design locations that can reveal new areas or change based on narrative progression.

6. **Counter mainstream Persian misconceptions**: Just as GOW showed villainous Odin/Thor (countering Marvel), Shahnameh can differentiate from "Arabian Nights" conflation by emphasizing authentic pre-Islamic Persian culture.

7. **Focus narrative on relatable human dynamics**: The father-son relationship elevated GOW above typical action games. Persian mythology's themes of honor, family duty, generational conflict, and heroic sacrifice offer similar emotional anchors.

### Honest scope expectations

God of War 2018 required ~300 developers, 5 years, and likely $50-100M to achieve its quality level. A 2-person team cannot match this scope. However, **focused episodic releases of 2-4 hours each** can achieve:

- Satisfying combat with 1-2 weapons (refined extensively rather than variety)
- 5-8 enemy types with distinctive patterns per episode
- 1-2 major boss encounters per episode
- Companion-delivered mythology during exploration
- One richly realized Persian environment per episode
- AI-generated voice acting and music supplemented with key human performances

The critical insight from GOW development: they spent **3+ years iterating on core mechanics** before the game felt right. For Shahnameh, invest disproportionate time in **weapon feel and combat responsiveness** during prototyping rather than content volume. The Leviathan Axe's satisfaction came from thousands of micro-adjustments to rumble timing, sound synchronization, and animation curves—work that can be done by a small team with patience and iteration.

---

*This analysis focuses on actionable insights for indie development. God of War (2018) represents an aspirational quality target, but its core design principles—layered feedback for combat satisfaction, companion-delivered mythology, and focused scope decisions—translate across budget levels.*