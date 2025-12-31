# Shahnameh: Legends of Persia — Game Benchmarking Guide

A 2-person team using AI tools and free software can absolutely create a commercially successful action-adventure game. This research identifies **67 games** across 10 categories, prioritized by relevance to your specific constraints: small team, Dark Souls-inspired combat, episodic release, Persian mythology, and stylized art direction using Stable Diffusion and Blender.

**The clearest path forward**: Study Salt and Sanctuary (2-person team, Souls-like), Hollow Knight (3 people, $57K budget, 15M+ sales), and Hades (20 people, mythology adaptation, exceptional combat feel). Prince of Persia: The Lost Crown represents the gold standard for authentic Persian representation — despite commercial underperformance, its cultural approach should inform your visual and narrative direction.

---

## Executive summary: Priority distribution

| Tier | Games | Focus Areas | Study Order |
|------|-------|-------------|-------------|
| **TIER 1** | 15 games | Immediate study required | Weeks 1-4 |
| **TIER 2** | 20 games | Important reference points | Weeks 5-8 |
| **TIER 3** | 32 games | Comprehensive coverage | As needed |

**Critical insight from the research**: The episodic model has largely been abandoned by the industry (Hitman, Life is Strange, Telltale all switched to full releases). Your **$19.99 + $19.99 + $24.99** pricing is aggressive — consider Episode 1 free/discounted or very short gaps between episodes (2-4 weeks maximum) to prevent the 50% sales drop-off that killed most episodic games.

---

## TIER 1: Immediate study (15 games)

These games have the richest documentation and highest relevance to your specific project.

### Small team combat references (CRITICAL)

**Salt and Sanctuary** — Ska Studios (2 people)
- Development: 2.5 years, self-funded
- Souls-like 2D combat by husband-wife team James and Michelle Silva
- **600+ weapons, armor, spells** created by just 2 people
- Engine: MonoGame (XNA successor)
- **GDC 2017 postmortem available** on YouTube
- *Why study first*: Exact team size match, same genre, proven viable

**Hollow Knight** — Team Cherry (3 people)
- Budget: AU$57,000 Kickstarter + personal savings
- Development: 4 years (started as Ludum Dare jam project)
- Sales: **15+ million copies**, estimated $30+ million revenue
- Engine: Unity (switched from Stencyl)
- Key technique: Hand-drawn Photoshop assets, PNG exports, 4 free DLC packs built massive goodwill
- *Why study*: Proves 3 people can create world-class Metroidvania; combat feel highly refined

**Hades** — Supergiant Games (~20 people)
- Development: 3 years with 2-year Early Access period
- Sales: 1+ million copies shortly after launch, multiple GOTY awards
- **40-50% of final features came from Early Access feedback**
- Greek mythology adaptation balances authenticity with creative freedom
- Combat combines roguelike loops with satisfying melee
- *Why study*: Mythology adaptation approach, small-team polish, combat responsiveness

**Dead Cells** — Motion Twin (8-10 people)
- Worker cooperative model — equal salary and decision-making
- Sales: **10 million copies** (9 million came after Evil Empire spinoff continued development)
- Development: 2 years with Early Access
- 40-50% features from player feedback
- *Why study*: Cooperative structure, Early Access iteration model, tight melee combat

**Sifu** — Sloclap (~50 people)
- Sales: 4+ million copies
- Real martial arts choreographer (Benjamin Colussi, actual Pak Mei Sifu)
- Motion capture with authentic Kung Fu techniques
- 12 free content updates post-launch
- *Why study*: Authentic martial arts integration, melee combat weight and feel

### Persian/Middle Eastern references (CRITICAL)

**Prince of Persia: The Lost Crown** (2024) — Ubisoft Montpellier
- Development: ~3.5 years
- **First Prince of Persia dubbed into Farsi**
- Composers include Mentrix (Samar Rad) — Iranian-born, uses traditional Persian instruments (tanbur, daf, oud)
- Explicitly moved away from Orientalism toward actual Persian/Zoroastrian mythology
- Features: Simurgh, Manticore (Persian origin), Azhdaha, Kaveh the Blacksmith, Mount Qaf, Immortals, Faravahar symbol, Towers of Silence
- Jordan Mechner: "The Prince of Persia game I've been wishing for"
- **Critical lesson**: Despite 86-87 Metacritic and 1M+ sales, failed to meet expectations; team disbanded
- *Why study*: Gold standard for authentic Persian representation; learn from both successes and commercial challenges

**Assassin's Creed Mirage** (2023) — Ubisoft Bordeaux
- Setting: 9th-century Baghdad (Islamic Golden Age)
- Consulting team included Dr. Raphaël Weyland, Dr. Glaire Anderson (Islamic art/architecture), Dr. Ali Olomi
- **First AC with full Arabic localization globally**
- Major challenge: 9th-century Baghdad is a "lost city" — completely destroyed by Mongols, no archaeology exists
- History of Baghdad codex with 66 entries, museum artifact images
- *Why study*: Unprecedented historical research methodology; how to reconstruct "lost" historical settings

**Prince of Persia: The Sands of Time** (2003) — Ubisoft Montreal
- Team: Started with 7, peaked at **65 staff**
- Sales: 14 million copies (as of 2014)
- Research: Team read One Thousand and One Nights; Jordan Mechner drew from Shahnameh
- Architecture based on 9th-12th century Persia
- *Why study*: Foundational Persian game aesthetic; GDC postmortem available from producer Yannis Mallat

### Combat system masters

**Sekiro: Shadows Die Twice** — FromSoftware (~200-230 at peak)
- Revolutionary posture system replaces HP-focused combat
- Lead Designer Masaru Yamamura: "Departing from Dark Souls — created deflect system from scratch"
- Failed deflects become blocks (generous timing = accessibility without trivializing)
- Three attack types (normal, thrust, sweep) each require specific counter
- *Why study*: Most innovative modern melee combat system; every attack has deterministic counter

**Ghost of Tsushima** — Sucker Punch (~150-160 people)
- Budget: ~$60 million (remarkably low for scope)
- Sales: 13+ million copies
- Development: 6 years (multiple combat versions built and discarded)
- **GDC talks**: "Honoring the Blade: Lethality and Combat Balance" (Theodore Fishman), "Master of the Katana" (Chris Zimmerman)
- Blue/red glints system directly inspired by God of War's yellow/red rings
- "Six Blades of Kojiro" boss design: each teaches unique attack, final boss combines ALL previous moves
- *Why study*: Most detailed GDC documentation on samurai combat feel; boss design philosophy directly applicable

**Dark Souls** — FromSoftware (~195 people credits, DS1)
- Budget: Estimated $5-20 million (low for impact)
- Sales: 27+ million (series cumulative)
- Miyazaki's "image words" approach: abstract concepts drive visual design
- Core principles: Animation commitment (cannot cancel), stamina as core resource, enemies follow same rules as player
- *Why study*: Foundation of the genre you're entering; fairness and weight principles

### Budget champions

**Balatro** (2024) — LocalThunk (1 person)
- Budget: **~$100** (only expense: Fiverr music commission)
- Development: 2.5 years as side project
- Sales: **5+ million copies**; profitable within 1 HOUR of launch; $1 million gross in 8 hours
- Tools: Löve game framework + Lua (both FREE)
- *Why study*: Proves nearly zero-budget games can achieve massive success in 2024

**Undertale** (2015) — Toby Fox (1 person)
- Budget: ~$50,000 (Kickstarter)
- Development: 32 months
- Sales: 3.5+ million copies; estimated $126 million lifetime revenue
- Tools: GameMaker: Studio, MS Paint
- *Why study*: Solo dev mastery; subverting genre expectations

**Stardew Valley** (2016) — Eric Barone (1 person)
- Budget: Near $0 (lived on savings, girlfriend's support)
- Development: 4.5 years, 10-12 hours/day
- Sales: **41+ million copies**; estimated $300+ million revenue
- Tools: C#, MonoGame, Paint.NET (all free or nearly free)
- *Why study*: Ultimate solo dev success; proves quality trumps budget

### Cultural authenticity models

**Never Alone** — Upper One Games (Indigenous-owned)
- **40+ Alaska Native elders, storytellers, community members** contributed
- Game originated FROM the Indigenous community
- 26 unlockable "Cultural Insights" — documentary mini-films
- Revenue supports CITC programs for Alaska Native people
- 15+ million players; Peabody Award 2022
- *Why study*: Gold standard for cultural collaboration; "made WITH not ABOUT" approach

---

## TIER 2: Important reference points (20 games)

### Small team achievers

**Tunic** — Andrew Shouldice (primarily solo)
- Development: 7 years
- In-game manual as fundamental gameplay mechanic
- Iterative development: redesigned nearly every element "at least once or twice"
- Publisher: Finji
- *Why study*: Solo dev perseverance; discovery as core design pillar

**Celeste** — Matt Makes Games (~6 people)
- Development: 2.5 years (started as 4-day PICO-8 jam)
- Sales: 1+ million copies
- **Locked 60fps** for determinism — critical for precision platforming
- Engine: Custom C#/MonoGame
- *Why study*: Accessibility features (Assist Mode took "a couple days work"); mental health themes resonated

**Cuphead** — Studio MDHR (started 2-3, grew to ~25)
- Development: 7 years; founders remortgaged their homes
- **50,000+ hand-drawn frames**
- Tools: Unity, traditional paper/ink, $300 scanner from Best Buy
- Sales: 2+ million by end of 2017
- *Why study*: DICE 2018 talk on making game with no budget/experience; extreme art commitment

**Hyper Light Drifter** — Heart Machine (~4 core)
- Budget: $645,158 Kickstarter (from $27,000 goal)
- Engine: GameMaker Studio
- Lead developer's heart disease inspired game and studio name
- *Why study*: Personal story woven into game narrative; pixel impressionism art style

**Ori and the Blind Forest** — Moon Studios (10 core + contractors)
- Development: 4 years
- "Virtual studio" — distributed team across Austria, Australia, Israel, US
- Never rented office; recruited global talent via internet
- Profitable for Microsoft in 7 days
- *Why study*: Distributed team model; Microsoft partnership approach

**A Plague Tale: Innocence** — Asobo Studio (40 people)
- First original IP in 10 years after contract work
- Child actors participated in writing process
- Narrative-focused development inspired by Last of Us and Brothers
- *Why study*: Narrative-focused indie AA approach

### Episodic model references (cautionary tales)

**Telltale's The Walking Dead Season 1** (2012)
- Pricing: $5/episode, $25 season pass
- Sales: 8.5 million episodes in 7 months; ~$40 million revenue
- **Average revenue per user: $16** (below $25 full season)
- Release gaps: 6-8 weeks typical
- *Why study*: Peak episodic success; also shows why model became unsustainable

**Hitman (2016)** — IO Interactive
- Intro Pack: $15; Episodes: $10 each; Full: $60
- Release: 7 months (monthly episodes)
- Word-of-mouth improved over time; allowed iterative improvement
- **ABANDONED EPISODIC for Hitman 2** — "A lot of people were not so happy with that format"
- *Why study*: Most sophisticated episodic attempt; clear lessons on why it failed

**Bendy and the Ink Machine** — Joey Drew Studios (started 2 people)
- **Chapter 1: FREE** + $5.99 per subsequent chapter
- Developer refused season passes: "We don't believe in selling something that doesn't exist yet"
- 20 months total development (grew team to 6 by Chapter 3)
- *Why study*: Free first chapter model; small team episodic success

**Kentucky Route Zero** — Cardboard Computer (3 people)
- **7 years total** (planned for 1 year)
- Act 1 to Act 5: 2013 to 2020
- Critical success (Peabody Award) but extreme delays caused frustration
- *Why study*: Cautionary tale — small teams cannot sustain episodic schedules

### Mythology and art direction

**Okami** — Clover Studio
- Originally planned photorealistic 3D; PS2 couldn't handle it
- Character designer drew wolf with brush → inspired sumi-e pivot
- Art style led directly to Celestial Brush gameplay mechanic
- "Artistic style doesn't age at all" — based on centuries-old art forms
- *Why study*: Constraint-driven art innovation; Japanese mythology integration

**God of War (2018)** — Santa Monica Studio
- Director Cory Barlog: "Our interpretation of mythology, not history"
- Chose characters underrepresented in pop culture (Baldur vs. Thor/Loki)
- Studied gaps in source material for creative opportunities
- **GDC talks**: "Evolving Combat in God of War" (Mihir Sheth)
- *Why study*: AAA mythology adaptation philosophy; combat weight principles

**Raji: An Ancient Epic** — Nodding Heads Games (13 people)
- Indian mythology (Hindu/Balinese); art style based on Pahari paintings
- Nominated Best Debut Game at The Game Awards 2020
- **Controversy**: Criticized for implicit erasure of Muslim influence on Indian culture
- *Why study*: Small team mythology game; cultural representation pitfalls to avoid

**Mulaka** — Lienzo (small indie team)
- 2 years communicating with Tarahumara community before production
- Secured blessing from cultural governess
- Unlimited stamina mechanic honors Tarahumara legendary running
- Donates up to 10% to NGOs for Sierra Tarahumara
- *Why study*: Community-blessed cultural adaptation; revenue sharing model

**Return of the Obra Dinn** — Lucas Pope (1 person)
- Development: 4.5 years, solo
- 1-bit rendering (800×450 pixels) — constraint as feature
- "Low resolution leaves detail out — benefit as developer and player"
- *Why study*: Extreme constraint-driven art; mystery puzzle innovation

**Dead Cells** / **Hades** / **Hollow Knight** (see TIER 1) — combined represent best stylized 2D approaches

### Combat references (secondary)

**Devil May Cry 5** — Capcom
- Director Hideaki Itsuno: "Hit-stop displays animation frames longer" — key to impact feel
- Style ranking rewards variety, not just damage
- **GDC 2019 talk**: "Creating a Standout Action Game"
- *Why study*: Deep action game feel principles

**Elden Ring** — FromSoftware
- Guard counter, Spirit Ashes, Ashes of War — accessibility innovations
- "Heavy, high-tension combat with more options"
- Boss design: demigods as "heroic, mythological" climaxes
- *Why study*: Evolution of Souls formula with more player freedom

---

## TIER 3: Comprehensive coverage (32 games)

### Additional combat references
- **Assassin's Creed Origins/Mirage** — Parry window analysis; yellow/red visual indicators
- **Blasphemous** — The Game Kitchen (~5 initial, grew post-Kickstarter); Spanish Catholic imagery approach
- **Jotun** — Norse mythology, hand-drawn art, boss-focused design
- **Asura's Wrath** — Hindu/Buddhist mythology; cinematic action approach
- **Apotheon** — Greek mythology, 2D black-figure pottery art style

### Additional budget champions
- **Vampire Survivors** (2022) — Luca Galante (1 person); Phaser JS (FREE); ~£40M net worth now
- **Lethal Company** (2023) — Zeekerss (1 person, age 21); 10M+ copies; $119M gross
- **Content Warning** (2024) — 5 developers; 700K+ copies first week; 24-hour free launch viral
- **FTL: Faster Than Light** — Subset Games (2 people); $200K Kickstarter; 10M+ users
- **Into the Breach** — Subset Games (2-3 people); 5-year development
- **Terraria** — Re-Logic (started solo, now ~11); 58M+ copies; 4 months initial dev
- **Papers, Please** — Lucas Pope (solo); 5M+ units; Haxe + NME (FREE tools)
- **Cave Story** — Daisuke Amaya (solo); 5 years; hobby project, later commercialized
- **Shovel Knight** — Yacht Club (6 people initially); $1.4M budget (Treasure Trove: $9M total); 3M+ sales

### Additional cultural/mythology
- **Immortals Fenyx Rising** — Ubisoft's comedic Greek mythology take
- **Smite** — Multi-pantheon god representation
- **Aurion: Legacy of the Kori-Odan** — African mythology by Cameroonian studio
- **Aztez** — Aztec culture action game
- **Thymesia** — Dark medieval mythology approach

### Episodic/narrative
- **Life is Strange 1** (2015) — €6 million budget; 20M+ players; episodic success before abandoning model
- **Life is Strange: True Colors** (2021) — Abandoned episodic; "Can't imagine going back"
- **Resident Evil Revelations 2** — Weekly releases (unique approach); $5.99/episode
- **Tales from the Borderlands** — Internal failure despite critical success; 95% staff reassigned mid-season

### Art direction references
- **Persona 5** — Bold graphic style
- **Borderlands series** — Cel-shading
- **Gris** — Watercolor
- **Transistor** — Art nouveau/deco
- **Journey** — Minimalist
- **Sable** — Moebius-inspired
- **Disco Elysium** — Oil painting style

### Hardware optimization references
- **Any of the above 2D games** run on Switch/low-spec hardware
- Unity optimization: URP, baked lighting, sprite atlases, object pooling

### Persian-adjacent
- **Prince of Persia (2008 Reboot)** — Heavily based on Zoroastrianism; Ormazd vs. Ahriman; art direction nominated for awards despite criticism of "Anglicized" protagonist
- **Prince of Persia: Warrior Within/Two Thrones** — Tonal shift lessons (what NOT to do)
- **Original Prince of Persia (1989)** — Jordan Mechner's foundation; inspired by Shahnameh and Arabian Nights

### Existing Shahnameh games (limited, for reference)
- **Age of Heroes** (Iran) — 90+ Shahnameh figures; commissioned by Ferdowsi Foundation
- **Seven Quests** (in development) — Rostam as hero; by Iranian developers in Dubai
- **Quest of Persia series** (Iran) — Puya Arts; claims "100% Persian" vs Prince of Persia's Arab/Indian elements
- **Garshasp** (Iran) — Ultraviolent fantasy; Deev hunting

---

## Identified gaps in the research

**Persian/Shahnameh games are extremely rare.** Beyond Prince of Persia (which mixes Persian, Arab, and Indian elements) and a few Iranian-developed titles with limited international reach, no major game has directly adapted the Shahnameh epic. This represents both a **massive market opportunity** and a **risk** (unproven audience demand for specifically Persian mythology).

**Episodic success stories are nearly non-existent post-2020.** The model has been abandoned by almost every major practitioner. Your episodic approach is swimming against industry tide — consider alternatives or mitigations.

**Combat tutorials for 2-person teams are limited.** Most detailed combat design documentation comes from AAA studios (FromSoftware, Santa Monica, Sucker Punch). Salt and Sanctuary's GDC talk is the closest match to your constraints.

---

## Critical pricing and timing recommendations

Your proposed **$19.99 + $19.99 + $24.99 = $64.97 total** is unusually high for episodic:
- Telltale: $25 for 5 episodes ($5/episode)
- Life is Strange: $19.99 for 5 episodes ($4/episode)
- Hitman: ~$65 for 6 episodes ($10-15/episode)

Your pricing is closer to Hitman's premium model, requiring **substantial content per episode** (4+ hours minimum).

**Timing is critical.** Research shows:
- **1-2 weeks between episodes**: Best (RE Revelations 2, Dispatch 2025)
- **Monthly**: Acceptable if consistent
- **2-3+ months**: Fatal — causes abandonment and anger
- Phil Spencer (Xbox): "X divided by two is episode two" — expect 50% sales drop-off

**Alternatives to consider:**
1. Release all at once as "chapters" (Life is Strange: True Colors model)
2. Episode 1 free + paid remainder (Bendy model)
3. Very short gaps (weekly/bi-weekly)
4. Have Episode 2 nearly complete before Episode 1 launches

---

## Recommended analysis order

### Weeks 1-2: Foundation
1. **Salt and Sanctuary** — 2-person Souls-like reference
2. **Hollow Knight** — 3-person quality benchmark
3. **Prince of Persia: The Lost Crown** — Persian authenticity gold standard

### Weeks 3-4: Combat and feel
4. **Hades** — Mythology adaptation + combat polish
5. **Sekiro** — Innovative posture/parry system
6. **Ghost of Tsushima** — Detailed GDC combat talks

### Weeks 5-6: Production and constraints
7. **Balatro/Undertale/Stardew Valley** — Budget champion lessons
8. **Cuphead** — Art commitment with tiny team
9. **Never Alone** — Cultural collaboration model

### Weeks 7-8: Cautionary tales
10. **Telltale/Hitman episodic** — What failed and why
11. **Kentucky Route Zero** — Small team episodic dangers
12. **Raji** — Cultural representation pitfalls

---

## High-impact, low-cost techniques for your 2-person team

From combat research:
- **Hit-stop is free**: 2-5 frame pause on impact = massive feel improvement, zero budget
- **Animation commitment**: Fewer cancels = more weight = less animation work needed
- **Visual attack telegraphs**: Color-coded indicators (GoW/GoT model) cheaper than complex AI
- **Generous parry with fallback**: Sekiro model (failed parry = block) balances accessibility/depth
- **Enemy rule parity**: Enemies follow same rules as player = fairness without complexity

From budget research:
- **Free engines are proven**: Löve/Lua (Balatro), Godot, Unity free tier
- **AI tools are viable**: Your Stable Diffusion + Blender approach aligns with successful stylized games
- **Unique mechanic matters most**: Poker roguelike, bullet heaven, etc. — find your hook
- **Streamer-friendly design**: Co-op, shareable moments, reaction-worthy content
- **Low price point**: $10-20 removes purchase friction (your $64.97 total may be barrier)

From cultural research:
- **Farsi voice acting precedent set**: Lost Crown proved this adds authenticity
- **Use actual Shahnameh**: Rostam, Sohrab, Siavash, Zal have rich characterization
- **Distinguish Persian from Arab/Indian**: Common criticism of past games
- **Pre-Islamic focus**: Zoroastrian elements (Simurgh, Azhdaha, Manticore, fire temples) underexplored
- **Visual references**: Persian miniature painting, Persepolis architecture, Sassanid art, traditional instruments (tanbur, daf, oud)

---

## Final recommendation

Your project has a genuine market gap to exploit — no major game has authentically adapted the Shahnameh. Prince of Persia: The Lost Crown proved the audience appetite exists and established a visual/cultural vocabulary you can build from.

**Prioritize**:
1. Extremely tight core combat loop (study Salt and Sanctuary, Sekiro, Ghost of Tsushima)
2. Distinctive visual style that AI tools can help scale (study Hades pen-and-ink, Okami constraint-driven innovation)
3. Authentic Persian elements that distinguish you from "generic exotic East" (study Lost Crown's Zoroastrian approach)
4. Reconsider episodic timing/pricing (industry has abandoned model for good reasons)

The 15 TIER 1 games provide sufficient reference material for complete development — study these deeply before expanding to TIER 2. Your 2-person constraint is actually proven viable: Salt and Sanctuary, Cuphead (started with 2-3), and dozens of solo-dev hits demonstrate the path is possible.