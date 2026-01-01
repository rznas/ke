# Sekiro competitive analysis: What a 2-person team can learn from a 230-developer masterpiece

FromSoftware's Sekiro: Shadows Die Twice represents the pinnacle of focused action game design—built by approximately **200-230 developers over 3.5 years** with an undisclosed AAA budget. The game sold **10+ million copies** and won Game of the Year 2019, yet its most valuable lessons for Shahnameh: Legends of Persia aren't about replicating scale but understanding the design principles that made focused scope succeed spectacularly.

The core insight: Sekiro succeeded by **cutting features relentlessly** (no multiplayer, no builds, one weapon, one fixed character) to polish a single combat loop to perfection. This philosophy of intentional constraint is directly applicable to a 2-person AI-assisted team—you have forced constraints, but Sekiro proves constraints can become strengths.

---

## Development realities: A AAA benchmark with unexpected lessons

**Confirmed development facts:**
- **Team size**: ~200-230 at peak (estimated from producer Yasunori Ogura's statements about comparable FromSoftware projects)
- **Timeline**: Late 2015 to March 2019 (~3.5 years)
- **Budget**: Never publicly disclosed—FromSoftware maintains secrecy
- **Sales**: 10+ million units as of September 2023 (official KADOKAWA/FromSoftware press release)
- **Metacritic**: 91 (Xbox), 90 (PS4), 88 (PC)
- **Engine**: Custom proprietary engine (internally evolved since Demon's Souls, NOT PhyreEngine as often misreported)

**What FromSoftware cut to focus development:**
The "corners cut" reveal their priorities. They eliminated: character creation, armor variety, weapon variety (one katana only), stat-based leveling, magic systems, and multiplayer. Producer Robert Conkey explained: *"When you make a multiplayer game there are certain restrictions... you have to design bosses for two players, whether they're spellcasters or knights. This puts a limitation on how you can design bosses."*

Removing multiplayer enabled: pause functionality (a first for FromSoft), bosses tuned for single-player only, no network code overhead, and more creative level design freedom.

**Relevance to Shahnameh**: Your 2-person constraints mirror Sekiro's intentional cuts. The game proves that a single weapon, fixed protagonist, and no multiplayer can yield Game of the Year—these aren't limitations to apologize for but opportunities for polish.

---

## The posture system: Technically feasible for a small team

Sekiro's deflection/posture system is mechanically simpler than it appears, making it potentially adaptable with AI-assisted development.

**Core mechanics breakdown:**
- **Deflect window**: 12 frames (~0.2 seconds) for perfect deflection; degrades to 4-0 frames if spam-pressing
- **Posture meter**: Fills when taking/blocking damage; breaks when full, enabling a killing blow
- **HP-posture relationship**: Lower enemy HP = slower posture recovery (bar changes color from normal → orange → red)
- **Perfect deflect vs block**: Deflects damage enemy posture while taking minimal player posture; blocking does opposite
- **Recovery**: Player recovery accelerates when holding guard; enemies recover immediately when not being attacked

**Why this is achievable for 2 people:**

The posture system is fundamentally **deterministic and rule-based**—every enemy move has a specific counter, and rules never break. This makes it implementable through clear state machines:

1. **Input detection** (12-frame window for deflect)
2. **Meter management** (two values: HP and posture per entity)
3. **State-based recovery** (idle = recover; attacking/blocking = no recovery)
4. **HP threshold modifiers** (posture recovery rate tied to HP percentage)

Game design analyst Josh Bycer noted: *"Sekiro is not an action game, but a Kaizo game"*—meaning highly pattern-based and learnable. Pattern recognition systems are well-suited to AI-assisted development since enemy behaviors can be designed as finite state machines with clear transitions.

**What would require larger teams:**
- The **animation quality** (kendo-referenced sword animations requiring experienced animators)
- **40+ unique enemy types** with distinct movesets
- **Boss phase transitions** with multiple attack pattern libraries

**Realistic adaptation for Shahnameh**: Implement posture on 3-5 enemy types rather than 40+. AI tools can help generate enemy behavior trees, but animation work remains the bottleneck. Consider procedural animation blending or motion-matching systems that require less manual keyframing.

---

## Boss design patterns: Achievable frameworks for episodic scope

Sekiro contains **12-14 main bosses and 40+ mini-bosses** across ~30-34 hours. For a 6-9 hour episodic game, you need far fewer, but the design patterns scale down.

**Genichiro Ashina: The skill-check template**
This boss is specifically designed to ensure players master all core mechanics:
- Phase 1-2: Standard sword combat with 7-hit Floating Passage combo
- Phase 3 (Way of Tomoe): Introduces lightning, teaching Lightning Reversal
- Punishes healing attempts with ranged attack
- Mixes all three perilous attack types (thrust, sweep, grab)

The community consensus: *"He is the first boss that demands all sorts of reactions and deflections—regular, thrust, sweep, grab, air—while also punishing heals."*

**The Perilous Attack system (implementable):**
All bosses use three unblockable attack types with consistent visual/audio signaling:
1. **Thrust**: Counter with step-dodge forward (Mikiri Counter)
2. **Sweep**: Counter with jump + kick
3. **Grab**: Must dodge; cannot block

This creates a **rock-paper-scissors readability** that's relatively simple to implement: red kanji flash + unique sound → player identifies type → executes counter. The system works because rules are **absolute**—never broken across the entire game.

**Isshin, the Sword Saint: Phase progression model**
The final boss demonstrates escalating complexity:
- Phase 0: Genichiro (warm-up)
- Phase 1: Pure sword (Ashina Cross, Ichimonji Double)
- Phase 2: Adds spear + pistol (most difficult)
- Phase 3: Adds lightning (paradoxically easier—Lightning Reversal deals massive damage)

The design insight: **Later phases can be easier if they introduce player-advantage mechanics.** Phase 3's lightning is actually a gift to the player, creating emotional arc where relief follows the hardest phase.

**Achievable boss count for 6-9 hour episode**: 2-3 main bosses, 5-8 mini-bosses. Focus on one "skill check" boss (like Genichiro) that ensures players master your core combat loop before proceeding.

---

## Mythological adaptation: FromSoftware's approach transfers directly to Persian content

Miyazaki's philosophy on historical/mythological settings provides a template for handling the Shahnameh.

**"Starting point, not constraint"**
Direct quote from Miyazaki (Famitsu): *"Though Sekiro is set at the end of the Sengoku era, this is only a point of reference for the atmosphere, or a starting point, and ultimately the world greatly deviates from there."*

This freed FromSoftware to include entirely fictional clans, supernatural immortality systems, and yokai—while maintaining authentic atmosphere. The Ashina clan is inspired by real history but heavily fictionalized.

**Era selection for mood**
Miyazaki chose Sengoku over Edo because: *"The Sengoku period was dirtier—it was grittier and bloodier. It had more of a feel of the type of world we'd want to create... The Sengoku era, being the middle ages, is a time when old, mysterious things might have still remained, hiding in the corners of the world."*

**For Shahnameh**: Select a Persian era (likely pre-Islamic Persia) for similar reasons—it allows mythological creatures and legendary kings without historical constraint. The Achaemenid or Sassanid periods offer "medieval" grounding where Simurghs and divs can plausibly exist.

**How mythology serves gameplay in Sekiro:**
- **Centipedes**: Grant corrupted immortality to monks (explains respawning enemies + horror imagery)
- **Dragon's Heritage**: Justifies resurrection mechanic
- **Divine Dragon**: Korean/Chinese dragon design explains its "foreignness" in Japanese setting
- **Sokushinbutsu** (self-mummification): Real Buddhist practice twisted into horror

**Persian mythology opportunities:**
- **Farr (divine glory)**: Could justify a power/meter system—heroes possess farr, losing it through immoral actions
- **Divs**: Demon bosses with distinct designs based on classical descriptions
- **Simurgh**: Healing/wisdom source (like the Divine Dragon's origin)
- **Zoroastrian dualism**: Morality system affecting gameplay/endings (Asha vs. Druj—truth vs. lie)

**Localization warning**: FromSoftware let Activision handle English translation independently, creating problems. "Sakura Dragon" became "Divine Dragon," losing cherry blossom symbolism. "Maboroshi O-Chou" (Phantom Butterfly) became simply "Lady Butterfly." Japanese players noticed lost nuances; Western players didn't know what they missed. **Keep localization close to the creative team for culturally-dense content.**

---

## User reception data: What players actually love and hate

**Steam reception**: 95% positive (336,580 reviews)—"Overwhelmingly Positive"

**Top 5 praised aspects:**
1. **The deflection combat system**: *"One of, if not the best parry system"*; described as "rhythm game" combat creating a dance of steel
2. **Sense of mastery**: *"This game changed the way I play video games. I went from a guy that didn't like to be challenged to embrace the challenge and love it"*
3. **Boss fights** (especially Isshin): *"The best final boss in any FromSoftware game"*
4. **Japanese atmosphere**: Originality versus typical dark fantasy praised
5. **Focused, streamlined design**: *"Gets rid of things like leveling your stats or managing tons of equipment"*

**Top 5 criticized aspects:**
1. **No build variety**: *"No weapon variation, boring rewards... There isn't anything like builds"*
2. **No multiplayer/co-op**: Removes summoning help option
3. **Camera issues**: *"Every time you died and it wasn't because the camera f***ed you over, you hesitated"*
4. **Limited replayability**: *"Every run of Sekiro is the same"*
5. **Steep learning curve**: *"I had to unlearn so many ingrained instincts"*—Souls veterans struggled most

**The accessibility debate and FromSoftware's response:**
The "easy mode" controversy generated significant media coverage. Miyazaki's official position (GameSpot, 2018): *"We don't want to include a difficulty selection because we want to bring everyone to the same level of discussion... We feel if there's different difficulties, that's going to segment and fragment the user base."*

However, Sekiro includes **hidden difficulty modifiers**: Kuro's Charm removal adds 30% chip damage through blocks; Demon Bell adds ~50% to enemy stats. This provides hardcore options without visible "easy mode."

**Meme culture impact:**
- **"Hesitation is defeat"**: 3.9M+ TikTok posts; became life advice beyond gaming
- **"MY NAME IS GYOUBU MASATAKA ONIWA!"**: Over-the-top boss introduction became beloved meme
- The death screen's red kanji became instantly recognizable

**Relevance to Shahnameh**: The criticism about "no build variety" is actually praise in disguise—players who loved Sekiro loved its focus. Your single-protagonist, episodic structure aligns with what worked. Consider hiding difficulty options (modifiers that unlock after completion) rather than explicit easy/hard modes.

---

## YouTube resources for developers: Specific timestamps and insights

**1. Did You Know Gaming - Sekiro Development**
- **URL**: Search "Did You Know Gaming Sekiro" on YouTube
- **Length**: ~15-20 minutes
- **Key insights**: Evolution from potential Tenchu sequel; how grappling hook inspired vertical level design; cut content including Dark Souls-style message system; tutorial design decisions

**2. Game Informer - Interview with Lead Designer Masaru Yamamura**
- **Source**: gameinformer.com/video-feature/2019/01/15/exclusive-gameplay-and-details-on-creating-sekiro
- **Key developer quote**: *"We have to restrict ourselves, and how far we can take that balance and that tuning, in order to cater to all these playstyles"*—explaining how removing builds allowed deeper combat polish
- **Topics**: Boss design philosophy, prosthetic tools as boss counters, inspiration from Tenchu

**3. Game Wisdom / Josh Bycer - Combat Analysis**
- **Channel**: Game Wisdom
- **Associated article**: gamedeveloper.com/design/how-i-broke-sekiro-shadows-die-twice
- **Key insights**: Posture degradation slows at 75% HP, nearly stops below 50% HP; three enemy type analysis (grunts, humanoid bosses, non-humanoid bosses); prosthetic tools as difficulty modulation
- **Critical perspective**: Argues combat is "broken" in ways that reveal design trade-offs—valuable for understanding what NOT to do

**4. Guardian Ape Boss Design Analysis**
- **Analyst**: Jason de Heras (jasondeheras.com)
- **Key design elements documented**:
  - Hit armor: Allows enemy to absorb hits without interruption
  - Setup attacks: Fart forces player backward, creating space for poo throw
  - Evasive attacks: Ape's evade IS an attack with fast startup
  - Hit threshold progression: Enough attacks → stagger → continue → huge reaction + escape

**5. SUPERJUMP Magazine - Art & Science of Sekiro's Combat**
- **Written source**: medium.com/super-jump/the-art-science-of-sekiros-combat-d39baebc2d56
- **Key concepts**: Deterministic design ("all enemy moves are telegraphed; to every action there's a specific counter"); tutorial design through combat; mini-bosses as skill checkpoints

**Notable absence**: No official FromSoftware GDC talk on Sekiro was found in public archives—their design insights come primarily through interviews rather than postmortems.

---

## Technical performance: Baseline expectations and optimizations

**Frame rate targets:**
- Console (base): 30fps with frame-pacing issues
- Console (enhanced): Uncapped ~38-48fps (PS4 Pro)
- PC: 60fps cap (moddable to 144fps)

Digital Foundry called the PC port "technically competent in almost every respect"—potentially their lead development platform.

**System requirements (Recommended):**
- CPU: Intel Core i5-2500K / AMD Ryzen 5 1400
- GPU: NVIDIA GTX 970 / AMD RX 570
- RAM: 8 GB
- Storage: 25 GB

**Asset reuse strategies:**
FromSoftware's proprietary engine has evolved since Demon's Souls (2009). Modding community analysis confirms: DS3 and Sekiro share similar file structures; same extraction tools work across DS1, DS3, Bloodborne, and Sekiro. Visual improvements over DS3 were "evolutionary rather than revolutionary."

**Relevance to Shahnameh**: Target 60fps on mid-range hardware. Sekiro proves modern players expect smooth performance in action games. For a 2-person team, using established engines (Unity/Unreal) with asset store resources is more practical than custom engine development—but study Sekiro's optimization as a benchmark for what players expect.

---

## Scope analysis: What a 6-9 hour episode needs versus 30+ hour AAA

**Sekiro content density:**
| Metric | Sekiro | Suggested for Episode 1 |
|--------|--------|------------------------|
| Main story | 30-34 hours | 6-9 hours |
| Main bosses | 12-14 | 2-3 |
| Mini-bosses | 40+ | 5-8 |
| Major areas | 10-12 | 2-3 |
| Prosthetic tools | 10 base | 3-4 base |
| Enemy types | 40+ | 8-12 |
| Endings | 4 | 1-2 |

**Sekiro's "smart decisions that maximized impact":**
1. **One weapon, perfected**: The Kusabimaru katana enabled animation polish impossible with weapon variety
2. **Fixed protagonist**: Wolf's defined character allowed precise combat tuning
3. **Vertical exploration over horizontal sprawl**: Grappling hook created 3D space without larger maps
4. **Resurrection as pacing tool**: Miyazaki: *"The resurrection system was not introduced to make the game easier. It actually can make the game harder because it allows us to push the edge of risky combat."*
5. **Boss reuse via phases**: Rather than many distinct bosses, phases transform existing ones

**What could be cut for smaller scope:**
- Multiple endings (focus on one strong narrative)
- Extensive skill trees (provide 5-10 skills instead of 30+)
- Prosthetic tool upgrade trees (keep tools simple, one version each)
- Hub area complexity (minimal NPC systems)
- Optional bosses (every boss can be required)

---

## Feasibility assessment for 2-person AI-assisted team

**ACHIEVABLE with AI assistance:**

| System | Feasibility | Notes |
|--------|-------------|-------|
| Posture/deflection combat | ✅ High | Rule-based, deterministic—suits state machines |
| Perilous attack system | ✅ High | Three attack types with visual/audio cues |
| 2-3 phase bosses | ✅ Medium-High | Requires animation investment but pattern design is achievable |
| Persian mythology integration | ✅ High | Narrative design scales independent of team size |
| Environmental storytelling | ✅ High | Leverages art assets rather than systems programming |
| One weapon, fixed protagonist | ✅ Required | Your constraints match Sekiro's intentional cuts |

**CHALLENGING but possible:**

| System | Feasibility | Notes |
|--------|-------------|-------|
| 12-frame deflect precision | ⚠️ Medium | Requires tight input handling and polish |
| Animation quality | ⚠️ Medium | AI animation tools emerging; consider procedural techniques |
| 8-12 distinct enemy types | ⚠️ Medium | AI can help generate behavior trees; art is bottleneck |
| Stealth integration | ⚠️ Medium | Basic detection cones achievable; full system complex |

**OUT OF SCOPE:**

| System | Reason |
|--------|--------|
| 40+ enemy types | Animation/design time impossible for 2 people |
| 4 endings with branching | Exponential content multiplication |
| Vertical grappling exploration | Level design complexity too high |
| 30+ hour runtime | Content volume requires team |
| Full prosthetic tool system | 10 tools with upgrade trees = too much balance work |

---

## Actionable recommendations for Shahnameh: Legends of Persia

**Combat system approach:**
1. Implement **posture-like stamina system** with simpler parameters—start with 3-second deflect windows, tighten through playtesting
2. Use **three unblockable attack types** (Persian equivalents of thrust/sweep/grab) with consistent visual language
3. Design **one "skill check" boss** per episode that ensures core combat mastery
4. Consider boss **phase additions** rather than entirely new bosses to stretch content

**Mythological integration:**
1. Use Shahnameh as **"starting point, not constraint"**—creative liberty is expected
2. Design **one core theme** (farr/divine glory or Zoroastrian dualism) that explains game mechanics
3. Let mythological creatures justify gameplay systems (divs for enemy variety, Simurgh for healing/save points)
4. Plan localization from the start—Persian names should survive translation

**Scope management:**
1. Target **6-9 hours** with 2-3 bosses, 5-8 mini-bosses, 2-3 areas
2. Cut multiplayer, build variety, weapon variety—Sekiro proves these cuts enable polish
3. Consider **hidden difficulty modifiers** (unlock after completion) rather than easy mode
4. One strong ending per episode; save branching for later episodes

**Technical priorities:**
1. Target **60fps on mid-range hardware**—non-negotiable for action games
2. Use **established engines** (Unity/Unreal) rather than custom solutions
3. Invest in **animation quality** over quantity—fewer enemy types, better animations
4. Implement **deterministic combat rules**—consistency builds player trust

**AI-assisted development opportunities:**
1. **Enemy behavior trees**: Pattern-based AI suits generative tools
2. **Dialogue/item descriptions**: AI can draft, humans refine
3. **Level layout iteration**: AI can generate variations for testing
4. **Balancing**: AI can simulate combat for tuning posture values

---

## Conclusion: Constraint as competitive advantage

Sekiro's greatest lesson isn't its 230-person team or AAA budget—it's that **intentional constraint enables excellence**. By cutting multiplayer, builds, and weapon variety, FromSoftware polished a single combat loop until it won Game of the Year. Your 2-person team with AI tools faces similar constraints by necessity rather than choice, but the outcome can be the same: a focused, polished experience that respects players' time.

The posture system, perilous attacks, and boss phase design are all technically achievable at smaller scale. Persian mythology offers material as rich as Sengoku Japan—the key is Miyazaki's philosophy of using history as "starting point, not constraint." 

Focus Episode 1 on **nailing deflection combat and one unforgettable boss**. If players feel the rhythm-game satisfaction of steel-on-steel combat that Sekiro pioneered, everything else follows. As Isshin says: *"Hesitation is defeat."* Ship the focused vision rather than the ambitious compromise.