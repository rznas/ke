# How Celeste's 6-person team built a Game of the Year contender

**A 2.5-year development cycle by just seven core people produced one of the most critically acclaimed platformers ever made.** Celeste achieved a 97% positive rating on Steam from 132,000+ reviews, won Best Independent Game at The Game Awards 2018, and has sold **1.7 million copies** as of early 2025—all without a disclosed budget or AAA resources. The game's success offers a masterclass in scope management, technical precision, and player-centric design that a 2-person team developing Shahnameh can directly apply.

The critical insight for small teams: Celeste's polish came not from resources but from **ruthless mechanical minimalism** (just four actions: move, jump, dash, climb) combined with **hidden forgiveness systems** that make the game feel responsive without players understanding why. This "kind difficulty" philosophy—being punishing yet fair—created a game that resonated with both speedrunners and casual players struggling with its mental health themes.

---

## The core team achieved AAA polish through radical constraints

Celeste was built by **7 core contributors** working remotely across Vancouver, Toronto, Montréal, and São Paulo:

| Role | Person | Key Contribution |
|------|--------|------------------|
| Director/Designer | Maddy Thorson | Level design, story, code |
| Lead Programmer | Noel Berry | Engine, tools, physics |
| Pixel Artist | Pedro Medeiros (Saint11) | All in-game sprites |
| Character Artist | Amora Bettany | Character designs, portraits |
| Composer | Lena Raine | 2+ hour original soundtrack |
| Sound Design | Kevin Regamey (Power Up Audio) | SFX, audio integration |
| Operations | Heidy Motta | Business operations |

**Development timeline:** The game began as a 4-day PICO-8 game jam prototype in August 2015. Full production started January 2016 and shipped January 25, 2018—roughly **2.5 years total**. The team experienced crunch in final months, which Thorson later reflected was "a form of self-harm" during anxiety management.

**No public budget was disclosed**, but the project was described as "modest for indie projects." The game's financial success enabled the free Chapter 9: Farewell DLC (September 2019), which added 100+ new levels.

---

## Technical stack prioritized control over convenience

The team built custom technology rather than adopting existing engines, which proved essential for the precision platforming Celeste required.

**Core stack:**
- **Language:** C# for all game code
- **Framework:** XNA (deprecated Microsoft framework), ported via FNA and MonoGame
- **Custom framework:** Monocle—a Scene→Entity→Component architecture handling collisions, animation, and game logic
- **Level editor:** Ogmo Editor v3 (custom-built)
- **Art tools:** Aseprite (pixel art/animation), Clip Studio (concept art)
- **Audio:** FMOD Studio for sound management; Ableton Live for music composition

**Why custom physics mattered:** The team explicitly rejected pre-existing physics engines to "predetermine outcomes for certain situations." All colliders use axis-aligned bounding boxes with **integer-based positions**—no fractional pixels. Movement happens one pixel at a time with collision checks, ensuring pixel-perfect precision.

**Collaboration tools for remote work:** Slack for communication, Trello for bug tracking, Google Docs for shared design documents. This lightweight stack enabled effective distributed development across four cities.

---

## Ten hidden mechanics make difficulty feel fair

Celeste's renowned "game feel" comes from **systematic player forgiveness**—invisible mechanics that widen timing windows without players realizing. Maddy Thorson publicly documented these techniques:

**Coyote Time (5 frames):** Players can jump for 5 frames after walking off a ledge—named after Wile E. Coyote hovering before falling. This prevents frustrating "I pressed jump!" deaths.

**Input Buffering (5 frames):** Jump inputs are remembered for 5 frames before landing. Press slightly early, and Madeline jumps the exact frame she touches ground.

**Jump Corner Correction (4 pixels):** Bonking your head on a corner automatically wiggles you around it rather than stopping momentum dead.

**Wide Wall-Jump Window (2-5 pixels):** Wall jumps work from 2 pixels away; super wall-jumps from 5 pixels away—over half a tile in a 320×180 resolution game.

**Halved-Gravity Jump Peak:** Holding the jump button halves gravity at apex, giving more airtime for positioning adjustments.

Additional forgiveness includes dash corner correction (clips pop you onto ledges), lift momentum storage (jumping off moving platforms adds their velocity), and stamina refunds (converting climb jumps to wall jumps retroactively).

> "All are centered around widening timing/positioning windows, so that everything is fudged a tiny bit in the player's favor. I think this is a big reason why Celeste can feel kind even though it's very difficult—it wants you to succeed." —Maddy Thorson

---

## Level design follows a teach-escalate-combine pattern

Each of Celeste's **700+ hand-crafted screens** follows a pedagogical structure that trains players without explicit tutorials.

**The teaching framework:**
1. **Safe introduction:** New mechanics appear where death is unlikely
2. **First challenge:** Mechanic combined with simple obstacles
3. **Escalation:** Increasing complexity through the chapter
4. **Mastery test:** End-of-chapter sequences combining all elements

Each chapter introduces **3-6 new mechanics**, ensuring constant novelty without overwhelming players. This structure mirrors story beats—mechanical mastery reflects Madeline's emotional growth.

**Speedrunner consideration proved crucial:** The team designed "multiple valid solutions" for most screens, allowing creative play while maintaining challenge. Advanced techniques like hyperdashes and wavedashes were intentionally accommodated—sometimes discovered by speedrunners, then formally implemented. Rather than patching exploits, EXOK discussed with the speedrunning community to add quality-of-life features.

**Death and respawn design eliminates frustration:** No lives, no loading screens, instant respawn at screen start. Death becomes iteration rather than punishment. The death counter displayed at chapter end acknowledges struggle without mocking it.

---

## User reception reveals what players genuinely value

**Steam metrics show exceptional retention:** 97% positive from 132,000+ reviews with **54.87%** of players completing the main story (Summit achievement)—remarkable for a challenging platformer. The steepest drop-off occurs at Chapter 3 (74% → 64%), a known frustration point.

**Most praised elements across reviews:**
- Controls described as "the tightest, most responsive of any platformer"
- Level design that "builds on previous screens in creative ways"
- Soundtrack praised for motivating players through difficult sections
- Story's authentic portrayal of anxiety and depression
- Fair difficulty—"hard but never feels unfair"

**Common criticisms to learn from:**
- Wind mechanics in Chapter 4 (almost universally disliked)
- Maze-like level structure in Chapter 5 (players get lost)
- Chase sequences while carrying objects (Chapter 6)
- Chapter 3's length feels excessive to many players
- Keyboard controls problematic (diagonal dash misinputs)

**The Assist Mode decision proved prescient:** Offering granular options (game speed 50-100%, infinite stamina, infinite dashes, invincibility, chapter skip) without locking achievements received overwhelming praise. The framing evolved from calling it "essential" difficulty to "intended" experience based on accessibility advocate feedback.

---

## Key video resources with timestamps for deeper learning

### GDC 2017: Level Design Workshop - Designing Celeste
**URL:** https://www.youtube.com/watch?v=4RlpMhBKNr0  
**Duration:** ~28 minutes  
**Speaker:** Maddy Thorson

Covers the complete level design process for 300+ stages, including area map arrangement, story integration through environment, and balancing challenge with accessibility. Essential viewing for understanding iterative level design workflow.

### Game Maker's Toolkit: Why Does Celeste Feel So Good to Play?
**URL:** https://www.youtube.com/watch?v=yorTG9at90g  
**Duration:** ~17 minutes

**Key timestamps:**
- **01:28** – Movement acceleration analysis (why Celeste feels snappier than Mario)
- **03:08** – Jump curve mechanics and variable height
- **05:14** – How Celeste was coded (technical implementation)
- **08:40** – Art and animation juice (sprite stretching techniques)
- **09:27** – Player forgiveness systems (coyote time, input buffering breakdown)
- **13:20** – Level design philosophy

Includes direct Skype interviews with Thorson and Berry. References the open-sourced player code on GitHub.

### Developer Commentary Livestream
**URL:** https://www.youtube.com/watch?v=u-nSjhIgmXc  
**Duration:** Extended playthrough

Real-time design decision explanations from Maddy Thorson, covering level-by-level choices and behind-the-scenes development stories.

**Additional technical resource:** Mix and Jam's Celeste movement recreation in Unity (https://www.youtube.com/watch?v=STyY26a_dPY) demonstrates practical implementation.

---

## What a 2-person team can realistically adopt for Shahnameh

### Directly applicable patterns

**Minimal moveset, maximum depth:** Celeste uses just four actions. For an action-adventure, consider constraining to 3-5 core verbs and making them feel exceptional rather than adding more.

**Hidden forgiveness systems:** Implement coyote time, input buffering, and corner correction for any action mechanics. These are low-cost, high-impact improvements that require minimal assets.

**Instant feedback loops:** Whatever your death/failure state, make recovery instantaneous. Celeste's per-screen checkpointing could translate to generous checkpoint placement in action-adventure levels.

**Teach through level design:** Introduce each mechanic in a safe space before testing it. This reduces tutorial development burden while improving player experience.

**Assist Mode philosophy:** Plan granular accessibility options from the start. Celeste's team implemented Assist Mode in "a couple of days" near launch—but early architectural decisions enabled this.

### What requires larger teams/budgets

**700+ handcrafted screens:** The content volume isn't achievable with 2 people. Episodic structure is the right approach—deliver quality over quantity.

**2+ hour original orchestral soundtrack:** Lena Raine's work is exceptional. Consider licensed music, AI-assisted composition, or smaller scope soundtrack.

**Multi-year full-time development:** Celeste took 2.5 years with 7 people working full-time near the end. Realistic scoping for 2-person teams means smaller episodes.

### AI-assisted development opportunities

Where AI tools could accelerate Celeste-style quality for Shahnameh:

- **Pixel art iteration:** AI can generate sprite variations for rapid prototyping before manual refinement
- **Level layout generation:** AI assistance for initial room layouts, then human curation
- **Playtesting analysis:** Automated difficulty curve analysis from playtest data
- **Localization:** Story text translation assistance
- **Sound design:** AI-generated ambient audio and effect variations
- **Code assistance:** Physics implementation, edge case handling

### Scope management lessons

Celeste's original timeline was 6 months—it took 2.5 years. The team's key decisions:

1. **Start with proven mechanics:** The PICO-8 prototype validated core gameplay before full production
2. **Cut mechanics that don't serve the vision:** Story scope expanded, but mechanical scope stayed tight
3. **One exceptional thing per chapter:** Each chapter has a distinct identity rather than everything everywhere
4. **Post-release content:** Chapter 9 came 20 months after launch, funded by success

For Shahnameh's episodic structure: validate core combat/traversal feel in Episode 1, then expand in subsequent episodes based on what resonates with players.

---

## Conclusion: The Celeste blueprint for small team excellence

Celeste demonstrates that **polish comes from depth, not breadth**. Seven people created a Game of the Year contender by constraining scope to four mechanics, implementing systematic forgiveness, and letting personal authenticity drive narrative. The game's 97% positive rating across 132,000+ reviews proves players respond to genuine craft over feature lists.

For Shahnameh's 2-person team, the actionable takeaways are: ruthlessly limit your core mechanics but make them feel perfect; implement hidden forgiveness systems from the start; design levels that teach without tutorials; plan for accessibility architecturally; and let your Persian mythology setting carry narrative weight while gameplay carries emotional resonance. AI tools can accelerate iteration cycles that Celeste achieved through sheer hours—use them to prototype faster, not to expand scope beyond what you can polish.

The most transferable insight is philosophical: Celeste's difficulty works because it wants players to succeed. Whatever challenges Shahnameh presents, build the systems that help players overcome them—then they'll feel the triumph is earned.